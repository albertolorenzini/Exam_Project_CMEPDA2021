'''
merging.py merge different annotations and images dataset in a unique one 

it request COCO-assistant to work, you can install it using pip install coco-assistant or from source: https://github.com/ashnair1/COCO-Assistant

author = Alberto Lorenzini
'''

'''
usage: create a directory and move this file inside the just created directory, then insiede this directory create two folder called 'images' and 'annotations', 
put all your images in the 'images' folder and all your annotations files in the 'annotations' folder
Then run the following command:

    python merging.py
    
'''


import os
from coco_assistant import COCO_Assistant

# Specify image and annotation directories
img_dir = os.path.join(os.getcwd(), 'images')
ann_dir = os.path.join(os.getcwd(), 'annotations')

# Create COCO_Assistant object
cas = COCO_Assistant(img_dir, ann_dir)
cas.merge(merge_images=True)