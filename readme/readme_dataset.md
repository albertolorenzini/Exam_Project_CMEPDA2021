## Dataset

In this repository we use street cones images dataset for the training, in fact our purpose is to find what is the object detection best solution for E-Team Squadra Corse driverless car, the car of the University of Pisa Formula Student team. In Formula Student competition the circuits are created using yellow, blue and orange street cones.
We use different dataset format for each net:

1. darknet format for YOLO.
2. COCO format for CenterNet.
3. tfrecord for SSD-Tensorflow.

This because not all nets can recognize all formats and also because, as written in the repositories, those are the best format for each net.
It is important that you follow the next order, otherwise is not possible to convert data.

### Darknet-YOLO

We start with format for YOLO. In Formula Student, all driverless teams prepare six hundreds laballed images, in order to have all dataset access, which includes thousands of labelled street cones images. Darknet requests a .txt file in which you have to insert all trining images directories, and another one in wich there are all testing images directories. You can find them in darknet_utilities folder as "train.txt" and "test.txt". All dataset .zip file can be download from this [link](https://drive.google.com/file/d/1owi0N7P71JKmvCkWekrEgjKFi-q5GM9m/view?usp=sharing). You can find the instructions to create your bbox files for darknet in this repository (not sure it work correctly): [Yolo_mark](https://github.com/AlexeyAB/Yolo_mark).

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
  |---data
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

### kitti/tfrecords-SSD-Tensorflow

For the SSD-Tensorflow dataset setup you have to start from CenterNet dataset and convert it in kitti format. To do that you can use another scripts inside utilities folder named "coco2kitti.py". coco2kitti.py file is suppose to be moved inside the annotations folder of coco dataset. Inside the file you have to choose what kind of .json file you want convert, at line 52 you can shift between train, test, or val. In our case we need only training labels in kitti format, so in this repository coco2kitti.py file is setted up in train mode as default. Once you created the label folder with the txt files inside using `python coco2kitti.py` command, you have to create a kitti dataset folder like below:
```
Example:

./kitti_cones
  |---training
  |   |---image_2/train_00****.jpg
  |   |---label_2/train_00****.txt
  |---testing
  |   |---image_2/test_00****.jpg
```

Inside the `kitti_cones/training/image_2/` folder you have to copy all of images from `CenterNet/data/coco_cones/images/train/` folder. In the same way you have to copy all of CenterNet val images, inside `kitti_cones/testing/image_2`, pay attention: I wrote it in the correct way, CenterNet val folder images into kitti testing images and not test to testing folders.

At this point you have to create a file .txt in order to do the last step of cenverting. To do that you can use the "train_imagesets.sh" script inside the scripts folder. Open it with your preferred text editor and edit its first line with your current `kitti_cones` directory path. After that you have to redo the same with "val_imagesets.sh" and "trainval_imagesets.sh" scripts and run them. At this point you should have a `kitti_cones` folder like below:

```
Example:

./kitti_cones
  |---training
  |   |---image_2/train_00****.jpg
  |   |---label_2/train_00****.txt
  |---testing
  |   |---image_2/test_00****.jpg
  |---ImageSets
  |   |---train.txt
  |   |---val.txt
  |   |---trainval.txt
```

The last step is convert kitti cones dataset in tfrecord format. In order to do that you need to go with your shell inside utilities folder and run the command below:

```
python ./tf_convert_data.py \
  --dataset_name=kitti \
  --dataset_root=path/to/kitti_cones \
  --split=train \
  --output_dir=path/to/kitti_cones/tfrecord \
```

Remember to create the "tfrecord" folder before you run the command. Than run another time the above command with --split=val and you will have create your dataset for SSD-Tensorflow. To be sure, at this point your `kitti_cones` folder should be like below:

```
Example:

./kitti_cones
  |---training
  |   |---image_2/train_00****.jpg
  |   |---label_2/train_00****.txt
  |---testing
  |   |---image_2/test_00****.jpg
  |---ImageSets
  |   |---train.txt
  |   |---val.txt
  |   |---trainval.txt
  |---tfrecord
  |   |---test_***.tfrecord
  |   |---train_***.tfrecord
```

Now your datasets are ready.