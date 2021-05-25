# Exam_Project_CMEPDA2021
## Performance comparison between three different available neural nets.

This repository tests the performance of three neural nets for object detection, in particular we use:

1. darknet-YOLO from AlexeyAB: https://github.com/AlexeyAB/darknet
2. CenterNet from xingyizhou: https://github.com/xingyizhou/CenterNet
3. SSD-Tensorflow from balancap: https://github.com/balancap/SSD-Tensorflow

For each net we trained different pre-trained weight, in order to have a better comparison. Each net has different precision and speed (as one can see following the repositories links above), in particular last characteristic (speed), is very importan for us, because the best net will work on a driverless race car.

These three repositories are not up-to-date, and their readme files often are not precise, so we created a "readme" folder in which there are all correct instructions to prepare these three nets. Furthermore, in readme folder, you can find another readme with the instructions to prepare your own datasets, that can be train on each net.

In order to be able to run all these nets on your local machine, there is a folder for each net, in which you can find all you need to run the repository dataset. Moreover, inside each file is explained (through comments) how to modify it for your own dataset. Some of these modifications are explained in the repositories linked above, but often these explanations are quite useless if not totally wrong.

Inside "utilities" folder, you can find some usefull files that can help you to prepare your own dataset (it is all explained inside readme_dataset.md) to be used by nets to train their pretrained weights.

Inside the "scripts" folder, there are files that can be used as a solution for some problems that I encountered during this work.

## Results

