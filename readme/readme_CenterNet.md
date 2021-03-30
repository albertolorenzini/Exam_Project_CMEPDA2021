# CenterNet Setup Instructions

Also for this net I used a conda environment with python 3.6, so create and activate the environment:
`conda create --name CenterNet python=3.6`
`conda activate CenterNet`

The first requirement is CUDA, you can find all instruction to install it [here](https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html).
Then you need to install pytorch, to do it you can use the command `conda install pytorch torchvision torchaudio cudatoolkit=10.2 -c pytorch` (check your cuda version to be sure this is the right command, more information [here](https://pytorch.org/get-started/locally/)).
Last requirement, before repository cloning, is the installation of tensorflow, you can run this command in order to do that (you need pip installed):
`pip install --upgrade pip`
`pip install tensorflow`

CenterNet need COCOAPI to works, so you have to clone its repository and make it:
```
cd path/to/clone/cocoapi
git clone https://github.com/cocodataset/cocoapi.git
cd ./cocoapi/PythonAPI
make
python setup.py install --user
```

You are now ready to download the repository with the command:
```
cd path/to/clone/CenterNet
git clone https://github.com/xingyizhou/CenterNet.git
```

Here you have to remove DCNv2 folder inside CenterNet repository because it doesn't work, you can do it with:
```
cd ./CenterNet/src/lib/models/networks
rm -rf DCNv2
```
and replace it with this DCNv2 source (you can clone it directly in "networks" folder):
`git clone https://github.com/lbin/DCNv2`

Now you are ready to install CenterNet requirements with:
```
cd path/to/clone/CenterNet
pip install -r requirements.txt
```

And finally compile it running this script:
```
cd ./CenterNet/src/lib/models/networks
chmod 755 -R make.sh
./make.sh
```

CenterNet should be installed correctly on you local machine.

Now you have to move in `path/to/clone/CenterNet/CenterNet/src/lib/datasets/dataset` directory and remove `coco.py` file. Then you have to replace it with `coco.py` file present in CenterNet_utilities folder, this file in fact was madified to be suitable with coco cones dataset. If you want to train the net with others datasets, you need to modify the file with the correct num_classes (line 14), data_dir (line 23), annotations names (line 27,28,32,33,36,37), class_names (line 40), valid_ids (line 42).

## Pre-Trained Weights

In this repository we use three different pre-trained weights, dla 2x, resdcn101 and resdcn18, that, looking specs, are fastest weights, you can download them with through these links:
[dla_2x](https://drive.google.com/open?id=1pl_-ael8wERdUREEnaIfqOV_VF2bEVRT)
[resdcn101](https://drive.google.com/open?id=1bTJCbAc1szA9lWU-fvVw52lqR3U2TTry)
[resdcn18](https://drive.google.com/open?id=1b-_sjq1Pe_dVxt5SeFmoadMfiPTPZqpz)

For others weights you can look in CenterNet repository [here](https://github.com/xingyizhou/CenterNet).

After pre-trained weights download is finished, you have to put them in "models" folder.

## Training

You can download this repository dataset, ready to be trained, at this [link](https://drive.google.com/file/d/1f1SJ2H50Y_Nr582i2bilm8o-ORXGwz2l/view?usp=sharing), then you have to unzip it and replace "data" folder inside CenterNet with this "data" folder of the unzipped file. If you want to train another dataset, you can follow the home folder readme instructions to create it.

You should now ready for train CenterNet. In order to do this you have to move in `path/to/clone/CenterNet/CenterNet/src` folder and run this command (for dla 2x pre-trained weights):
```
python main.py ctdet \
  --exp_id coco_dla_2x \
  --batch_size 64 \
  --master_batch 9 \
  --lr 5e-4 \
  --gpus 0 \
  --num_workers 16
```
If `out of memory` error occours, you have to change batch_size with a lower number. If your machine has more than a GPU, you can say to CenterNet to use them changing `--gpus 0` with `--gpus 0,1`, if you have two GPUS for example. 
For others pre-trained weights you have to change exp_id flag, `--exp_id coco_resdcn101 --arch resdcn_101` and `--exp_id coco_resdcn18 --arch resdcn_18` for resdcn101 and resdcn18 respectively. For more pre-trained weights exp_id you can look inside CenterNet repository.

## Evaluation

After training, if you want to give an evaluation of your net, you need to compile external, to do it you have to move inside `path/to/clone/CenterNet/CenterNet/src/lib/external` directory and run the command `make`. Then you can evaluate your net with the following command (for dla 2x):
```
python test.py ctdet \
  --exp_id coco_dla \
  --keep_res \
  --load_model ../exp/ctdet/coco_dla_2x/model_best.pth
```
If you trained resdcn101 weights:
```
python test.py ctdet \
  --exp_id coco_resdcn101 --arch resdcn_101 \
  --keep_res \
  --load_model ../exp/ctdet/coco_redcn101/model_best.pth
```
If you trained resdcn18 weights:
```
python test.py ctdet \
  --exp_id coco_resdcn18 --arch resdcn_18 \
  --keep_res \
  --load_model ../exp/ctdet/coco_redcn18/model_best.pth
```
For others pre-trained weights you can look for the exp_id inside CenterNet repository.

## Colab Notebook
For a easy use, you can run CenterNet with the Colab Notebook present in the "SSD-Tensorflow_utilities" folder. It is prepared with the example dataset, inside it you can find the cells in which you have to change the code, in order to train your own dataset. To run it you need a Google account, than the notebook will save the trained weight in your Google Drive.
