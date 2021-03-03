# Exam_Project_CMEPDA2021
## Performance comparison between three different available neural nets.

This repository tests the performance of three nural nets for object detection, in particular we use:

1. darknet-YOLO from AlexeyAB: https://github.com/AlexeyAB/darknet
2. CenterNet from xingyizhou: https://github.com/xingyizhou/CenterNet
3. SSD-Tensorflow from balancap: https://github.com/balancap/SSD-Tensorflow

For each net we trained different pre-trained weight, in order to have a better comparison. Each net has different precision and speed (as one can see following the repositories links above), in particular last characteristic (speed), is very importan for us, because the best net will work on a driverless race car.

These three repositories are not up-to-date, and their readme files often are not precise, so we created a readme folder in which there are all correct instructions to prepare these three nets.

## Dataset

In this repository we use street cones images dataset for the training, in fact our purpose is to find what is the object detection best solution for E-Team Squadra Corse driverless car, the car of the University of Pisa Formula Student team. In Formula Student competition the circuits are created using yellow, blue and orange street cones.
We use different dataset format for each net:

1. darknet format for YOLO.
2. COCO format for CenterNet.
3. tfrecord for SSD-Tensorflow.

This because not all nets can recognize all formats and also because, as written in the repositories, those are the best format for each net.
It is important that you follow the next order, otherwise is not possible to convert data.

### Darknet-YOLO

We start with format for YOLO. In Formula Student, all driverless teams prepare six hundreds laballed images, in order to have all dataset access, which includes thousands of labelled street cones images. Darknet requests a .txt file in which you have to insert all trining images directories, and another one in wich there are all testing images directories. You can find them in DarknetUtilities folder as "train.txt" and "test.txt". All dataset .zip file can be download from this [link](https://drive.google.com/file/d/1owi0N7P71JKmvCkWekrEgjKFi-q5GM9m/view?usp=sharing).

### COCO-CenterNet

In order to be sure that nets will use the same images as training, testing and validating, we create a python file that divide dataset, starting from "train.txt" and "test.txt", for validating folder we takes nine hundreds directories images from train.txt file. The file names "movingmoving.py" and it is available inside Utilities folder, do not move it in another directory, otherwise you will have to change train.txt and test.txt paths inside movingmoving.py file.

To convert darknet format dataset to COCO dataset, we used [Roboflow](https://roboflow.com/), a nice site in which you can upload your dataset and than convert and download it in your preferred format. Unfortunately with free version you cannot convert more than one thousand images. To beat capitalism, we create nice file called "merging.py" that, with the help of COCO-Assistant repository, will merge your annotations files and images. To use it follow the next instructions:
*   * Download COCO-Assistant repository, in order to do that use the command `git clone https://github.com/ashnair1/COCO-Assistant.git`.
    * Inside COCO-Assistant repository, build and install the library with `make`.
    * Move all your annotations.json files in a folder called "annotations".
    * Move all your images folders in another folder called "images".
    * Move merging.py in current directory.
        Your data directory should look as follows:

        ```
        Example:
        .
        |---merging.py
        |
        |---annotations
        |   |---annotations1.json
        |   |---annotations2.json
        |   |---annotations3.json
        |
        |---images
        |   |---images1
        |   |---images2
        |   |---images3
        ```
    * Run merging.py file using the command `python merging.py`.

    The merged dataset can be found in `./results/combination`.
At the end of this preparation, in order to have your dataset usefull for CenterNet, you have to move all your combination results in a new folder, that has to be moved inside `data` folder inside CenterNet repository. 
You should have a data directory that look as follows:
```
Example:

./CenterNet
  |---.gitignore
  |---Data
  |   |---coco_cones
  |   |   |---annotations
  |   |   |   |---annotations_test.json
  |   |   |   |---annotations_train.json
  |   |   |   |---annotations_val.json
  |   |   |
  |   |   |---images
  |   |   |   |---test
  |   |   |   |---train
  |   |   |   |---val
```
Your COCO dataset should be ready.

### tfrecord-SSD-Tensorflow




