import numpy as np
import cv2
import picamera
import picamera.array
import time

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')

first_read = True
blink_detected = False
last_blink_time = ""

with picamera.PiCamera() as camera:
    # Set the desired resolution and frame rate
    camera.resolution = (400, 300)
    camera.framerate = 30

    # Create an array to store the video frames
    stream = picamera.array.PiRGBArray(camera)

    # Continuously capture and process video frames
    for frame in camera.capture_continuous(stream, format='bgr', use_video_port=True):
        # Retrieve the image array from the frame
        img = frame.array

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gray = cv2.bilateralFilter(gray, 5, 1, 1)

        faces = face_cascade.detectMultiScale(gray, 1.3, 5, minSize=(200, 200))

        if len(faces) > 0:
            for (x, y, w, h) in faces:
                img = cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

                roi_face = gray[y:y+h, x:x+w]
                roi_face_clr = img[y:y+h, x:x+w]
                eyes = eye_cascade.detectMultiScale(roi_face, 1.2, 5, minSize=(40, 40))

                if len(eyes) >= 2:
                    if first_read:
                        cv2.putText(img, "Eye detected press s to begin", (70, 70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 2)
                    else:
                        cv2.putText(img, "Eyes open!", (70, 70), cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), 2)
                    
                        if last_blink_time == "":
                            last_blink_time = time.time()
                            
                        elif time.time() - last_blink_time >= 5:
                            print("Preslo 5 sec")
                            last_blink_time = ""
                else:
                    if first_read:
                        cv2.putText(img, "No eyes detected", (70, 70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 255), 2)
                    else:
                        print("Blink blink ++++++++++++")
                        cv2.waitKey(1000)                        

        else:
            cv2.putText(img, "No face detected", (100, 100), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 2)

        cv2.imshow('img', img)
        a = cv2.waitKey(1)

        if a == ord('q'):
            break
        elif a == ord('s') and first_read:
            first_read = False

        # Clear the stream for the next frame
        stream.seek(0)
        stream.truncate()

cv2.destroyAllWindows()
