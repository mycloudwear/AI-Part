import csv
import os
import color_detect
import account


# Prediction results processing
def prediction_length_classification():
    # prediction length results
    input_file_0 = open('results/test_length.csv', 'r')
    file_to_read_0 = csv.reader(input_file_0)

    # prediction_length_coat_temp.csv
    output_file_coat = open(
        'results/' + account.get_signal() + '/prediction_length_results_classification/prediction_length_coat_temp.csv',
        'a',
        newline='')
    file_to_write_coat = csv.writer(output_file_coat, dialect='excel')

    # prediction_length_sleeve_temp.csv
    output_file_sleeve = open(
        'results/' + account.get_signal() + '/prediction_length_results_classification/prediction_length_sleeve_temp.csv',
        'a',
        newline='')
    file_to_write_sleeve = csv.writer(output_file_sleeve, dialect='excel')

    #  prediction_length_pant.csv
    output_file_pant = open(
        'results/' + account.get_signal() + '/prediction_length_results_classification/prediction_length_pant.csv', 'a',
        newline='')
    file_to_write_pant = csv.writer(output_file_pant, dialect='excel')

    # prediction_length_skirt.csv
    output_file_skirt = open(
        'results/' + account.get_signal() + '/prediction_length_results_classification/prediction_length_skirt.csv',
        'a',
        newline='')
    file_to_write_skirt = csv.writer(output_file_skirt, dialect='excel')

    for eachline in file_to_read_0:
        result_length = []
        result_length.append('datasets/final-rank/' + eachline[0])

        result_length.append(eachline[1])

        var = eachline[2].split(';')
        index = var.index(max(var))

        if (eachline[1] == 'coat_length_labels'):
            color = color_detect.return_color_2('datasets/final-rank/' + eachline[0])
            result_length.append(color)

            if (index <= 1):
                result_length.append(1)
            elif (index <= 3 and index > 1):
                result_length.append(2)
            elif (index <= 5 and index > 3):
                result_length.append(3)
            elif (index <= 7 and index > 5):
                result_length.append(4)

            file_to_write_coat.writerow(result_length)

        elif (eachline[1] == 'sleeve_length_labels'):
            result_length.append('')

            if (index == 0):
                result_length.append(0)
            elif (index <= 2 and index > 0):
                result_length.append(1)
            elif (index <= 4 and index > 2):
                result_length.append(2)
            elif (index <= 6 and index > 4):
                result_length.append(3)
            elif (index <= 8 and index > 6):
                result_length.append(4)

            file_to_write_sleeve.writerow(result_length)

        elif (eachline[1] == 'pant_length_labels'):
            color = color_detect.return_color_2('datasets/final-rank/' + eachline[0])
            result_length.append(color)

            if (index <= 1):
                result_length.append(1)
            elif (index <= 3 and index > 1):
                result_length.append(2)
            elif (index <= 5 and index > 3):
                result_length.append(3)

            file_to_write_pant.writerow(result_length)

        elif (eachline[1] == 'skirt_length_labels'):
            color = color_detect.return_color_2('datasets/final-rank/' + eachline[0])
            result_length.append(color)

            if (index <= 1):
                result_length.append(1)
            elif (index <= 3 and index > 1):
                result_length.append(2)
            elif (index <= 5 and index > 3):
                result_length.append(3)

            file_to_write_skirt.writerow(result_length)

    input_file_0.close()
    output_file_coat.close()
    output_file_sleeve.close()
    output_file_pant.close()
    output_file_skirt.close()

    input_file_coat_temp = open(
        'results/' + account.get_signal() + '/prediction_length_results_classification/prediction_length_coat_temp.csv',
        'r')
    file_to_read_coat_temp = csv.reader(input_file_coat_temp)

    input_file_sleeve_temp = open(
        'results/' + account.get_signal() + '/prediction_length_results_classification/prediction_length_sleeve_temp.csv',
        'r')
    file_to_read_sleeve_temp = csv.reader(input_file_sleeve_temp)

    output_file_coat = open(
        'results/' + account.get_signal() + '/prediction_length_results_classification/prediction_length_coat.csv', 'a',
        newline='')
    file_to_write_coat = csv.writer(output_file_coat, dialect='excel')

    rows_coat = [row for row in file_to_read_coat_temp]
    rows_sleeve = [row for row in file_to_read_sleeve_temp]

    for i in range(len(rows_coat)):
        file_to_write_coat.writerow(
            [rows_coat[i][0], 'coat_length_labels', rows_coat[i][2],
             (int(rows_coat[i][3]) + int(rows_sleeve[i][3])) / 2])

    input_file_sleeve_temp.close()
    input_file_coat_temp.close()
    output_file_coat.close()
    os.remove(
        'results/' + account.get_signal() + '/prediction_length_results_classification/prediction_length_coat_temp.csv')
    os.remove(
        'results/' + account.get_signal() + '/prediction_length_results_classification/prediction_length_sleeve_temp.csv')
