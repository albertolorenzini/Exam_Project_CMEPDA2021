# SSD-Tensorflow setup instructions

First of all you need to clone the SSD-Tensorflow repository on your local computer using git command:
`git clone https://github.com/balancap/SSD-Tensorflow.git`

The first requirement is CUDA, you can find all instruction to install it [here](https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html).
SSD-tensorflow was written using "contrib" command in several files, a deprecated library of tensorflow, so in order to use it, you need to setup tensorflow versions 1.x in your virtual environment, personally, I use Anaconda for the environments, so here there are SSD-Tensorflow requirements instructions using conda env.
Once you have installed Anaconda, create your virtual env with `conda create --name SSD-Tensorflow python=3.6` and activate it with `conda activate SSD-Tensorflow`, then install tensorflow 1.x into your virtual environment with `conda install -c conda-forge tensorflow`. Check the version with `python -c 'import tensorflow as tf; print(tf.__version__)'`, if in the last line terminal will display `1.14.0` it is working correctly.
Then you need to install pytorch, to do it you can use the command `conda install pytorch torchvision torchaudio cudatoolkit=10.2 -c pytorch` (check your cuda version to be sure this is the right command, more information [here](https://pytorch.org/get-started/locally/)).
Then you need to unzip the pretrained weight already present in the repository "ssd_300_vgg.ckpt", you can find it inside the checkpoints folder.
Next step is to remove "dataset_factory.py" and "dataset_utils.py" inside datasets folder, these files do not work with a dataset prepared following the master readme.md instructions. Than you have to copy the following files and paste it inside datasets folders, you can find these files in the "SSD-Tenasorflow_utilities" folder:
* kitti.py
* kitti_common.py
* dataset_factory.py
* dataset_utils.py

If you already have prepared your dataset, you can start your training using this command:
```
DATASET_DIR=./data/kitti_cones/tfrecord
TRAIN_DIR=./log/
CHECKPOINT_PATH=./checkpoints/ssd_300_vgg.ckpt
python train_ssd_network.py \
    --train_dir=${TRAIN_DIR} \
    --dataset_dir=${DATASET_DIR} \
    --dataset_name=kitti \
    --dataset_split_name=train \
    --model_name=ssd_300_vgg \
    --checkpoint_path=${CHECKPOINT_PATH} \
    --save_summaries_secs=60 \
    --save_interval_secs=600 \
    --weight_decay=0.0005 \
    --optimizer=adam \
    --learning_rate=0.001 \
    --batch_size=16
```
Obviously, you need to modify the directories with your ones. Alternatively, you can run the script "SSD_train.sh" that you can find in the scripts folder, move it to the SSD-Tensorflow repository if take this way (also in this script you need to modify the directories).
If out of memory error occurs, change batch_size with a low number.
If you want to try with a ready to work dataset you can find one [here](https://drive.google.com/file/d/1NrDwpC0XB8-V7by-sB2DEJbnBoBgTpk6/view?usp=sharing), download it and unzip it, to complete the operation to start your train with this dataset, you need to create two new folder inside the repository main folder, named "data" - where you will unzip the downloaded dataset - and "log", in which SSD-Tensorflow will save the trained weight. IF you want to train this dataset you are now ready to use the command above as is it.

You can find a second model at this [link](https://drive.google.com/open?id=0B0qPCUZ-3YwWT1RCLVZNN3RTVEU), that compress your images at 512x512 resolution instead of 300x300, giving a bigger mean average precision.

## Evaluation

Once you trained your model, you can evaluate it using the command below:

```
EVAL_DIR=./log/
DATASET_DIR=./data/kitti_cones/tfrecord
CHECKPOINT_PATH=./checkpoints/ssd_300_vgg.ckpt
python eval_ssd_network.py \
    --eval_dir=${EVAL_DIR} \
    --dataset_dir=${DATASET_DIR} \
    --dataset_name=kitti \
    --dataset_split_name=val \
    --model_name=ssd_300_vgg \
    --checkpoint_path=${CHECKPOINT_PATH} \
    --batch_size=1
```

## Colab Notebook
For a easy use, you can run SSD-Tensorflow with the Colab Notebook present in the "SSD-Tensorflow_utilities" folder. It is prepared with the example dataset, inside it you can find the cells in which you have to change the code, in order to train your own dataset. To run it you need a Google account, than the notebook will save the trained weight in your Google Drive.