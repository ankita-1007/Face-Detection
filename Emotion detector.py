import cv2 as cv
from deepface import DeepFace

key = cv. waitKey(1)
cam = cv.VideoCapture(0)
while cam.isOpened():
    try:
        check, frame = cam.read()
        # print(check) #prints true as long as the webcam is running
        # print(frame) #prints matrix values of each framecd 
        cv.imshow("Capturing", frame)
        key = cv.waitKey(1)
        if key == ord('c'): 
            cv.imwrite(filename='image.jpeg', img=frame)
	       
            cam.release()
			

        
    except(KeyboardInterrupt):
        print("Turning off camera.")
        cam.release()
        print("Camera off.")
        print("Program ended.")
        cv.destroyAllWindows()
        break


# read the input image
img = cv.imread('image.jpeg')
face_analysis = DeepFace.analyze(img_path = "image.jpeg")
print(face_analysis)
s = [ sub['dominant_emotion'] for sub in face_analysis ]
result=' '.join(s)


position = (170,30)
cv.putText(
     img, #numpy array on which text is written
     result, #text
     position, #position at which writing has to start
     cv.FONT_HERSHEY_SIMPLEX, #font family
     1, #font size
     (209, 80, 0, 255), #font color
     3) #font stroke

# Display an image in a window


cv.imshow('Emotion Detection',img)
cv.waitKey(0)
cv.destroyAllWindows()





