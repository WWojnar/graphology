import cv2
import numpy as np


def findVerticalStick(img, edges):

    topPoint = (0,0)
    for x in range(0,len(img)):
        for y in range(0, len(img[x])):
            if edges[x][y] > 0:
                topPoint = (y,x)
                break
        if topPoint != (0,0):
            break
    print "topPoint", topPoint

    verticalStick = [topPoint]

    currentPoint=(topPoint[0], topPoint[1]+4)

    while(currentPoint[1]<len(img)-10):
        while(currentPoint[1]<len(img) and np.sum(img[currentPoint[1]][currentPoint[0]]) >0 ):
            currentPoint = (currentPoint[0], currentPoint[1]+1)
            verticalStick.append(currentPoint)

        #TODO: IMPROVE THIS:
        newPoint=(currentPoint[0]-5, currentPoint[1])
        if(newPoint[0]>0 and np.sum(img[newPoint[1]][newPoint[0]]) >0):
            currentPoint = newPoint
        else:
            newPoint = (currentPoint[0] + 5, currentPoint[1])
            if (newPoint[0] > 0 and np.sum(img[newPoint[1]][newPoint[0]]) > 0):
                currentPoint = newPoint
            else:
                newPoint = (currentPoint[0] - 20, currentPoint[1])
                if (newPoint[0] > 0 and np.sum(img[newPoint[1]][newPoint[0]]) > 0):
                    currentPoint = newPoint
                else:
                    newPoint = (currentPoint[0] + 20, currentPoint[1])
                    if (newPoint[0] > 0 and np.sum(img[newPoint[1]][newPoint[0]]) > 0):
                        currentPoint = newPoint
                    else:
                        break



        verticalStick.append(currentPoint)

    edgeLeft = []
    edgeRight = []
    thickness =[]
    maxThickness = 80
    for point in verticalStick:
        x = point[1]

        leftFoundEdge = (0,0)
        edgeCounter = 0
        for y in range(0, point[0]-1):
            if edges[x][y]>0:
                leftFoundEdge = (y,x)
                edgeCounter = 0
            edgeCounter+=1
        if edgeCounter < maxThickness and leftFoundEdge != (0,0):
            edgeLeft.append(leftFoundEdge)

        rangeEnd = np.min([point[0]+maxThickness, len(edges[x])])
        rightFoundEdge = (0,0)
        for y in range(point[0], rangeEnd):
            if edges[x][y]>0:
                rightFoundEdge = (y,x)
                edgeRight.append( rightFoundEdge )
                break
        if(rightFoundEdge != (0,0) and leftFoundEdge != (0,0)):
            thickness.append(np.abs(rightFoundEdge[0]-leftFoundEdge[0]))





    return (verticalStick, thickness, edgeLeft, edgeRight)



def findTopLabel(edges):
    bestTopEdge = [(0, 0)]
    currentTopEdge = [(0, 0)]
    lastPoint = (0, 0)


    iterationsAfterChangingTopEdge = 0

    for y in range(1, len(edges[0])):

        minBestTopEdge = 1000000
        maxBestTopEdge = 0
        for p in bestTopEdge:
            if(minBestTopEdge > p[1]):
                minBestTopEdge = p[1]
            if(maxBestTopEdge < p[1]):
                maxBestTopEdge = p[1]

        for x in range(1, len(edges)):
            if edges[x][y] != 0:

                if (len(currentTopEdge) < len(bestTopEdge) and iterationsAfterChangingTopEdge> 10
                    and (abs(minBestTopEdge - x) < 25 or abs(maxBestTopEdge-x)< 25 or ( x > minBestTopEdge and x < maxBestTopEdge))):
                    currentTopEdge = bestTopEdge
                    iterationsAfterChangingTopEdge = 0
                else:
                    if (abs(lastPoint[1] - x) > 3):
                        if len(bestTopEdge) < len(currentTopEdge):
                            bestTopEdge = currentTopEdge
                        currentTopEdge = []
                        iterationsAfterChangingTopEdge = 0
                iterationsAfterChangingTopEdge+=1
                currentTopEdge.append((y, x))
                lastPoint = (y, x)
                break



    if len(bestTopEdge) < len(currentTopEdge):
        bestTopEdge = currentTopEdge

    return bestTopEdge







def analyzeT(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresholded = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
    kernel = np.ones((5, 5), np.uint8)

    closing = cv2.morphologyEx(thresholded, cv2.MORPH_CLOSE, kernel)
    opening = cv2.morphologyEx(closing, cv2.MORPH_OPEN, kernel)

    kernel = np.ones((5,5),np.float32)/25
    opening = cv2.filter2D(opening,-1,kernel)
    edges = cv2.Canny(opening, 50, 150, apertureSize=3)

    img = closing
    topEdgeStart = (0, 0)
    topEdgeLabel = findTopLabel(edges)

    bottomEdgeLabel = []
    labelThickness = []

    for point in topEdgeLabel:
        for x in range(point[1]+2, len(edges)):
            if edges[x][point[0]] != 0:
                bottomEdgeLabel.append((point[0],x))
                labelThickness.append(x - point[1])
                break

    for point in topEdgeLabel:
        cv2.circle(img, point, 2, (0,0, 255), -1)

    for point in bottomEdgeLabel:
        cv2.circle(img, point, 2, (0,255, 0), -1)


    print labelThickness

    poly = np.polyfit(range(0, len(labelThickness)), labelThickness, 1)
    print poly


    #[ 0.21965908  8.96886355] - rosnaca
    #[ -0.08947244  61.56185738] -malejaca
    #[ -3.54252225e-03   2.54786461e+01] - rowne
    #patrzymy na 1 parametr aby analizowac wzrost - spadek - jak fukncja liniowa

    if abs(poly[0]) < 0.02:
        print "Label thickness does not increase a lot"
    else:
        if poly[0]>0:
            print "Label thickness grows"
        else:
            print "Label thickness is falling"


    averageThicknessLabel = np.average(labelThickness)

    print "average label thikness : ", averageThicknessLabel
    labelStart = topEdgeLabel[0]
    labelEnd = topEdgeLabel[len(topEdgeLabel)-1]


    print "Label start ", labelStart
    print "Label end", labelEnd


    if(abs(labelStart[1]-labelEnd[1])< averageThicknessLabel * 1.5):
        print "Label is vertical"
    else:
        if labelStart[1] < labelEnd[1]:
            print "Label is falling"
        else:
            print "Label is rising"


    (verticalStick, verticalThickness, leftEdgeStick, rightEdgeStick) = findVerticalStick(img, edges)
    for point in verticalStick:
        cv2.circle(img, point, 2, (125,125, 0), -1)

    print verticalThickness

    for point in leftEdgeStick:
        cv2.circle(img, point, 2, (125,255, 0), -1)
    for point in rightEdgeStick:
        cv2.circle(img, point, 2, (255,125, 0), -1)


    return img





for i in range(1,20):
    img = cv2.imread('tImages/t' + str(i) + '.png')

    img = analyzeT(img)

    cv2.imshow("result" + str(i), img)

while True:
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
