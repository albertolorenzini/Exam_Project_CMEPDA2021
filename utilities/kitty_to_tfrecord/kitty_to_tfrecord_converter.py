######################################################################
# This file convert kitti object format to tfrecord for SSD-TensorFlow
#
# Author = Alberto Lorenzini
######################################################################
"""
Usage:
```shell
python tf_convert_data.py \
    --datset_root=path/to/kittyobjectdataset \
    --split=trainval \
    --output_dir=./kitti_tfrecord
```
"""
import tensorflow as tf
import os, sys
import kitti_object_to_tfrecords

FLAGS = tf.app.flags.FLAGS

tf.app.flags.DEFINE_string(
    'dataset_name', 'kitti',
    'The name of the dataset to convert.')
tf.app.flags.DEFINE_string(
    'dataset_root', None,
    'Directory where the original dataset is stored.')
tf.app.flags.DEFINE_string(
    'split', 'trainval',
    'Split of dataset, trainval/train/val/test.')
tf.app.flags.DEFINE_string(
    'output_dir', './',
    'Output directory where to store TFRecords files.')


def main(_):
    print('Dataset root dir:', FLAGS.dataset_root)
    print('Output directory:', FLAGS.output_dir)

    if FLAGS.dataset_name == 'kitti':
        kitti_object_to_tfrecords.run(FLAGS.dataset_root,
                                   FLAGS.split,
                                   FLAGS.output_dir,
                                   shuffling=True)
    else:
        raise ValueError('Dataset [%s] was not recognized.' % FLAGS.dataset_name)


if __name__ == '__main__':
    tf.app.run()

