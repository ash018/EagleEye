import cv2
import imutils


class VideoCamera(object):
    
    def __init__(self):
        # Using OpenCV to capture from device 0. If you have trouble capturing
        # from a webcam, comment the line below out and use a video file
        # instead.
        self.video = cv2.VideoCapture(0)
		
        # If you decide to use video.mp4, you must have this file in the folder
        # as the main.py.
        # self.video = cv2.VideoCapture('video.mp4')
    
    def __del__(self):
        self.video.release()
    
    def get_frame(self):
        success, image = self.video.read()
        image = imutils.resize(image, width=500)
        frame_count += 1
        print(frame_count)
        # We are using Motion JPEG, but OpenCV defaults to capture raw images,
        # so we must encode it into JPEG in order to correctly display the
        # video stream.
        inside_count = 0
        cv2.putText(image, "Number of people inside: {}".format(inside_count), (10, 20),
		cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
        cv2.line(image, (400,0), (400,500), (255, 0, 0), 2)
        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()