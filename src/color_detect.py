#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import os

import cv2
import numpy as np
import color_list
from removebg import RemoveBg

filename = 'image/5.png'


# deal with picture files.
'''
 * @author int93
 * @version 1.0.0
 * @since 02/1/2018
 * Published on 02/1/2018.
 * The original code was provided by int93 (https://blog.csdn.net/int93/article/details/78954129) but in our app we
 * only use part of his code to achieve our function.
'''
def get_color(frame):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    maxsum = -100
    color = None
    color_dict = color_list.getColorList()
    for d in color_dict:
        mask = cv2.inRange(hsv, color_dict[d][0], color_dict[d][1])
        # cv2.imwrite(d + '.jpg', mask)
        binary = cv2.threshold(mask, 127, 255, cv2.THRESH_BINARY)[1]
        binary = cv2.dilate(binary, None, iterations=2)
        img, cnts, hiera = cv2.findContours(binary.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        sum = 0
        for c in cnts:
            sum += cv2.contourArea(c)
        if sum > maxsum:
            maxsum = sum
            color = d

    return color


def back_remove(dir):
    rmbg = RemoveBg("JePRjqGGRxy2LzN526zikRxg", "error.log")
    rmbg.remove_background_from_img_file(dir)


def return_color(dir):
    back_remove(dir)
    new_dir = dir + '_no_bg.png'
    frame = cv2.imread(new_dir)
    color = get_color(frame)
    #os.remove(new_dir)
    return color


def return_color_2(dir):
    frame = cv2.imread(dir)
    color = get_color(frame)
    return color
