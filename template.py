import cv2

cam = cv2.VideoCapture(0)

cv2.namedWindow("Python Webcam Screenshot App")

# Capture and process frames here

# Release the camera when done
cam.release()

# Close all OpenCV windows
cv2.destroyAllWindows()