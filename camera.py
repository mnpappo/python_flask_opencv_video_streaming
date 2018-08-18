#python_flask_opencv_video_streaming
#Author: Md. Nadimozzaman Pappo
#Company: GoonFol
#Inspired By: https://blog.miguelgrinberg.com/post/video-streaming-with-flask
#Source: https://github.com/goonfol/python_flask_opencv_video_streaming

import cv2

class VideoCamera(object):
    def __init__(self):
        video_source = 'http://admin:Apekkhik@007@192.168.1.108/cgi-bin/realmonitor.cgi?action=getStream&channel=1&subtype=1'
        # Video Source can be any video file(.mp4,...) supported by opencv, 
        # # raspberry pi camera or any com port like webcam, even a ipcamera stream output
        # Here I have tested it with IP Camera (DAHUA DH-IPC-HFW1120SP)
        self.video = cv2.VideoCapture(video_source)

    def __del__(self):
        self.video.release()

    def get_frame(self):
        _, image = self.video.read()
        _, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()
