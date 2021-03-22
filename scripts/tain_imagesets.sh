cd /path/to/kitti_cones
mkdir ImageSets
cd ./ImageSets
ls ../training/image_2/ | grep ".jpg" | sed s/.jpg// > train.txt
