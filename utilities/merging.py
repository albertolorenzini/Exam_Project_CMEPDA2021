import os
from coco_assistant import COCO_Assistant

# Specify image and annotation directories
img_dir = os.path.join(os.getcwd(), 'images')
ann_dir = os.path.join(os.getcwd(), 'annotations')

# Create COCO_Assistant object
cas = COCO_Assistant(img_dir, ann_dir)
cas.merge(merge_images=True)