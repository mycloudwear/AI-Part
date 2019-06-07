'''
 * @author Jeremyczhj
 * @version 1.0.0
 * @since 02/5/2018
 * Published on 02/5/2018.
 * The original code was provided by int93 (https://github.com/Jeremyczhj/FashionAI_Tianchi_2018) but in our app we
 * only use part of his code to achieve our function.
'''
import gc
import pandas as pd
from keras.layers import *
from keras.models import *
import inception_v4
from keras.preprocessing.image import *
from keras.applications.inception_resnet_v2 import preprocess_input
from keras.applications import *
from dataset import *
from config import *

import data_prehanding
import data_handling
import os


def predict(task):
    if (task == 'design'):
        task_list = task_list_design
        model1_path = MODEL_DESIGN_INCEPTIONV4

    else:
        task_list = task_list_length
        model1_path = MODEL_LENGTH_INCEPTIONV4

    label_names = list(task_list.keys())

    # load model 1
    base_model = inception_v4.create_model(weights='imagenet', include_top=False, width=width)
    input_tensor = Input((width, width, 3))
    x = input_tensor
    x = Lambda(preprocess_input, name='preprocessing')(x)
    x = base_model(x)
    x = GlobalAveragePooling2D()(x)
    x = Dropout(0.5)(x)
    x = [Dense(count, activation='softmax', name=name)(x) for name, count in task_list.items()]

    model1 = Model(input_tensor, x)
    model1.load_weights(model1_path, by_name=True)

    y_pred11 = process('default', model1, width, fnames_test, n_test)
    y_pred12 = process('flip', model1, width, fnames_test, n_test)

    del model1, base_model, x, input_tensor

    # ensemble two models
    for i in range(n_test):
        problem_name = df_test.label_name[i].replace('_labels', '')
        problem_index = label_names.index(problem_name)
        probs11 = y_pred11[problem_index][i]
        probs12 = y_pred12[problem_index][i]
        probs1 = probs11 + probs12
        probs = probs1
        df_test.label[i] = ';'.join(np.char.mod('%.8f', probs))

    # write csv files
    fname_csv = 'results/test_%s.csv' % (task)
    df_test.to_csv(fname_csv, index=None, header=None)


def csv_loader():
    df_test = pd.read_csv(TEST_LABEL_DIR, header=None)
    df_test.columns = ['filename', 'label_name', 'label']
    df_test_length = df_test[
        (df_test.label_name == 'skirt_length_labels') | (df_test.label_name == 'sleeve_length_labels')
        | (df_test.label_name == 'coat_length_labels') | (df_test.label_name == 'pant_length_labels')]
    df_test_design = df_test[
        (df_test.label_name == 'collar_design_labels') | (df_test.label_name == 'lapel_design_labels')
        | (df_test.label_name == 'neckline_design_labels') | (df_test.label_name == 'neck_design_labels')]
    df_test_length.to_csv(TEST_LENGTH_LABEL_DIR, index=False, header=None)
    df_test_design.to_csv(TEST_DESIGN_LABEL_DIR, index=False, header=None)


if __name__ == '__main__':
    # Prehand data
    print('=======================================================================================================')
    print('start prehanding')
    data_prehanding.prehanding()
    print('=======================================================================================================')

    if (os.path.exists('datasets/final-rank/Tests/question.csv')):
        print('=======================================================================================================')
        print('prediction start')
        # Began to predict
        csv_loader()

        # df_test = pd.read_csv(TEST_DESIGN_LABEL_DIR, header=None)
        # df_test.columns = ['filename', 'label_name', 'label']
        # fnames_test = df_test.filename
        # n_test = len(df_test)
        # predict('design')
        # del df_test

        df_test = pd.read_csv(TEST_LENGTH_LABEL_DIR, header=None)
        df_test.columns = ['filename', 'label_name', 'label']
        fnames_test = df_test.filename
        n_test = len(df_test)
        predict('length')
        del df_test

        gc.collect()

        os.remove('datasets/final-rank/Tests/question.csv')

        print('prediction completed')
        print('=======================================================================================================')

        # Prediction results processing
        print('start handing prediction results...')
        data_handling.prediction_length_classification()

        print('handing prediction results completed')
        print('=======================================================================================================')
