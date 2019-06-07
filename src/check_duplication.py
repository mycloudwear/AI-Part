import csv
import os
import account


def delete_image(path):
    os.remove(path)


def delete_item(dir, delete_all):
    temp_rows = []
    with open(dir, 'r', encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile)
        for each_to_delete in delete_all:
            for row in reader:
                if (row[0].split('/')[-1] != each_to_delete):
                    temp_rows.append(row)

    with open(dir, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, dialect='excel')
        for row in temp_rows:
            writer.writerow(row)


# 判断filename中新增的内容
def check_add(all_recorder, filename):
    add = []
    for item in filename:
        if item not in all_recorder:
            add.append(item)
    return add


def classify_delete(all_delete, filename):
    delete = []
    for item in all_delete:
        if item in filename:
            delete.append(item)
    return delete


def check(tops_filename, pants_filename, skirts_filename):
    file_all_recorder = open('datasets/final-rank/' + account.get_signal() + '/download/recorder.csv', 'r', newline='')
    recorder_to_read = csv.reader(file_all_recorder)
    all_recorder = [row[0] for row in recorder_to_read][1:]
    file_all_recorder.close()

    file_recorder_tops = open(
        'results/' + account.get_signal() + '/prediction_length_results_classification/prediction_length_coat.csv', 'r',
        newline='')
    recorder_to_read = csv.reader(file_recorder_tops)
    tops_recorder = [row[0].split('/')[-1] for row in recorder_to_read]
    file_recorder_tops.close()

    file_pants_recorder = open(
        'results/' + account.get_signal() + '/prediction_length_results_classification/prediction_length_pant.csv', 'r',
        newline='')
    recorder_to_read = csv.reader(file_pants_recorder)
    pants_recorder = [row[0].split('/')[-1] for row in recorder_to_read]
    file_pants_recorder.close()

    file_skirts_recorder = open(
        'results/' + account.get_signal() + '/prediction_length_results_classification/prediction_length_skirt.csv',
        'r', newline='')
    recorder_to_read = csv.reader(file_skirts_recorder)
    skirts_recorder = [row[0].split('/')[-1] for row in recorder_to_read]
    file_skirts_recorder.close()

    # 新上传的内容
    add_tops = check_add(all_recorder, tops_filename)
    add_pants = check_add(all_recorder, pants_filename)
    add_skirts = check_add(all_recorder, skirts_filename)

    # 找到需要删除的图片名称
    all_delete = []
    all_filename = tops_filename + pants_filename + skirts_filename
    for item in all_recorder:
        if item not in all_filename:
            all_delete.append(item)

    # 分类需要删除的图片
    delete_tops = classify_delete(all_delete, tops_recorder)
    delete_pants = classify_delete(all_delete, pants_recorder)
    delete_skirts = classify_delete(all_delete, skirts_recorder)

    return add_tops, add_pants, add_skirts, delete_tops, delete_pants, delete_skirts
