import csv
from PIL import Image
import random
import requests
import image_upload
import numpy as np
import cv2 as cv
import os
import uuid
import color_filter
import account

weather_url = 'http://192.168.0.67:8080/WebLogin/WeatherChecker?phone=Kzg2MTg2MTU1OTkyODA'


# Obtain weather data
def getWeatherAttribures(weather_url):
    response = requests.get(weather_url)
    weatherAttributes = response.text.split(",")
    weather = weatherAttributes[0]
    temperature = weatherAttributes[1]
    windScale = weatherAttributes[2]
    humidity = weatherAttributes[3]
    return [weather, temperature, windScale, humidity]


# Weather data analysis - acceptance of Weather Status/Temperature/Humidity/Wind Level
def weather_analysis(t, w):
    # detect temperature
    if (t <= 10):
        weather_value = 8
    elif (t > 10 and t <= 15):
        weather_value = 7
    elif (t > 15 and t <= 20):
        weather_value = 6
    elif (t > 20 and t <= 25):
        weather_value = 5
    elif (t > 25 and t <= 35):
        weather_value = 4
    else:
        weather_value = 3

    # detect wind level
    if (w > 6 and w <= 9):
        weather_value = weather_value + 1
    elif (w > 9):
        weather_value = weather_value + 2

    return weather_value


# Filter results, get a required coat
def get_required_coat(arrvalue):
    try:
        required_coat_list = []
        input_file_all_coat = open(
            'results/' + account.get_signal() + '/prediction_length_results_classification/prediction_length_coat.csv',
            'r')
        file_to_read_all_coat = csv.reader(input_file_all_coat)

        all_coat_rows = [row for row in file_to_read_all_coat]
        for row in all_coat_rows:
            if (float(row[3]) == arrvalue):
                required_coat_list.append(row[0])

        return required_coat_list
    except:
        print('File Warning')
        return []


# Filter results, get a required pant
def get_required_pant(arrvalue):
    try:
        required_pant_list = []
        input_file_all_pant = open(
            'results/' + account.get_signal() + '/prediction_length_results_classification/prediction_length_pant.csv',
            'r')
        file_to_read_all_pant = csv.reader(input_file_all_pant)

        all_pant_rows = [row for row in file_to_read_all_pant]
        for row in all_pant_rows:
            if (float(row[3]) == arrvalue):
                required_pant_list.append(row[0])

        return required_pant_list
    except:
        print('File Warning')
        return []


# Filter results, get a required skirt
def get_required_skirt(arrvalue):
    try:
        required_skirt_list = []
        input_file_all_skirt = open(
            'results/' + account.get_signal() + '/prediction_length_results_classification/prediction_length_skirt.csv',
            'r')
        file_to_read_all_skirt = csv.reader(input_file_all_skirt)

        all_skirt_rows = [row for row in file_to_read_all_skirt]
        for row in all_skirt_rows:
            if (float(row[3]) == arrvalue):
                required_skirt_list.append(row[0])

        return required_skirt_list
    except:
        print('File Warning')
        return []


def PNG_JPG(PngPath):
    img = cv.imread(PngPath, 0)
    w, h = img.shape[::-1]
    infile = PngPath
    outfile = os.path.splitext(infile)[0] + '.jpg'
    img = Image.open(infile)
    img = img.resize((int(w / 2), int(h / 2)), Image.ANTIALIAS)
    try:
        if len(img.split()) == 4:
            # prevent IOError: cannot write mode RGBA as BMP
            r, g, b, a = img.split()
            img = Image.merge('RGB', (r, g, b))
            img.convert('RGB').save(outfile, quality=70)
            os.remove(PngPath)
        else:
            img.convert('RGB').save(outfile, quality=70)
            os.remove(PngPath)
        return outfile
    except Exception as e:
        print('PNG change into JPG ERROR', e)


# image Composition, Parameter - image List
def image_composite(imageList):
    baseimg = Image.open(imageList[0])
    baseimg = baseimg.convert('RGBA')
    sz = baseimg.size
    basemat = np.atleast_2d(baseimg)
    for file in imageList[1:]:
        im = Image.open(file, 'r')
        im = im.convert('RGBA')
        # resize to same width
        sz2 = im.size
        if sz2 != sz:
            im = im.resize((sz[0], round(sz2[0] / sz[0] * sz2[1])), Image.ANTIALIAS)
        mat = np.atleast_2d(im)
        basemat = np.append(basemat, mat, axis=0)
    report_img = Image.fromarray(basemat)
    # report_img.show()
    filename = str(uuid.uuid1())

    report_img.save('results/' + account.get_signal() + '/matching_results/' + filename + '.png')
    PNG_JPG('results/' + account.get_signal() + '/matching_results/' + filename + '.png')
    return filename + '.jpg'


# Matching Algorithm
def matching(matching_up, matching_bottom):
    matching_result = []

    if (len(matching_up) != 0 and len(matching_bottom) != 0):
        matching_result.append(matching_up[random.randint(0, len(matching_up) - 1)])
        matching_result.append(matching_bottom[random.randint(0, len(matching_bottom) - 1)])
        return matching_result
    else:
        return []


def start_matching(username, times):
    try:
        print('start matching...')

        match_results_filename = []

        weather_list = getWeatherAttribures(weather_url)
        if not (weather_list[2]):
            weather_list[2] = 0
        weather_value = weather_analysis(float(weather_list[1]), float(weather_list[2]))
        print(
            'Today Weather: weather = {0[0]}, temperature = {0[1]}, windScale = {0[2]}, humidity = {0[3]}, Weather Value = {1}'.format(
                weather_list, weather_value))

        basic_top_value = int(weather_value / 2)
        basic_bottom_value = weather_value - basic_top_value
        matching_up = []
        matching_bottom = []

        for i in [basic_top_value - 0.5, basic_top_value, basic_top_value + 0.5, basic_top_value + 1]:
            if (get_required_coat(i) != []):
                matching_up = get_required_coat(i)

        for j in [basic_bottom_value - 1, basic_bottom_value - 0.5, basic_bottom_value, basic_bottom_value + 0.5]:
            if (get_required_pant(j) != []):
                matching_bottom = get_required_pant(j)

            if (get_required_skirt(j) != []):
                matching_bottom = matching_bottom + get_required_skirt(j)

        print('Top    Candidate: ', matching_up)
        print('Bottom Candidate: ', matching_bottom)

        matching_results_color_detect = []
        for times in range(times):
            temp = matching(matching_up, matching_bottom)
            #print('matching result {0}: {1}'.format(times, temp))
            matching_results_color_detect.append(temp)

        beforeInColor = [list(t) for t in set(tuple(_) for _ in matching_results_color_detect)]
        print('before: {0} {1}'.format(len(beforeInColor), beforeInColor))
        print('start detecting color matching...')
        final_results = color_filter.color_matching(beforeInColor, 4)
        for k in range(len(final_results)):
            print('composite image {0}: {1}'.format(k, final_results[k]))
            match_results_filename.append(image_composite(final_results[k]))

        print('matching completed')
        print('=======================================================================================================')

        print('start uploading...')
        image_upload.upload_filename(match_results_filename, username)

        for eachpic in match_results_filename:
            image_upload.upload_image('results/' + account.get_signal() + '/matching_results/' + eachpic,
                                      eachpic.split('.')[0], username)

        print('uploading completed')
        print('=======================================================================================================')
    except Exception as e:
        print('=======================================================================================================')
        print('error:', e)
        image_upload.upload_filename(['error_image.jpg'], username)
        image_upload.upload_image('results/error_image.jpg', 'error_image', username)

# start_matching('+8618615599280', 30)
