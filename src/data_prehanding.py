import urllib.request
import shutil
import csv
import account

# Get data from these three URL every time
import check_duplication

urlTops = 'http://192.168.0.67:8080/WebPicStream/'
urlPants = 'http://192.168.0.67:8080/WebPicStream/'
urlSkirts = 'http://192.168.0.67:8080/WebPicStream/'


# # Write data into question.csv
# def write_question_csv(filename, filetype):
#     question = open('datasets/final-rank/Tests/question.csv', 'a', newline='')
#     question_to_write = csv.writer(question, dialect='excel')
#     question_to_write.writerow([filename, filetype, '?'])
#     print(filename + '-----------------write over')
#     question.close()


def write_recorder(add_all, path, mod):
    with open(path, mod, newline='') as csvFile:
        writer = csv.writer(csvFile, dialect='excel')
        for row in add_all:
            writer.writerow([row])


def write_question(front, add_all, clothingType, path, mod):
    with open(path, mod, newline='') as csvFile:
        writer = csv.writer(csvFile, dialect='excel')
        for item in add_all:
            writer.writerow([front + item, clothingType, '?'])


# Download images from URL to local and copy them to the appropriate folder
def prehanding():
    # Address for downloading images to save
    sourDir = 'datasets/final-rank/' + account.get_signal() + '/download/'
    destDirCoat = ['datasets/final-rank/' + account.get_signal() + '/coat_length_labels/',
                   'datasets/final-rank/' + account.get_signal() + '/sleeve_length_labels/',
                   'datasets/final-rank/' + account.get_signal() + '/collar_design_labels/',
                   'datasets/final-rank/' + account.get_signal() + '/lapel_design_labels/',
                   'datasets/final-rank/' + account.get_signal() + '/neck_design_labels/',
                   'datasets/final-rank/' + account.get_signal() + '/neckline_design_labels/']
    destDirPant = 'datasets/final-rank/' + account.get_signal() + '/pant_length_labels/'
    destDirSkirt = 'datasets/final-rank/' + account.get_signal() + '/skirt_length_labels/'

    responseTops = urllib.request.urlopen(urlTops + 'GetTopTXT?phone=' + account.get_encode_signal())
    responsePants = urllib.request.urlopen(urlPants + 'GetPantTXT?phone=' + account.get_encode_signal())
    responseSkirts = urllib.request.urlopen(urlSkirts + 'GetSkirtTXT?phone=' + account.get_encode_signal())

    print(account.get_encode_signal())
    print(account.get_signal())

    topsfilename = (responseTops.read().decode()).split('\r\n')[:-1]
    pantsfilename = (responsePants.read().decode()).split('\r\n')[:-1]
    skirtsfilename = (responseSkirts.read().decode()).split('\r\n')[:-1]

    print('TopsFilename: {0} {1}'.format(len(topsfilename), topsfilename))
    print('PantsFilename: {0} {1}'.format(len(pantsfilename), pantsfilename))
    print('SkirtsFilename: {0} {1}'.format(len(skirtsfilename), skirtsfilename))

    add_tops, add_pants, add_skirts, delete_tops, delete_pants, delete_skirts = check_duplication.check(topsfilename,
                                                                                                        pantsfilename,
                                                                                                        skirtsfilename)

    print('TopsAdd: {0} {1}'.format(len(add_tops), add_tops))
    print('PantsAdd: {0} {1}'.format(len(add_pants), add_pants))
    print('SkirtsAdd: {0} {1}'.format(len(add_skirts), add_skirts))
    print('TopsDelete: {0} {1}'.format(len(delete_tops), delete_tops))
    print('PantsDelete: {0} {1}'.format(len(delete_pants), delete_pants))
    print('SkirtsDelete: {0} {1}'.format(len(delete_skirts), delete_skirts))

    # delete
    delete_all = delete_tops + delete_pants + delete_skirts
    if not delete_all:
        print('no image needs to delete')
    else:
        # delete items in recorder
        check_duplication.delete_item('datasets/final-rank/' + account.get_signal() + '/download/recorder.csv',
                                      delete_all)
        # delete items in 3 csv
        check_duplication.delete_item(
            'results/' + account.get_signal() + '/prediction_length_results_classification/prediction_length_coat.csv',
            delete_all)

        check_duplication.delete_item(
            'results/' + account.get_signal() + '/prediction_length_results_classification/prediction_length_pant.csv',
            delete_all)

        check_duplication.delete_item(
            'results/' + account.get_signal() + '/prediction_length_results_classification/prediction_length_skirt.csv',
            delete_all)

        # delete images in download
        for each_to_delete in delete_all:
            check_duplication.delete_image(
                'datasets/final-rank/' + account.get_signal() + '/download/' + each_to_delete)
            for each_dir in destDirCoat + destDirPant + destDirSkirt:
                check_duplication.delete_image(each_dir + each_to_delete)

    # 写入新增的、需要预测的内容
    add_all = add_tops + add_pants + add_skirts
    if not add_all:
        print('all images has been downloaded')
    else:

        write_recorder(add_all, 'datasets/final-rank/' + account.get_signal() + '/download/recorder.csv', 'a')

        for eachDir in destDirCoat:
            write_question(eachDir[20:], add_tops, eachDir[35:-1], 'datasets/final-rank/Tests/question.csv', 'a')
        write_question(destDirPant[20:], add_pants, destDirPant[35:-1], 'datasets/final-rank/Tests/question.csv', 'a')
        write_question(destDirSkirt[20:], add_skirts, destDirSkirt[35:-1], 'datasets/final-rank/Tests/question.csv',
                       'a')

        if add_tops:
            for item in add_tops:
                item_url = urlTops + 'GetTopPhoto?phone=' + account.get_encode_signal() + '&path=' + item
                response = urllib.request.urlopen(item_url)
                pic = response.read()

                with open(sourDir + item, 'wb') as f:
                    f.write(pic)
                    for eachDir in destDirCoat:
                        shutil.copyfile(sourDir + item, eachDir + item)
                        # write_question_csv(eachDir[20:] + item, eachDir[40:-1])

        if add_pants:
            for item in add_pants:
                item_url = urlTops + 'GetPantPhoto?phone=' + account.get_encode_signal() + '&path=' + item
                response = urllib.request.urlopen(item_url)
                pic = response.read()

                with open(sourDir + item, 'wb') as f:
                    f.write(pic)
                    shutil.copyfile(sourDir + item, destDirPant + item)
                    # write_question_csv(destDirPant[20:] + item, destDirPant[40:-1])

        if add_skirts:
            for item in add_skirts:
                item_url = urlTops + 'GetSkirtPhoto?phone=' + account.get_encode_signal() + '&path=' + item
                response = urllib.request.urlopen(item_url)
                pic = response.read()

                with open(sourDir + item, 'wb') as f:
                    f.write(pic)
                    shutil.copyfile(sourDir + item, destDirSkirt + item)
                    # write_question_csv(destDirSkirt[20:] + item, destDirSkirt[40:-1])
