#python_flask_opencv_video_streaming
#Author: Md. Nadimozzaman Pappo
#Company: GoonFol
#Inspired By: https://blog.miguelgrinberg.com/post/video-streaming-with-flask

import cv2

class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture('http://admin:Apekkhik@007@192.168.1.108/cgi-bin/realmonitor.cgi?action=getStream&channel=1&subtype=1')

    def __del__(self):
        self.video.release()

    def get_frame(self):
        _, image = self.video.read()
        _, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()
