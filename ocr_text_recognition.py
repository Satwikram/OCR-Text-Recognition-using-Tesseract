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
    for i in range(0, numRows):
        scoresData = scores[0, 0, i]
        xData0 = geometry[0, 0, i]
        xData1 = geometry[0, 1, i]
        xData2 = geometry[0, 2, i]
        xData3 = geometry[0, 3, i]
        anglesData = geometry[0, 4, i]

    # Loop over the Columns
