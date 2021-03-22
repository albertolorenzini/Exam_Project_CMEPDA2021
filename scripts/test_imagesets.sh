cd /path/to/kitti_cones
mkdir ImageSets
cd ./ImageSets
ls ../testing/image_2/ | grep ".jpg" | sed s/.jpg// > val.txt
