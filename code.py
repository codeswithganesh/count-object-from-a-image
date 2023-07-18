

#count objects from image

import cv2
import numpy as np
import matplotlib.pyplot as plt
import cvlib as cv
from cvlib.object_detection import draw_bbox
from numpy.lib.polynomial import poly
image = cv2.imread("example.jpeg")
plt.imshow(image)
box,label,count=cv.detect_common_objects(image)
output=draw_bbox(image,box,label,count)
plt.imshow(image)
arr=['bus','car','person','dog','truck','cat','apple']
for i in arr:
    print(i,label.count(i))

    
