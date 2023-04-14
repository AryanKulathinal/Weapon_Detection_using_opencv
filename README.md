# Weapon_Detection_using_opencv
This is a Weapon Detection System using OpenCV LIbrary implemented Using Haar Cascade Classfier.

Haar Cascade Classifier :
Haar Cascade training is a machine learning technique used for object detection in images. During the training process, Haar features are extracted from positive and negative images, and a classifier is trained using these features. The output of the training process is a set of XML files that contain the trained classifier.

Datasets of Three types of weapons were collected :
1.Firearms(Guns,rifles,pistol,etc)
2.Sharp Objects(Knives,Swords,Daggers,etc)
3.Explosives(TNT Dynamite,Grenades,etc)

The training was done using Cascade Trainer GUI.The output of the training was an xml file.
**The XML files contain the trained Haar classifier model and the parameters used during training, such as the number of stages, the size of the image patches, the number of positive and negative samples, and the threshold values. The XML files are used during the detection phase to detect objects in new images. The Haar classifier is applied to the image using a sliding window technique, and the XML files are used to determine whether the image patch contains the object of interest.In summary, the XML files generated as a result of Haar Cascade training contain the trained Haar classifier and the parameters used during training, and they are used during the detection phase to detect objects in new images.**

The trained model was integrated into a python program crearted using opencv library.
The videos in mp4 format given as input are also attached here.


A version of the system incorporating a GUI(using tkinter) is also given.
The GUI provide an user friendly interface for first time user.

GUI Integration Credits : [Govind A](https://github.com/GOVINDFROMINDIA)

**Note : This is simply an object detection model demonstrating the tecniques used in computer vision.The accuracy of the system is not desirabl nor suitable  for a real world system.

