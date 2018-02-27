import cv2
import numpy as np
import time
cap = cv2.VideoCapture("test.mp4")
ret, frame1 = cap.read()
if ret is True:
    prvs = cv2.cvtColor(frame1,cv2.COLOR_BGR2GRAY)
hsv = np.zeros_like(frame1)
hsv[...,1] = 255
cnt=0
path = './flow_result/'
starttime = time.time()
while(1):
    cnt=cnt+1
    ret, frame2 = cap.read()
    if ret is True:
        next = cv2.cvtColor(frame2,cv2.COLOR_BGR2GRAY)
    flow = cv2.calcOpticalFlowFarneback(prvs,next, None, 0.5, 3, 15, 3, 5, 1.2, 0)
    mag, ang = cv2.cartToPolar(flow[...,0], flow[...,1])
    hsv[...,0] = ang*180/np.pi/2
    hsv[...,2] = cv2.normalize(mag,None,0,255,cv2.NORM_MINMAX)
    bgr = cv2.cvtColor(hsv,cv2.COLOR_HSV2BGR)
    cv2.imshow('frame2',bgr)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
    else:
        #cv2.imwrite(path+str(cnt)+'.png',frame2)
        cv2.imwrite(path+str(cnt)+'.png',bgr)
    prvs = next
    print (time.time())
   
    time.sleep(0.04 - (int(100*(time.time() - starttime)) % 4)*0.01)

cap.release()
cv2.destroyAllWindows()
