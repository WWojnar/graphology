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
        bestTopEdge = self.findBestTopEdgeCandidatePoints()

        labelStartPoint = bestTopEdge[0]

        self.findLabelCore(labelStartPoint)


        maxThickness = 50
        for point in self.labelCore:
            y = point[0]
            topFoundEdge = (0, 0)
            rangeStart = np.max([point[1] - maxThickness, 0])
            for x in range(point[1] - 1, rangeStart, -1):
                if self.edges[x][y] > 0:
                    topFoundEdge = (y, x)
                    self.topEdgeLabel.append(topFoundEdge)
                    break


            rangeEnd = np.min([point[1] + maxThickness, len(self.edges)])
            bottomFoundEdge = (0, 0)
            for x in range(point[1], rangeEnd):
                if self.edges[x][y] > 0:
                    bottomFoundEdge = (y, x)
                    self.bottomEdgeLabel.append(bottomFoundEdge)
                    break
            if (topFoundEdge != (0, 0) and bottomFoundEdge != (0, 0)):
                self.labelThickness.append(np.abs(topFoundEdge[1] - bottomFoundEdge[1]))

    def findLabelCore(self, labelStartPoint):
        self.labelCore = [labelStartPoint]
        currentPoint = (labelStartPoint[0] + 4, labelStartPoint[1])
        direction = 0
        while (currentPoint[0] < len(self.img[0]) - 10):
            while (currentPoint[0] < len(self.img[0]) - 1 and np.sum(self.img[currentPoint[1]][currentPoint[0]]) > 0):
                currentPoint = (currentPoint[0] + 1, currentPoint[1])
                self.labelCore.append(currentPoint)

            checkRange = self.getRangeForDirection(direction)
            foundPoint = self.findCandidateInVerticalRange(checkRange, currentPoint)
            if foundPoint == (0, 0) and direction != 0:
                checkRange = self.getRangeForDirection(-direction)
                foundPoint = self.findCandidateInVerticalRange(checkRange, currentPoint)

            if foundPoint == (0, 0):
                break
            direction = self.determineVerticalDirection(currentPoint, foundPoint)
            currentPoint = foundPoint
            self.labelCore.append(currentPoint)

    def findCandidateInVerticalRange(self, checkRange, currentPoint):
        foundPoint = (0,0)
        for change in checkRange:
            newPoint = (currentPoint[0], currentPoint[1] + change)
            if (newPoint[1] > 0 and newPoint[1] < len(self.img) and np.sum(self.img[newPoint[1]][newPoint[0]]) > 0):
                foundPoint = newPoint
                break
        return foundPoint

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

    def findBestTopEdgeCandidatePoints(self):
        bestTopEdge = [(0, 0)]
        currentTopEdge = [(0, 0)]
        lastPoint = (0, 0)
        iterationsAfterChangingTopEdge = 0
        for y in range(1, len(self.edges[0])):
            minBestTopEdge = 1000000
            maxBestTopEdge = 0
            for p in bestTopEdge:
                if (minBestTopEdge > p[1]):
                    minBestTopEdge = p[1]
                if (maxBestTopEdge < p[1]):
                    maxBestTopEdge = p[1]

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

    def findStem(self):
        topPoint = (0, 0)
        for x in range(0, len(self.img)):
            for y in range(0, len(self.img[x])):
                if self.edges[x][y] > 0:
                    topPoint = (y, x)
                    break
            if topPoint != (0, 0):
                break

        self.stemCore = [topPoint]

        currentPoint = (topPoint[0], topPoint[1] + 4)

        direction = 0
        while (currentPoint[1] < len(self.img) - 10):
            while (currentPoint[1] < len(self.img) and np.sum(self.img[currentPoint[1]][currentPoint[0]]) > 0):
                currentPoint = (currentPoint[0], currentPoint[1] + 1)
                self.stemCore.append(currentPoint)

            checkRange = self.getRangeForDirection(direction)
            foundPoint = self.findCandidateInHorizontalRange(checkRange, currentPoint)

            if foundPoint == (0,0) and direction !=0:
                checkRange = self.getRangeForDirection(-direction)
                foundPoint = self.findCandidateInHorizontalRange(checkRange, currentPoint)

            if foundPoint == (0, 0):
                break

            direction = self.determineNewHorizontalDirection(currentPoint, foundPoint)

            currentPoint = foundPoint
            self.stemCore.append(currentPoint)


        edgeLeft = []
        edgeRight = []
        thickness = []
        maxThickness = 80
        for point in self.stemCore:
            x = point[1]

            leftFoundEdge = (0, 0)
            edgeCounter = 0
            rangeStart = np.max([point[0] - maxThickness, 0])
            for y in range( point[0] - 1, rangeStart, -1):
                if self.edges[x][y] > 0:
                    leftFoundEdge = (y, x)
                    edgeCounter = 0
                    self.leftEdgeStem.append(leftFoundEdge)
                    break


            rangeEnd = np.min([point[0] + maxThickness, len(self.edges[x])])
            rightFoundEdge = (0, 0)
            for y in range(point[0], rangeEnd):
                if self.edges[x][y] > 0:
                    rightFoundEdge = (y, x)
                    self.rightEdgeStem.append(rightFoundEdge)
                    break
            if (rightFoundEdge != (0, 0) and leftFoundEdge != (0, 0)):
                thickness.append(np.abs(rightFoundEdge[0] - leftFoundEdge[0]))

    def findCandidateInHorizontalRange(self, checkRange, currentPoint):
        foundPoint = (0, 0)
        for change in checkRange:
            newPoint = (currentPoint[0] + change, currentPoint[1])
            if (newPoint[0] > 0 and np.sum(self.img[newPoint[1]][newPoint[0]]) > 0):
                foundPoint = newPoint
                break
        return foundPoint

    def determineNewHorizontalDirection(self, currentPoint, foundPoint):
        if foundPoint[0] > currentPoint[0]:
            direction = 1
        else:
            direction = -1
        return direction

    def analyze(self):
        self.preprocessImage()
        self.findTopLabel()
        self.findStem()

        self.drawPoints(self.topEdgeLabel, Colors.blue)
        self.drawPoints(self.bottomEdgeLabel, Colors.purple)
        self.drawPoints(self.stemCore, Colors.green)
        self.drawPoints(self.rightEdgeStem, Colors.yellow)
        self.drawPoints(self.leftEdgeStem, Colors.orange)
        self.drawPoints(self.labelCore, Colors.red)

        self.analysis["labelTrend"] = self.getLabelTrend()

        self.analysis["labelThickness"] = self.getLabelThicknessAnalysis()

    def getAnalysis(self):
        return self.analysis

    def getResultImg(self):
        return self.img

    def getResultEdges(self):
        return self.edges



if __name__ == '__main__':

    for i in range(1,21):
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
