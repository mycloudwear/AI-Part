import os
import csv

backDir = ['/coat_length_labels', '/sleeve_length_labels',
           '/collar_design_labels', '/lapel_design_labels',
           '/neck_design_labels', '/neckline_design_labels',
           '/pant_length_labels', '/skirt_length_labels',
           '/download']


def get_signal():
    fo = open('datasets/final-rank/Tests/signal.txt', 'r')
    signal = fo.read()
    fo.close()
    return signal[0:14]


def get_encode_signal():
    fo = open('datasets/final-rank/Tests/signal.txt', 'r')
    encode_signal = fo.read()
    fo.close()
    return encode_signal[14:]


def check_acount():
    path1 = 'datasets/final-rank/' + get_signal()
    path2 = 'results/' + get_signal()
    folder1 = os.path.exists(path1)
    folder2 = os.path.exists(path2)
    if not (folder1 and folder2):
        os.makedirs(path1)
        os.makedirs(path2)
        print(path1 + ' create path successfully')
        print(path2 + ' create path successfully')
        return True
    else:
        print(path1 + ' this path has been created')
        print(path2 + ' this path has been created')
        return False


def create_account():
    if check_acount():
        print('====================================================================================================')
        print('create account....')
        for each in backDir:
            os.makedirs('datasets/final-rank/' + get_signal() + each)

        os.makedirs('results/' + get_signal() + '/matching_results')
        os.makedirs('results/' + get_signal() + '/prediction_length_results_classification')


        with open(
                'datasets/final-rank/' + get_signal() + '/download/recorder.csv',
                'w', newline='') as csvfile0:
            recorder_to_write = csv.writer(csvfile0, dialect='excel')
            recorder_to_write.writerow(['ImageName'])

        with open(
                'results/' + get_signal() + '/prediction_length_results_classification/prediction_length_coat.csv',
                'w', newline='') as csvfile1:
            pass
        with open(
                'results/' + get_signal() + '/prediction_length_results_classification/prediction_length_pant.csv',
                'w', newline='') as csvfile2:
            pass
        with open(
                'results/' + get_signal() + '/prediction_length_results_classification/prediction_length_skirt.csv',
                'w', newline='') as csvfile3:
            pass
