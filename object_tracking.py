import cv2
import time
import math

video = cv2.VideoCapture("bb3.mp4")
#load tracker
tracker=cv2.TrackerCSRT_create()
#read the first frame of the video 
returned, img=video.read()
#select the bonding box on the image 
bbox=cv2.selectROI("Tracking",img, False) 
# initialize the tracker on the img and the bbox
tracker.init(img,bbox)
print(bbox)
 
def drawBox(img,bbox):
    x,y,w,h=int(bbox[0]),int(bbox[1]),int(bbox[2]),int(bbox[3])
    cv2.rectangle(img,(x,y),((x+w),(y+h)),(255,0,255),3,1)
    cv2.putText(img,"Tracking",(75,90),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,255,0),2)
while True:
    check,img = video.read()
    #update the tracker on the img and the bbox  
    success, bbox=tracker.update(img)
    if success:
        drawBox(img,bbox)
    else:
        cv2.putText(img,"lost",(75,90),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255),2)

    cv2.imshow("result",img)
            
    key = cv2.waitKey(25)

    if key == 32:
        print("Stopped!")
        break


video.release()
cv2.destroyALLwindows()



