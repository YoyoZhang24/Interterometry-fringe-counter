import cv2
import numpy as np
import matplotlib.pyplot as plt
import math

cap = cv2.VideoCapture("trial2.mov")

# Get the first frame of the video
ret, frame = cap.read()

# Convert the frame to grayscale
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


# Set ROI
xcenter = 871
ycenter = 244
w = 96
h = 76

x1 = xcenter-math.floor(w/2)
x2 = xcenter+math.floor(w/2)
y1 = ycenter-math.floor(h/2)
y2 = ycenter+math.floor(h/2)


# Set threshold
threshold = 148

roi = gray[x1:x2, y1:y2]

count = 0
bright_frames = 0
flag = False

r_history = []
while True:

    ref, frame = cap.read()

    if not ref:
        break

    # ROI ([row, col])
    roi = frame[x1:x2, y1:y2]
    r_history.append(np.mean(roi))
    print(np.mean(roi))
    # import ipdb; ipdb.set_trace()

    # Check if intensity of pixels in the ROI is above the threshold
    if np.mean(roi) > threshold: 
        bright_frames += 1
        #print('bright:', np.mean(roi))
        if flag == False:
            count += 1
        flag = True
    else:
        #print('dark:', np.mean(roi))
        flag = False

cap.release()

print("Total count:", count)
print(bright_frames)

# print(r_history)
# plt.plot(r_history)
# plt.show()