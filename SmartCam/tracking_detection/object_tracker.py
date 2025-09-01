# USAGE
# python object_tracker.py --prototxt deploy.prototxt --model res10_300x300_ssd_iter_140000.caffemodel

# import the necessary packages
import base64

import time
import os
from datetime import date, datetime
from .pyimagesearch.centroidtracker import CentroidTracker
from imutils.video import VideoStream
import pandas as pd
import numpy as np
import argparse
import imutils
import time
import cv2
import pandas

def detections(path):

# construct the argument parse and parse the arguments
# ap = argparse.ArgumentParser()
# ap.add_argument("-p", "--prototxt", required=True,
#  help="path to Caffe 'deploy' prototxt file")
# ap.add_argument("-m", "--model", required=True,
#  help="path to Caffe pre-trained model")
# ap.add_argument("-c", "--confidence", type=float, default=0.5,
#  help="minimum probability to filter weak detections")
# args = vars(ap.parse_args())
   args = {"prototxt":"deploy.prototxt ",
         "model":"res10_300x300_ssd_iter_140000.caffemodel",
         "confidence":0.5}

# initialize our centroid tracker and frame dimensions
   ct = CentroidTracker()
   (H, W) = (None, None)

# load our serialized model from disk
   print("[INFO] loading model...")
   net = cv2.dnn.readNetFromCaffe(args["prototxt"], args["model"])

# initialize the video stream and allow the camera sensor to warmup
   print("[INFO] starting videso stream...")
#frame = cv2.imread("C:/Users/213330962/project/tracking_detection/Screenshots/ester.jpg")

# vs = VideoStream(0).start()
# time.sleep(2.0)

# loop over the frames from the video stream
#while True:
   # read the next frame from the video stream and resize it
# frame = cv2.imread("C:/Users/213330962/project/tracking_detection/Screenshots/ester.jpg")
   pathdata = 'C:/Users/213330962/project/Simple-object-tracking-with-OpenCV/data.txt'
   folder_dir = path
   for images in os.listdir(folder_dir):
      i=0
      frame = cv2.imread(folder_dir + '/' + images)
      frame = imutils.resize(frame, width=400)

   # if the frame dimensions are None, grab them
      if W is None or H is None:
         (H, W) = frame.shape[:2]

   # construct a blob from the frame, pass it through the network,
   # obtain our output predictions, and initialize the list of
   # bounding box rectangles
      blob = cv2.dnn.blobFromImage(frame, 1.0, (W, H),
         (104.0, 177.0, 123.0))
      net.setInput(blob)
      detections = net.forward()
      rects = []

   # loop over the detections
      for i in range(0, detections.shape[2]):
      # filter out weak detections by ensuring the predicted
      # probability is greater than a minimum threshold
         if detections[0, 0, i, 2] > args["confidence"]:
         # compute the (x, y)-coordinates of the bounding box for
         # the object, then update the bounding box rectangles list
            box = detections[0, 0, i, 3:7] * np.array([W, H, W, H])
            rects.append(box.astype("int"))

         # draw a bounding box surrounding the object so we can
         # visualize it
            (startX, startY, endX, endY) = box.astype("int")
            cv2.rectangle(frame, (startX, startY), (endX, endY),
               (0, 255, 0), 2)

   # update our centroid tracker using the computed set of bounding
   # box rectangles
      objects = ct.update(rects)
      tmp=objects
   # loop over the tracked objects
      for (objectID, centroid) in objects.items():
      # draw both the ID of the object and the centroid of the
      # object on the output frame0559857960
         text = "ID {}".format(objectID)
         cv2.putText(frame, text, (centroid[0] - 10, centroid[1] - 10),
            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
         cv2.circle(frame, (centroid[0], centroid[1]), 4, (0, 255, 0), -1)
      curDT = datetime.now().strftime("%H:%M:%S")
   # path.write('id of image: '+text+curDT+'\n')
      import pandas as pd

      dataset = {
         'id': [i],
         'start points': [startX],
         'end points': [endX],
         'time': [curDT],
      #'last time': [i.last_detection.date.time() for i in listOfTrack],
      #'colors': [i.color for i in listOfTrack],
      # 'colors': [for x  for i in listOfTrack in i.last_detection.color]
      # 'color':[i.last_detection.color for i in listOfTrack]
      # 'start time':[i.]
      }
      i+=1
      myvar = pd.DataFrame(dataset)
   # if path.exists('metaData.csv'):
   #myvar.to_csv('metaData.csv', mode='a', index=True, header=False)
   # else:
      myvar.to_csv('metaData.csv', mode='a', index=True, header=True)
   # show the output frame
      cv2.imshow("Frame", frame)
      key = cv2.waitKey(1) & 0xFF

   # if the `q` key was pressed, break from the loop
      if key == ord("q"):
       break
      time.sleep(0.2)
# # do a bit of cleanup
   cv2.destroyAllWindows()
# vs.stop()


