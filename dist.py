import cv2
import numpy as np
from scipy.spatial import distance
from dist_analyzer import DistAnalyzer

point=[]
pixels=[]

def pointer(event, x, y, flags, param):
	global point, dist, ratio, pixels, left, right
	if event == cv2.EVENT_LBUTTONDOWN:
		point.append((x, y))
		cv2.circle(dst,(x,y),2,(255,0,0),-1)

	elif event == cv2.EVENT_LBUTTONUP:
		left = 0
		right = 0
	
	#left
		for l in range(x,x-50):

			if img_data[y,l][0] == 255:
				left += 1
	#right
		for r in range(x,x+50):
			
			if img_data[y,r][0]  == 255:
				right += 1

	

		dist = left + right	
		ratio = dist/text
	 	print DistAnalyzer.analyze(ratio)

def onChange(pos):
	global img, gray, dst, text

	dst = np.copy(img)
	top = cv2.getTrackbarPos("Top", "test")
	bottom = cv2.getTrackbarPos("Bottom", "test")

 	cv2.line(dst,(0, bottom),(20000, bottom),(255,0,0),1)
 	cv2.line(dst,(0, top),(20000, bottom),(255,0,0),1)

	text = bottom - top

if __name__ == "__main__" :
	global h, w
	img = cv2.imread("well_balanced.jpg", -1)
   	dst = np.copy(img)
   	h, w = img.shape[:2]
   	img_data = np.asarray(img)
   	cv2.namedWindow("test", cv2.WINDOW_AUTOSIZE)
	gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	cv2.createTrackbar("Top", "test", 0, len(gray), onChange)
	cv2.createTrackbar("Bottom", "test", 50, len(gray), onChange)
	cv2.setMouseCallback("test", pointer)

	while True:
        	cv2.imshow("test", dst)
        	key = cv2.waitKey(1)
        	if key == ord('q'):
			break

	cv2.destroyAllWindows()


