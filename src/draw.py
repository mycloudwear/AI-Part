import csv

import numpy as np
import matplotlib.pyplot as plt
from itertools import cycle
from sklearn import svm, datasets
from sklearn.metrics import roc_curve, auc
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import label_binarize
from sklearn.multiclass import OneVsRestClassifier
from scipy import interp


def roc_draw(category, n):
    answer_file = 'answer_' + category + '.csv'
    test_file = 'test_' + category + '.csv'

    # 读取正确样例标签
    y_true_list = []
    csv_reader = csv.reader(open(answer_file, encoding='utf-8'))
    for row in csv_reader:
        if row[0] != '\ufeff1':
            index = row.index("y")
            y_true_list.append(index)

    # 读取预测结果
    y_score_list = []
    csv_reader = csv.reader(open(test_file, encoding='utf-8'))
    for row in csv_reader:
        if row[0] != '\ufeff1':
            y_score_list.append([float(i) for i in row[:n]])

    # 处理参数
    classes = list(range(0, n))
    y_true = label_binarize(y_true_list, classes=classes)
    n_classes = y_true.shape[1]  # 第一行有几个=计算类别的个数
    y_score = np.array(y_score_list)

    # 计算所有类别的ROC
    pos_label = 2
    fpr = dict()
    tpr = dict()
    roc_auc = dict()
    for i in range(n_classes):
        print(i)
        print(y_true)
        fpr[i], tpr[i], _ = roc_curve(y_true[:, i], y_score[:, i])
        roc_auc[i] = auc(fpr[i], tpr[i])

    # Compute micro-average ROC curve and ROC area（方法二：micro）
    fpr["micro"], tpr["micro"], _ = roc_curve(y_true.ravel(), y_score.ravel())
    roc_auc["micro"] = auc(fpr["micro"], tpr["micro"])

    # Compute macro-average ROC curve and ROC area（方法一：macro）
    # First aggregate all false positive rates
    all_fpr = np.unique(np.concatenate([fpr[i] for i in range(n_classes)]))
    # Then interpolate all ROC curves at this points
    mean_tpr = np.zeros_like(all_fpr)
    for i in range(n_classes):
        mean_tpr += interp(all_fpr, fpr[i], tpr[i])
    # Finally average it and compute AUC
    mean_tpr /= n_classes
    fpr["macro"] = all_fpr
    tpr["macro"] = mean_tpr
    roc_auc["macro"] = auc(fpr["macro"], tpr["macro"])

    # Plot all ROC curves
    lw = 2
    plt.figure()

    # 画所有线
    colors = cycle(['aqua', 'darkorange', 'cornflowerblue', 'yellow', 'magenta'])
    for i, color in zip(range(n_classes), colors):
        plt.plot(fpr[i], tpr[i], color=color, lw=lw,
                 label='ROC curve of class {0} (area = {1:0.2f})'
                       ''.format(i, roc_auc[i]))

    # 画miciro
    plt.plot(fpr["micro"], tpr["micro"],
             label='micro-average ROC curve (area = {0:0.2f})'
                   ''.format(roc_auc["micro"]),
             color='magenta', linestyle=':', linewidth=4)

    # 画macro
    plt.plot(fpr["macro"], tpr["macro"],
             label='macro-average ROC curve (area = {0:0.2f})'
                   ''.format(roc_auc["macro"]),
             color='cornflowerblue', linestyle=':', linewidth=4)
    plt.plot([0, 1], [0, 1], 'k--', lw=lw)
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    title = 'ROC to multi-class of ' + category
    plt.title(title)
    plt.legend(loc="lower right")
    plt.show()
