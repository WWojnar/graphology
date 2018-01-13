import cv2
import numpy as np


class Colors:
    blue = (255, 0, 0)
    purple = (255, 0, 255)
    green = (0, 255, 0)
    lightGreen = (150, 255, 150)
    red = (0, 0, 255)
    yellow = (0, 255, 255)
    lightBlue = (0, 255, 255)
    orange = (0, 125, 255)


class TDataExtractor:
    maxEdgeThickness = 50
    maxStemThickness = 80
    def __init__(self, img):
        self.img = img
        self.analysis = {}
        self.labelCore = []
        self.topEdgeLabel = []
        self.bottomEdgeLabel = []
        self.labelThickness = []
        self.stemCore = []
        self.leftEdgeStem = []
        self.rightEdgeStem = []
        self.stemThickness = []

    def drawPoints(self, points, color):
        for point in points:
            cv2.circle(self.img, point, 1, color, -1)

    def preprocessImage(self):
        # gray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        ret, thresholded = cv2.threshold(self.img, 180, 255, cv2.THRESH_BINARY_INV)
        kernel = np.ones((5, 5), np.uint8)

        closing = cv2.morphologyEx(thresholded, cv2.MORPH_CLOSE, kernel)

        self.edges = cv2.Canny(closing, 50, 150, apertureSize=3)
        self.img = closing

    def findTopLabel(self):
        bestTopEdge = self.findBestTopEdgeLeftMostCandidatePoint()
        labelStartPoint = bestTopEdge[0]
        self.findLabelCore(labelStartPoint)
        self.findLabelEdgesAndThickness()

    # This function will look for the longest horizontal edge, this edge can have a gap if it keeps it trend
    def findBestTopEdgeLeftMostCandidatePoint(self):
        bestTopEdge = [(0, 0)]
        currentTopEdge = [(0, 0)]
        lastPoint = (0, 0)
        iterationsAfterChangingTopEdge = 0
        for y in range(1, len(self.edges[0])):
            maxBestTopEdge, minBestTopEdge = self.findMinAndMaxVertical(bestTopEdge)
            for x in range(1, len(self.edges)):
                if self.edges[x][y] != 0:
                    if (len(currentTopEdge) < len(bestTopEdge) and iterationsAfterChangingTopEdge > 10
                        and (abs(minBestTopEdge - x) < 40 or abs(maxBestTopEdge - x) < 40 or (
                                        x > minBestTopEdge and x < maxBestTopEdge))):
                        currentTopEdge = bestTopEdge
                        iterationsAfterChangingTopEdge = 0
                    else:
                        if (abs(lastPoint[1] - x) > 5):
                            if len(bestTopEdge) < len(currentTopEdge):
                                bestTopEdge = currentTopEdge
                            currentTopEdge = []
                            iterationsAfterChangingTopEdge = 0
                    iterationsAfterChangingTopEdge += 1
                    currentTopEdge.append((y, x))
                    lastPoint = (y, x)
                    break
        if len(bestTopEdge) < len(currentTopEdge):
            bestTopEdge = currentTopEdge
        return bestTopEdge

    def findLabelEdgesAndThickness(self):
        for point in self.labelCore:
            topFoundEdge = self.findAndAddTopEdgePoint(point)
            bottomFoundEdge = self.findAndAddBottomEdgePoint(point)
            if (topFoundEdge != (0, 0) and bottomFoundEdge != (0, 0)):
                self.labelThickness.append(np.abs(topFoundEdge[1] - bottomFoundEdge[1]))

    def findAndAddBottomEdgePoint(self, point):
        y = point[0]
        rangeEnd = np.min([point[1] + TDataExtractor.maxEdgeThickness, len(self.edges)])
        bottomFoundEdge = (0, 0)
        for x in range(point[1], rangeEnd):
            if self.edges[x][y] > 0:
                bottomFoundEdge = (y, x)
                self.bottomEdgeLabel.append(bottomFoundEdge)
                break
        return bottomFoundEdge

    def findAndAddTopEdgePoint(self, point):
        y = point[0]
        topFoundEdge = (0, 0)
        rangeStart = np.max([point[1] - TDataExtractor.maxEdgeThickness, 0])
        for x in range(point[1] - 1, rangeStart, -1):
            if self.edges[x][y] > 0:
                topFoundEdge = (y, x)
                self.topEdgeLabel.append(topFoundEdge)
                break
        return topFoundEdge

    def findLabelCore(self, labelStartPoint):
        self.labelCore = [labelStartPoint]
        currentPoint = (labelStartPoint[0] + 4, labelStartPoint[1])
        direction = 0
        while (currentPoint[0] < len(self.img[0]) - 10):
            currentPoint = self.addAsManyPointsAsPossibleToTheRight(currentPoint)
            foundPoint = self.findCandidatePointAboveOrBelow(currentPoint, direction)
            if foundPoint == (0, 0):
                break
            direction = self.determineVerticalDirection(currentPoint, foundPoint)
            currentPoint = foundPoint
            self.labelCore.append(currentPoint)

    def addAsManyPointsAsPossibleToTheRight(self, currentPoint):
        while (currentPoint[0] < len(self.img[0]) - 1 and np.sum(self.img[currentPoint[1]][currentPoint[0]]) > 0):
            currentPoint = (currentPoint[0] + 1, currentPoint[1])
            self.labelCore.append(currentPoint)
        return currentPoint

    def findCandidatePointAboveOrBelow(self, currentPoint, direction):
        checkRange = self.getRangeForDirection(direction)
        foundPoint = self.findCandidateInVerticalRange(checkRange, currentPoint)
        if foundPoint == (0, 0) and direction != 0:
            checkRange = self.getRangeForDirection(-direction)
            foundPoint = self.findCandidateInVerticalRange(checkRange, currentPoint)
        return foundPoint

    def findCandidateInVerticalRange(self, checkRange, currentPoint):
        foundPoint = (0,0)
        for change in checkRange:
            newPoint = (currentPoint[0], currentPoint[1] + change)
            if (newPoint[1] > 0 and newPoint[1] < len(self.img) and np.sum(self.img[newPoint[1]][newPoint[0]]) > 0):
                foundPoint = newPoint
                break
        return foundPoint

    # TODO: some helpers?
    def determineVerticalDirection(self, currentPoint, foundPoint):
        if foundPoint[1] > currentPoint[1]:
            direction = 1
        else:
            direction = -1
        return direction

    def getRangeForDirection(self, direction):
        if direction == 0:
            checkRange = [-2, 2, -5, 5, -10, 10, -17, 17, -25, 25, -40, 40]
        else:
            checkRange = [direction * 2, direction * 5, direction * 10, direction * 17, direction * 25,
                          direction * 40]
        return checkRange



    def findMinAndMaxVertical(self, bestTopEdge):
        minBestTopEdge = 1000000
        maxBestTopEdge = 0
        for p in bestTopEdge:
            if (minBestTopEdge > p[1]):
                minBestTopEdge = p[1]
            if (maxBestTopEdge < p[1]):
                maxBestTopEdge = p[1]
        return maxBestTopEdge, minBestTopEdge

    def findStem(self):
        topPoint = self.findTopPoint()
        self.findStemCore(topPoint)
        self.findStemEdgesAndThickness()

    def findTopPoint(self):
        topPoint = (0, 0)
        for x in range(0, len(self.img)):
            for y in range(0, len(self.img[x])):
                if self.edges[x][y] > 0:
                    topPoint = (y, x)
                    break
            if topPoint != (0, 0):
                break
        return topPoint

    def findStemCore(self, topPoint):
        self.stemCore = [topPoint]
        currentPoint = (topPoint[0], topPoint[1] + 4)
        direction = 0
        while (currentPoint[1] < len(self.img) - 10):
            while (currentPoint[1] < len(self.img) and np.sum(self.img[currentPoint[1]][currentPoint[0]]) > 0):
                currentPoint = (currentPoint[0], currentPoint[1] + 1)
                self.stemCore.append(currentPoint)
            foundPoint = self.findCandidateInHorizontalRange(self.getRangeForDirection(direction), currentPoint)
            if foundPoint == (0, 0) and direction != 0:
                foundPoint = self.findCandidateInHorizontalRange(self.getRangeForDirection(-direction), currentPoint)
            if foundPoint == (0, 0):
                break
            direction = self.determineNewHorizontalDirection(currentPoint, foundPoint)
            currentPoint = foundPoint
            self.stemCore.append(currentPoint)


    def findCandidateInHorizontalRange(self, checkRange, currentPoint):
        foundPoint = (0, 0)
        for change in checkRange:
            newPoint = (currentPoint[0] + change, currentPoint[1])
            if (newPoint[0] > 0 and np.sum(self.img[newPoint[1]][newPoint[0]]) > 0):
                foundPoint = newPoint
                break
        return foundPoint


    def findStemEdgesAndThickness(self):
        for point in self.stemCore:
            leftFoundEdge = self.findAndAddLeftEdgePoint(point)
            rightFoundEdge = self.findAndAddRightEdgePoint(point)
            if (rightFoundEdge != (0, 0) and leftFoundEdge != (0, 0)):
                self.stemThickness.append(np.abs(rightFoundEdge[0] - leftFoundEdge[0]))

    def findAndAddRightEdgePoint(self, point):
        x = point[1]
        rangeEnd = np.min([point[0] + TDataExtractor.maxStemThickness, len(self.edges[x])])
        rightFoundEdge = (0, 0)
        for y in range(point[0], rangeEnd):
            if self.edges[x][y] > 0:
                rightFoundEdge = (y, x)
                self.rightEdgeStem.append(rightFoundEdge)
                break
        return rightFoundEdge

    def findAndAddLeftEdgePoint(self, point):
        x = point[1]
        leftFoundEdge = (0, 0)
        rangeStart = np.max([point[0] - TDataExtractor.maxStemThickness, 0])
        for y in range(point[0] - 1, rangeStart, -1):
            if self.edges[x][y] > 0:
                leftFoundEdge = (y, x)
                self.leftEdgeStem.append(leftFoundEdge)
                break
        return leftFoundEdge

    def determineNewHorizontalDirection(self, currentPoint, foundPoint):
        if foundPoint[0] > currentPoint[0]:
            direction = 1
        else:
            direction = -1
        return direction





    def getLabelThicknessAnalysis(self):
        poly = np.polyfit(range(0, len(self.labelThickness)), self.labelThickness, 1)
        # [ 0.21965908  8.96886355] - rosnaca
        # [ -0.08947244  61.56185738] -malejaca
        # [ -3.54252225e-03   2.54786461e+01] - rowne
        # patrzymy na 1 parametr aby analizowac wzrost - spadek - jak fukncja liniowa

        if abs(poly[0]) < 0.05:
            return "constant"
        else:
            if poly[0] > 0:
                return "rising"
            else:
                return "falling"

    def getLabelTrend(self):
        labelStart = self.labelCore[np.min([len(self.labelCore)-1, 5])]
        labelEnd = self.labelCore[np.max([len(self.labelCore) - 5, 0])]
        averageThicknessLabel = np.average(self.labelThickness)
        if (abs(labelStart[1] - labelEnd[1]) < averageThicknessLabel * 1.5):
            return "vertical"
        else:
            if labelStart[1] < labelEnd[1]:
                return "falling"
            else:
                return "rising"

    def getCrossingLengthAnalysis(self):
        stemLength =self.stemCore[len(self.stemCore)-1][1]-self.stemCore[0][1] +0.0
        labelLength= self.labelCore[len(self.labelCore)-1][0]-self.labelCore[0][0] +0.0
        ratio = stemLength/labelLength -1.2
        print ratio
        if(abs(ratio)< 0.25):
            return "normal"
        else:
            if ratio>0:
                return "short"
            else:
                return "long"


    def analyze(self):
        self.preprocessImage()
        self.findTopLabel()
        self.findStem()

        self.drawAll()
        self.analysis["labelTrend"] = self.getLabelTrend()
        self.analysis["labelThickness"] = self.getLabelThicknessAnalysis()
        self.analysis["crossingLength"] = self.getCrossingLengthAnalysis()

    def drawAll(self):
        self.drawPoints(self.topEdgeLabel, Colors.blue)
        self.drawPoints(self.bottomEdgeLabel, Colors.purple)
        self.drawPoints(self.stemCore, Colors.green)
        self.drawPoints(self.rightEdgeStem, Colors.yellow)
        self.drawPoints(self.leftEdgeStem, Colors.orange)
        self.drawPoints(self.labelCore, Colors.red)

    def getAnalysis(self):
        return self.analysis

    def getResultImg(self):
        return self.img

    def getResultEdges(self):
        return self.edges



if __name__ == '__main__':

    for i in range(20,21):
        img = cv2.imread('tImages/t' + str(i) + '.png')

        extractor = TDataExtractor(img)
        extractor.analyze()

        analysis = extractor.getAnalysis()
        resultImg = extractor.getResultImg()
        cv2.imshow("result" + str(i), resultImg)
        print "image :", str(i)
        print analysis
        # resultEdged = extractor.getResultEdges()
        # cv2.imshow("edges" + str(i), resultEdged)

    while True:
        key = cv2.waitKey(1)
        if key == ord('q'):
            break
