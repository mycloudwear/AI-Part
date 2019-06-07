import csv
import random
import account


def get_color_labels(address_list):
    # 创建一个list
    color_list = []
    # 打开results文件
    input_file_0 = open(
        './results/' + account.get_signal() + '/prediction_length_results_classification/prediction_length_coat.csv',
        'r')
    file_to_read_0 = list(csv.reader(input_file_0))
    input_file_0.close()

    input_file_1 = open(
        './results/' + account.get_signal() + '/prediction_length_results_classification/prediction_length_pant.csv',
        'r')
    file_to_read_1 = list(csv.reader(input_file_1))
    input_file_1.close()

    input_file_2 = open(
        './results/' + account.get_signal() + '/prediction_length_results_classification/prediction_length_skirt.csv',
        'r')
    file_to_read_2 = list(csv.reader(input_file_2))
    input_file_2.close()

    for sublist in address_list:
        top_color = ''
        down_color = ''
        for eachline in file_to_read_0:
            if sublist[0] == eachline[0]:
                top_color = eachline[2]
                break
        if (sublist[1].split('/')[3]) == 'pant_length_labels':
            for eachline in file_to_read_1:
                if sublist[1] == eachline[0]:
                    down_color = eachline[2]
                    break
        if (sublist[1].split('/')[3]) == 'skirt_length_labels':
            for eachline in file_to_read_2:
                if sublist[1] == eachline[0]:
                    down_color = eachline[2]
                    break
        sub_color_list = [top_color, down_color]
        color_list.append(sub_color_list)

    return color_list


def color_matching(dirlist, bmi):
    if len(dirlist) <= 3:
        return dirlist

    colorlist = get_color_labels(dirlist)
    print(colorlist)
    commend_dirlist = []  # 推荐
    temp_dirlist = []  # 不推荐；但当最终结果不足3个时，进行补充
    blacklist_dirlist = []  # 黑名单；但当最终结果不足3个时，进行补充

    while len(commend_dirlist) < 3 and len(colorlist) != 0:
        temp = colorlist.pop(0)
        top_color = temp[0]  # 上衣颜色
        buttom_color = temp[1]  # 下衣颜色

        # bmi 内容没有写完！！！！！！！
        # 先留着吧
        # if bmi >= 3:  # 如果很胖的话，就不推荐穿白衣服
        #     if ("white" in temp):
        #         # 但是保留该选项，如果总推荐不够，还是要放上去
        #         temp_dirlist.append(dirlist.pop(0))
        #         # print('fat 还没写完')
        #         continue

        # 下衣：white
        if buttom_color in color_dic[0]:
            if top_color == 'white':  # 上衣：white拉黑
                blacklist_dirlist.append(dirlist.pop(0))
            else:  # 上衣：其余不推荐
                temp_dirlist.append(dirlist.pop(0))
        # 下衣：yell_d,gre_s,cyan
        elif buttom_color in color_dic[1]:
            if top_color == 'black' or top_color == 'gray' or top_color == 'white':  # 上衣：black,gray,white推荐
                commend_dirlist.append(dirlist.pop(0))
            else:  # 上衣：其余拉黑
                blacklist_dirlist.append(dirlist.pop(0))
        # 下衣：red_s,oran_s,yell_s
        elif buttom_color in color_dic[2]:
            if top_color == 'black' or top_color == 'gray' or top_color == 'white' or top_color == 'yellow_s' or top_color == 'yellow_d':  # 上衣：black，gray，white，yell推荐
                commend_dirlist.append(dirlist.pop(0))
            else:  # 上衣：其余拉黑
                blacklist_dirlist.append(dirlist.pop(0))
        # 下衣：red_d,oran_d
        elif buttom_color in color_dic[3]:
            if top_color == 'black' or top_color == 'white' or top_color == 'yellow_s' or top_color == 'yellow_d' or top_color == 'blue_s' or top_color == 'blue_d':  # 上衣：black,white,yell,blue推荐
                commend_dirlist.append(dirlist.pop(0))
            elif top_color == 'gray' or top_color == 'purple_s' or top_color == 'purple_d':  # 上衣：gary,purple不推荐
                temp_dirlist.append(dirlist.pop(0))
            else:  # 上衣：red,orange,green,cyan拉黑
                blacklist_dirlist.append(dirlist.pop(0))
        # 下衣：purple
        elif buttom_color in color_dic[4]:
            if top_color == 'purple_s' or top_color == 'purple_d':  # 下衣：purple不推荐
                temp_dirlist.append(dirlist.pop(0))
            else:  # 其余：推荐
                commend_dirlist.append(dirlist.pop(0))
        # top_color in color_dic[5]
        #  下衣：black,gray,blu_s,blu_d
        else:
            # 上衣：都推荐
            commend_dirlist.append(dirlist.pop(0))

    if len(commend_dirlist) >= 3:
        final_dirlist = []
        # [0,len(commend_dirlist)]间随机生成3个数，返回列表
        index_list = random.sample(range(0, len(commend_dirlist)), 3)
        for index in index_list:
            final_dirlist.append(commend_dirlist[index])
    else:
        if len(temp_dirlist) >= (3 - len(commend_dirlist)):
            final_dirlist = commend_dirlist
            # [0,len(temp_dirlist)]间随机生成(3-len(final_dirlist))个数，返回列表
            index_list = random.sample(range(0, len(temp_dirlist)), 3 - len(final_dirlist))
            for index in index_list:
                final_dirlist.append(temp_dirlist[index])
        else:
            final_dirlist = commend_dirlist + temp_dirlist
            # [0,len(blacklist_dirlist)]间随机生成(3-len(final_dirlist))个数，返回列表
            index_list = random.sample(range(0, len(blacklist_dirlist)), 3 - len(final_dirlist))
            for index in index_list:
                final_dirlist.append(blacklist_dirlist[index])

    return final_dirlist


# 一定要留着
color_dic = [['white'],
             ['yellow_d', 'green_s', 'cyan_s', 'cyan_d'],
             ['red_s', 'orange_s', 'yellow_s'],
             ['red_d', 'orange_d'],
             ['green_d', 'purple_s', 'purple_d'],
             ['black', 'gray', 'blues_s', 'blue_d']
             ]
