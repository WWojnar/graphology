import cv2
import numpy as np


def findTopLabel(edges):
    bestTopEdge = [(0, 0)]
    currentTopEdge = [(0, 0)]
    lastPoint = (0, 0)
    for y in range(1, len(edges[0])):
        for x in range(1, len(edges)):
            if edges[x][y] != 0:

                if (abs(bestTopEdge[len(bestTopEdge) - 1][1] - x) < 10 and len(currentTopEdge) < len(bestTopEdge)):
                    currentTopEdge = bestTopEdge
                    lastPoint = bestTopEdge[len(bestTopEdge) - 1]

                if (abs(lastPoint[1] - x) > 5):
                    if len(bestTopEdge) < len(currentTopEdge):
                        bestTopEdge = currentTopEdge
                    currentTopEdge = []

                currentTopEdge.append((y, x))
                lastPoint = (y, x)
                break
    if len(bestTopEdge) < len(currentTopEdge):
        bestTopEdge = currentTopEdge

    return bestTopEdge




img = cv2.imread('tExample.png')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,50,150,apertureSize = 3)
cv2.imshow("edges", edges)


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
    cv2.circle(img, point, 2, (255,0, 0), -1)

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
labelStart = topEdgeLabel[0]
labelEnd = topEdgeLabel[len(topEdgeLabel-1)]







cv2.imshow("result", img)

while True:
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
