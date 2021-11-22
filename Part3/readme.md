Part 3 of Assignment
3.1 Either using Google maps or otherwise obtain a top-view of the site

3.2 Mark (either manually or using GPS coordinates) the position of each camera on the top- view.

3.3 Find the corresponding points between top-view image and your camera image from first
camera

3.4 Compute the homography between the corresponding points

3.5 Project the camera view on the top-view using the computed homography and produce a topview video of the camera view (this option should work for both online and offline modes discussed
earlier i.e. live feed and pre-recorded videos respectively)

3.6 Repeat the above process for all the cameras

3.7 Combine all the top-view videos into a single top-view video of the site. In this task a frame from
each of the camera will be obtained and projected on the common top-view and then you go to the
next frame and repeat the process in this way you will result in a top-view video feed. If there are
speed limitations in your own implementation of warping you can use the OpenCV implementation
instead. Your final visualisation should show live feed from all the cameras as well as the generate
top-view video 
