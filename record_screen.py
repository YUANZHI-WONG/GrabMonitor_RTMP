
import cv2
import mss
import numpy as np

import subprocess



rtmp='rtmp://127.0.0.1:2020/live/test'

width=1920
height=1080
fps=130
command = ['ffmpeg',
           '-y',
           '-f', 'rawvideo',
           '-vcodec', 'rawvideo',
           '-pix_fmt', 'bgr24',
           '-s', "{}x{}".format(width, height),
           '-r', str(fps),
           '-i', '-',
           '-c:v', 'libx264',
           '-pix_fmt', 'yuv420p',
           '-preset', 'ultrafast',
           '-f', 'flv',
           rtmp]


#pipe = subprocess.Popen(command  , stdin=subprocess.PIPE                        )
pipe = subprocess.Popen(command, stdin=subprocess.PIPE  )
with mss.mss() as sct:
# Part of the screen to capture
    monitor = {"top": 0, "left": 0, "width": width, "height": height}

    while True:
       
        # Get raw pixels from the screen, save it to a Numpy array

        img = np.array(sct.grab(monitor))
        #img=img.astype(np.uint8)
        img = img[:,:,:3]
        #print(img.shape)       
        # Display the picture
        #cv2.imshow('frame', img)  
                    
        pipe.stdin.write(img.tobytes())

