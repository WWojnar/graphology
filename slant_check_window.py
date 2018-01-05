import cv2
import numpy as np
from slantAnalyser import SlantAnalyser

def onChange(pos):
    global img
    global gray
    global dst

    dst = np.copy(img)

    width, height = img.shape[:2]

    linesGap = cv2.getTrackbarPos("Distance between lines", "Result")
    angle = cv2.getTrackbarPos("Angle", "Result")

    a = np.tan(angle*2*np.pi / 360)

    print a

    print width
    print linesGap
    print np.arange(0,2*width,int(linesGap))

    for i in np.arange(-5*width,5*width,int(linesGap)):
        x1 = i
        y1 = 0
        x2 = int((height + a*x1)/a)
        y2 = height
        cv2.line(dst, (x1, y1), (x2, y2), (0, 255, 0), 2)

    analysis = SlantAnalyser.analyzeSlant([180-angle])

    print analysis[0]["slantType"]
    print analysis[0]["analysis"]



    # if a != 0:
    #     cv2.line(dst,(100, 100),(200, 100+ int(100*a)),(0,255,0),2)
    # else:




#Run Main
if __name__ == "__main__" :

    img = cv2.imread("slantImages/inclined.jpg", -1)

    dst = np.copy(img)

    cv2.namedWindow("Result", cv2.WINDOW_NORMAL)

    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


    # according to OpenCV, aperture size must be odd and between 3 and 7
    # the aperture size range is (0 - 6)
    cv2.createTrackbar("Distance between lines", "Result", 50, 200, onChange)

    # line length range is (0 - 10)
    cv2.createTrackbar("Angle", "Result", 90, 180, onChange)

    while True:
        cv2.imshow("Result", dst)
        key = cv2.waitKey(1)
        if key == ord('q'):
            break

    cv2.destroyAllWindows()