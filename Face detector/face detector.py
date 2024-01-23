# Face Detector
# Developed and implemented a highly efficient face detection program capable of accurately detecting faces in both images and videos 
import cv2

# Pre-trained face detector file
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

video = cv2.VideoCapture('Full video name ex:-20220221_214621.mp4')
# image = cv2.imread('1.jpg')
# image = cv2.imread('2.png')

while True:
    # Read a frame from the video capture
    ret, frame = video.read()

    if not ret:
        print("Finished...")
        break

    # Resizing the Image
    # img = cv2.resize(image,None,fx=0.3,fy=0.3)

    # Resize the video for better processing speed
    frame = cv2.resize(frame,None,fx=0.3,fy=0.3)

    # Converting the image into grayscale image
    # imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Converting the video into grayscale video
    frameGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detecting The Faces
    # faces = face_cascade.detectMultiScale(imgGray, 1.2, 5)
    faces = face_cascade.detectMultiScale(frameGray, 1.2, 5)

    # Pointing The Faces
    # for (x,y,w,h) in faces:
        # cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0),2)

    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0),2)

    cv2.imshow('Video', frame)
    # cv2.imshow('Img', faces)
    # print("True, Faces available in this picture")

    # Break the loop when 'q' key is pressed
    # One time q press for video pause Two time for close the video 
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.waitKey()
video.release()
cv2.destroyAllWindows() 