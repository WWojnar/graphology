import cv2
import numpy as np
from zonesAnalyzer import ZonesAnalyzer

def onChange(pos):
    global img
    global gray
    global dst

    dst = np.copy(img)

    upperZoneTop = cv2.getTrackbarPos("UpperZoneTop", "Result")
    middleZoneTop = cv2.getTrackbarPos("MiddleZoneTop", "Result")
    bottomZoneTop = cv2.getTrackbarPos("BottomZoneTop", "Result")
    bottomZoneBottom = cv2.getTrackbarPos("BottomZoneBottom", "Result")

    cv2.line(dst,(0, upperZoneTop),(20000,upperZoneTop),(0,255,0),2);
    cv2.line(dst,(0, middleZoneTop),(20000,upperZoneTop),(0,255,0),2)
    cv2.line(dst,(0, bottomZoneTop),(20000,upperZoneTop),(0,255,0),2)
    cv2.line(dst,(0, bottomZoneBottom),(20000,upperZoneTop),(0,255,0),2)

    separators = [upperZoneTop, middleZoneTop, bottomZoneTop, bottomZoneBottom]

    print ZonesAnalyzer.analyze(separators)

    print separators


#Run Main
if __name__ == "__main__" :

    img = cv2.imread("zonesImages/middleZone.jpg", -1)

    dst = np.copy(img)

    cv2.namedWindow("Result", cv2.WINDOW_AUTOSIZE)

    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


    # according to OpenCV, aperture size must be odd and between 3 and 7
    # the aperture size range is (0 - 6)
    cv2.createTrackbar("UpperZoneTop", "Result", 0, len(gray), onChange)

    # line length range is (0 - 10)
    cv2.createTrackbar("MiddleZoneTop", "Result", 50, len(gray), onChange)

    # line gap range is (0 - 19)
    cv2.createTrackbar("BottomZoneTop", "Result", 100, len(gray), onChange)

    cv2.createTrackbar("BottomZoneBottom", "Result", 200, len(gray), onChange)

    while True:
        cv2.imshow("Result", dst)
        key = cv2.waitKey(1)
        if key == ord('q'):
            break

    cv2.destroyAllWindows()