from datetime import datetime
import traceback

import cv2

done = False

while not done:
    try:
        cap = cv2.VideoCapture("rtsp://tzeny:ghtwaylat@192.168.0.102/live")

        output_path = '/home/pi/opencv-python-timelapse/output/'

        while(cap.isOpened()):
            ret, frame = cap.read()
            
            datetime = datetime.now().strftime("%d.%m.%Y-%H:%M:%S")

            cv2.imwrite(output_path + datetime + '.jpg', frame)

            break

        cap.release()
        done = True
    except:
        print('Error capturing frame at ' + datetime.now().strftime("%d.%m.%Y-%H:%M:%S"))
        traceback.print_exc()
