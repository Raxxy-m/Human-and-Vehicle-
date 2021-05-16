# Human and Vehicle Detection
Object detection is a computer vision technique that allows us to identify and locate objects in an image or video. With this kind of identification and localization, object detection can be used to count objects in a scene and determine and track their precise locations, all while accurately labelling them. We can use the methods of object detection for various different specialized applications and here we use them for Human and Vehicle detection. Human detection is the task of locating all instances of human beings present in an image, whereas vehicle detection is task to do the same but with vehicles like buses, cars etc. Human detection and tracking are generally considered the first two processes in a video surveillance pipeline, and can feed into higher-level reasoning modules such as action recognition and dynamic scene analysis. 
These detection methods rely on OpenCV, a computer vision specialized library of python. It has over 2500 optimized machine learning algorithms which can be used to detect faces, identify objects, tracking camera movements and much more. But for our project we just needed its object identification powers. 
I also used a library of python called imutils which contains functions for image processing, like resizing, rotation, translation etc. 
 
**Built with**  
* Pycharm 
* Jupyter Notebook

**Getting Started**  
Make sure the video files and xml file and the python notebook/ python file are all stored in the same directory and if not then make sure the path address is correct.

**Prerequisites**   
This project requires you to have the basic knowledge of python and its syntax. The basic knowledge of opencv is essential, but in-depth working and knowledge can be found on countless online sources.  

**Installation**   
You might need to install a few packages with the commands listed below, run these in your command prompt(windows) or terminal(mac os)
pip install imutils
pip install opencv
