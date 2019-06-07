import os

# 2 gpus
os.environ['CUDA_VISIBLE_DEVICES'] = '0,4'

# path to train and test labels
TRAIN_LABEL_DIR = 'datasets/train/Annotations/label.csv'
TEST_LABEL_DIR = 'datasets/final-rank/Tests/question.csv'

TRAIN_LENGTH_LABEL_DIR = 'labels/length.csv'
TRAIN_DESIGN_LABEL_DIR = 'labels/design.csv'
TEST_DESIGN_LABEL_DIR = 'labels/test_design.csv'
TEST_LENGTH_LABEL_DIR = 'labels/test_length.csv'

# path to train and test images
TRAIN_IMG_DIR = 'datasets/train/'
TEST_IMG_DIR = 'datasets/final-rank/'

# path to trianed models
MODEL_LENGTH_INCEPTIONV4 = 'models/inceptionv4_length.h5'
# MODEL_LENGTH_INCEPTIONRESNETV2 = 'models/length_inceptionresnet_480_12.h5'
MODEL_DESIGN_INCEPTIONV4 = 'models/inceptionv4_design.h5'
# MODEL_DESIGN_INCEPTIONRESNETV2 = 'models/design_inceptionresnet_480_8.h5'


task_list_length = {
    'pant_length': 6,
    'skirt_length': 6,
    'sleeve_length': 9,
    'coat_length': 8
}

task_list_design = {
    'collar_design': 5,
    'lapel_design': 5,
    'neckline_design': 10,
    'neck_design': 5,
}

# input size
width = 480
model_name = 'inceptionv4'
