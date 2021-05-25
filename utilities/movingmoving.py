"""
movingmoving is a program that takes files from a directory written in a file txt, and copies that files in another new directory

author = Alberto Lorenzini
"""




import shutil
import os




############################################################################################################
#it reads the file in which it is write the directory's images for trainig and put the directories in a list
############################################################################################################

with open('/home/albertolorenzini/Documenti/Computing_Method/machine_learning/progetto_esame/dati_coni_backup/train.txt') as trainfile:
    original_path_train = trainfile.readlines()

original_path_train = [x.strip() for x in original_path_train]

#the same as above but for testing
with open('/home/albertolorenzini/Documenti/Computing_Method/machine_learning/progetto_esame/dati_coni_backup/test.txt') as testfile:
    original_path_test = testfile.readlines()

x = 0
original_path_test = [x.strip() for x in original_path_test]




##################################################################################################################
#it reads the file in which it is write the directory's annotations for training and put the directories in a list
##################################################################################################################

with open('/home/albertolorenzini/Documenti/Computing_Method/machine_learning/progetto_esame/dati_coni_backup/train_annotation.txt') as train_annotationfile:
    original_path_train_annotation = train_annotationfile.readlines()

x = 0
original_path_train_annotation = [x.strip() for x in original_path_train_annotation]

#the same as above but for testing
with open('/home/albertolorenzini/Documenti/Computing_Method/machine_learning/progetto_esame/dati_coni_backup/test_annotation.txt') as test_annotationfile:
    original_path_test_annotation = test_annotationfile.readlines()

x = 0
original_path_test_annotation = [x.strip() for x in original_path_test_annotation]




#############################################################################################################################
#
#here you have to change the directories with your own ones and copy them in destination_path_train and destination_path_test
#
#############################################################################################################################

#create new directory for training images and annotations
os.mkdir("/home/albertolorenzini/Documenti/Computing_Method/machine_learning/progetto_esame/train")

#create new directory for testing images and annotations
os.mkdir("/home/albertolorenzini/Documenti/Computing_Method/machine_learning/progetto_esame/test")

destination_path_train = "/home/albertolorenzini/Documenti/Computing_Method/machine_learning/progetto_esame/train"
destination_path_test = "/home/albertolorenzini/Documenti/Computing_Method/machine_learning/progetto_esame/test"




###########################################
#it copies training files in such directory
###########################################

x=0
y=0
for x in original_path_train:
    shutil.copy(original_path_train[y], destination_path_train)
    shutil.copy(original_path_train_annotation[y], destination_path_train)
    y+=1

#it copies testing files in such directory
x=0
y=0
for x in original_path_test:
    shutil.copy(original_path_test[y], destination_path_test)
    shutil.copy(original_path_test_annotation[y], destination_path_test)
    y+=1
