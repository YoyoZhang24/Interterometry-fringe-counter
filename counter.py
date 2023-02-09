import cv2
import numpy as np
import matplotlib.pyplot as plt
import math

cap = cv2.VideoCapture("trial4.mov")

# Get the first frame of the video
ret, frame = cap.read()

# Convert the frame to grayscale
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

# Set threshold
threshold = 164

# Set ROI
xcenter = 622
ycenter = 624
w = 20
h = 20

x1 = xcenter-math.floor(w/2)
x2 = xcenter+math.floor(w/2)
y1 = ycenter-math.floor(h/2)
y2 = ycenter+math.floor(h/2)

roi = gray[x1:x2, y1:y2]

count = 0
r_history = []
bright = [0]
dark = [0]
flag = False


while True:

    ref, frame = cap.read()

    if not ref:
        break

    # ROI ([row, col])
    roi = frame[x1:x2, y1:y2]
    intensity = np.mean(roi)

    r_history.append(intensity)
    print(intensity)
    # import ipdb; ipdb.set_trace()

    # Check if intensity of pixels in the ROI is above the threshold
    if np.mean(roi) > threshold: 
        bright.append(intensity)
        print('bright')
        if flag == False:
            count += 1
        flag = True
    else:
        dark.append(intensity)
        print('dark')
        flag = False

cap.release()

print("Total count:", count)
print("Bright avg intensity:", sum(bright) / len(bright))
print("Dark avg intensity:", sum(dark) / len(dark))

# print(r_history)
plt.plot(r_history)
plt.show()
