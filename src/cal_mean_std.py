'''
 * @author Jeremyczhj
 * @version 1.0.0
 * @since 02/5/2018
 * Published on 02/5/2018.
 * The original code was provided by int93 (https://github.com/Jeremyczhj/FashionAI_Tianchi_2018) but in our app we
 * only use part of his code to achieve our function.
'''
from PIL import Image
import numpy as np
from config import *


def get_files(dir):
    import os
    if not os.path.exists(dir):
        return []
    if os.path.isfile(dir):
        return [dir]
    result = []
    for subdir in os.listdir(dir):
        sub_path = os.path.join(dir, subdir)
        result += get_files(sub_path)
    return result


r = 0  # r mean
g = 0  # g mean
b = 0  # b mean

r_2 = 0  # r^2
g_2 = 0  # g^2
b_2 = 0  # b^2

total = 0

files = get_files(IMG_DIR)
count = len(files)

for i, image_file in enumerate(files):
    print('Process: %d/%d' % (i, count))
    img = Image.open(image_file)
    # img = img.resize((299, 299))
    img = np.asarray(img)
    img = img.astype('float32') / 255.
    total += img.shape[0] * img.shape[1]

    r += img[:, :, 0].sum()
    g += img[:, :, 1].sum()
    b += img[:, :, 2].sum()

    r_2 += (img[:, :, 0] ** 2).sum()
    g_2 += (img[:, :, 1] ** 2).sum()
    b_2 += (img[:, :, 2] ** 2).sum()

r_mean = r / total
g_mean = g / total
b_mean = b / total

r_var = r_2 / total - r_mean ** 2
g_var = g_2 / total - g_mean ** 2
b_var = b_2 / total - b_mean ** 2

print('Mean is %s' % ([r_mean, g_mean, b_mean]))
print('Var is %s' % ([r_var, g_var, b_var]))
