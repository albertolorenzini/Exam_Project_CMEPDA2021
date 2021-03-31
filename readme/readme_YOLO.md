# Darknet-YOLO Setup Instructions

Also for this net I used a conda environment with python 3.6, so create and activate the environment:
`conda create --name darknet python=3.6`
`conda activate darknet`

The first requirement is CUDA, you can find all instructions to install it [here](https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html).
Secondly you need OpenCV, you can find all instructions to install it (for linux) at this [link](https://docs.opencv.org/master/d7/d9f/tutorial_linux_install.html).
Then, if you want to train your net faster, you can proceed with CUDNN installation, following these [instructions](https://docs.nvidia.com/deeplearning/cudnn/install-guide/index.html#installlinux-tar).
Now you need to clone darknet repository using: `git clone https://github.com/AlexeyAB/darknet.git`.
My advice is to compile it using make, to do it you have to modify `Makefile` inside darknet directory, in this way:
```
OPENCV=1
GPU=1
CUDNN=1
CUDNN_HALF=1
```
Then you can compile it using `make` command (your shell need to be inside darknet directory).

## Training
Now, in order to train your net, you need to download pre-trained weights, for yolov4 you can download them from this [link](https://github.com/AlexeyAB/darknet/releases/download/darknet_yolo_v3_optimal/yolov4.conv.137). Others weights can be downloaded via this [link](https://github.com/AlexeyAB/darknet/releases/download/darknet_yolo_v3_optimal/yolov4.weights). You have to move these files inside darknet folder.

Now you have to prepare your config file, for this repository dataset a config file is ready inside "darknet_utilities" folder, its name is `yolo-obj.cfg` (this file works only with `yolov4.conv.137` weights). For the same dataset, in the same folder you can find also config file for "tiny-yolo" weights and `yolov4.weights`. You need to move them inside `path/to/clone/darknet/darknet/cfg` directory.

For your own dataset you should create bounded box .txt files for each image in your dataset, you can create them following these [instructions](https://github.com/AlexeyAB/Yolo_mark). For our dataset all of these files are ready, you can download them at this [link](https://drive.google.com/file/d/1owi0N7P71JKmvCkWekrEgjKFi-q5GM9m/view?usp=sharing), in which there are also all images dataset. My advice is to create a new folder called `obj` inside `path/to/clone/darknet/darknet/data` directory and unzip the dataset file directly inside it.

Next step is to prepare object data and names files, for this repository dataset you can find them as `obj.data` and `obj.names` inside "darknet_utilities" folder. If you want to prepare these files for your own data, you can modify them. Inside `obj.names` you have to replace lines, with the names of your classes dataset, one each line, inside `obj.data` you only have to replace classes number with your classes number. Then these two files have to be moved inside `path/to/clone/darknet/darknet/data` directory.

Lastly you need to create two files `train.txt` and `test.txt` in which you have to write the directories of images, ones by ones, one image each line, for training and testing images respectively. For this repository dataset, you can find the prepared files inside "darknet_utilities", you only have to replace `/home/...` with the directory path to your darknet repository. Then move these files inside `path/to/clone/darknet/darknet/data` directory.

you should now ready to train your net, in order to do it you can use the command below (for `yolov4.conv.137` weights):
`./darknet detector train ./data/obj.data ./cfg/yolo-obj.cfg ./yolov4.conv.137 -map`
if error `Out of memory` occurs then in `.cfg-file` you should increase `subdivisions=16` in 32 or 64.
You can stop and restart your train changing the weights directory. For example after 4000 iterations, you can restart your train using the command below:
`./darknet detector train ./data/obj.data ./cfg/yolo-obj.cfg ./backup/yolo-obj_4000.weights -map`

## Colab Notebook
For a easy use, you can run darknet-YOLO with the Colab Notebook present in the "darknet_utilities" folder. It is prepared with the example dataset, inside it you can find the cells in which you have to change the code to train your own dataset. To run it you need a Google account, than the notebook will save the trained weight in your Google Drive.

