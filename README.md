# MultiCameraSystem

Task 1: Multi-camera Setup & Recording


1.1 Collect three cameras within your home (smart phones, laptop camera etc) or from your friends,
project partners etc. In the worse case scenario you can search for a multi-camera dataset on the
web and use it for the project but that would result in deduction in marks.

1.2 Install IP Webcam app (or other similar app) on each of the smart phone

1.3 Open camera on smart phones and test the video feed on your laptop using VLC player

1.4 Use the given python and OpenCV code to record the feed from all these cameras on your hard
drive. The program should also optionally display the live feed from all three cameras. 


Task 2: Mask/Non-Mask Person Detection

In this task you are required to detect people and also classify them as those wearing masks and
those who are not wearing mask. To classify mask/non-mask people you can create a dataset of
faces only followed by binary classifier or you can update YOLO to directly give localisation and
classification.

2.1 Setup and run YOLO object detector

2.2 From the recorded videos annotate few people or faces from each of the camera view using
LabelMe software

2.3 Either fine tune the YOLO object detector using the generated annotations to detect separate
bounding boxes with separate class information for mask/non-mask persons. Depending upon your
data you may fine tune n different versions of YOLO one for each camera view

Task 3: Orthographics Top-View Generation 

3.1 Either using Google maps or otherwise obtain a top-view of the site

3.2 Mark (either manually or using GPS coordinates) the position of each camera on the top- view.

3.3 Find the corresponding points between top-view image and your camera image from first
camera

3.4 Compute the homography between the corresponding points

3.5 Project the camera view on the top-view using the computed homography and produce a topview video of the camera view (this option should work for both online and offline modes discussed earlier i.e. live feed and pre-recorded videos respectively)

3.6 Repeat the above process for all the cameras

3.7 Combine all the top-view videos into a single top-view video of the site. In this task a frame from
each of the camera will be obtained and projected on the common top-view and then you go to the
next frame and repeat the process in this way you will result in a top-view video feed. If there are
speed limitations in your own implementation of warping you can use the OpenCV implementation
instead. Your final visualisation should show live feed from all the cameras as well as the generate
top-view video 
