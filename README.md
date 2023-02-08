# Interterometry-fringe-counter
This program counts the number of fringes passed in an interference pattern from a video.

# Installation
```pip install opencv-python```

```pip install numpy```

```pip install matplotlib```

```pip install math```

# Pre-processing
The input video must be recorded at a stationary position. There should be nothing obstructing the interference pattern in the frame. Ideally, there would be a high contrast between the dark spots (backdrop) and the bright spots. The video should contain a reasonable amount of background around the intereference pattern.

Set the path to the video file in ```cap = cv2.VideoCapture("video_file")```

Find the Region of Interest (ROI) in the video where all the pixels are dark or bright throughout the video. In ```counter.py```, Set the pixel values for ```xcenter```, ```ycenter```, ```w```, and ```h```. 

Test run ```counter.py``` to see the average intensity values of ROI during each bright/dark cycle. Set a reasonable number as ```threshold```. 

# Run the program
```python counter.py```
