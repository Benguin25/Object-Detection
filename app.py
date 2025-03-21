import cv2

cam = cv2.VideoCapture(0)

cv2.namedWindow("Python Webcam Screenshot App")

# Capture and process frames here
img_counter = 1

while True:
    ret, frame = cam.read()

    if not ret:
        print ("Failed to grab frame.")
        break

    cv2.imshow("Camera Capture", frame)

    k = cv2.waitKey(1)

    if k%256 == 27:
        print ("Escape hit, closing the app")
        break
    elif k%256 == 32:
        img_name = "opencv_frame_" + str(img_counter) + ".png"
        cv2.imwrite(img_name, frame)
        print ("screenshot #" + str(img_counter) + " taken")
        img_counter+=1

# Release the camera when done
cam.release()

# Close all OpenCV windows
cv2.destroyAllWindows()