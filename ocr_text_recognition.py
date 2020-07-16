# import the necessary packages

from imutils.object_detection import non_max_suppression
import numpy as np
import cv2
import pytesseract
import argparse

def decode_predictions(scores, geometry):
    # grab the number of rows and columns from the scores volume, then
    # initialize our set of bounding box rectangles and corresponding
    # confidence scores
    (numRows, numCols) = scores.shape[2:4]
    rects = []
    confidence = []

    # Loop overs the number of Rows
    for y in range(0, numRows):
        scoresData = scores[0, 0, y]
        xData0 = geometry[0, 0, y]
        xData1 = geometry[0, 1, y]
        xData2 = geometry[0, 2, y]
        xData3 = geometry[0, 3, y]
        anglesData = geometry[0, 4, y]

    # Loop over the Columns
    for x in range(0, numCols):
        if scoresData[x] < args["min_confidence"]:
            continue
        # compute the offset factor as our resulting feature
        # maps will be 4x smaller than the input image
        (offsetX, offsetY) = (x * 4.0, y * 4.0)

        # extract the rotation angle for the prediction and
        # then compute the sin and cosine
        angle = anglesData[x]
        cos = np.cos(angle)
        sin = np.sin(angle)

        # use the geometry volume to derive the width and height
        # of the bounding box
        h = xData0[x] + xData2[x]
        w = xData1[x] + xData3[x]

