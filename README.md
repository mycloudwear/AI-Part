# Table of Contents
* [1 API Usage](#1-api-usage)
* [2 Features](#2-features)
# Python-based AI Computing Server
[![Badge](https://img.shields.io/badge/Website-MyCloudwear-%2322B8DB.svg)](https://mycloudwear.com)
[![LICENSE](https://img.shields.io/badge/License-Anti%20996-%23FF4D5B.svg?style=flat-square)](https://github.com/996icu/996.ICU/blob/master/LICENSE)
[![Removebg](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)](https://www.remove.bg/api)

[![Ubuntu](https://img.shields.io/badge/Ubuntu-18.04-%234000FF.svg)](http://releases.ubuntu.com/18.04/)
[![Python](https://img.shields.io/badge/Python-3.6.7-%237000FF.svg)](https://www.python.org/downloads/release/python-367/)
[![Tensorflow](https://img.shields.io/badge/Tensorflow-1.8.0-%237060FF.svg)](https://www.tensorflow.org/install/source)
[![CUDA](https://img.shields.io/badge/CUDA-9.0.176-%237090FF.svg)](https://developer.nvidia.com/cuda-90-download-archive)
[![cuDNN](https://img.shields.io/badge/cuDNN-7.5.0-%2370B0FF.svg)](https://developer.nvidia.com/cudnn)
[![Opencv](https://img.shields.io/badge/Opencv-3.4.5.20-%2370C0FF.svg)](https://pypi.org/project/opencv-python/3.4.5.20/)
[![imgaug](https://img.shields.io/badge/imgaug-0.2.5-%2370D0FF.svg)](https://pypi.org/project/imgaug/0.2.5/)
[![keras](https://img.shields.io/badge/keras-2.1.6-%2370E0FF.svg)](https://pypi.org/project/Keras/2.1.6/)

[中文](README_CN.md) | English
## 1 API Usage
You need to use the package from `Removebg`.
You can obtain the api key from https://www.remove.bg/api. 
## 2 Features
1. Deal with images uploaded by the user, to predict various attributes including:

* The **length** of the coat, sleeve, pant. 
* The **design** of the collar. 
* The **colour** of the cloth. 

2. Match the clothes by: 

* current weather, temperature, humidity, wind.
* color of clothes.
* BMI and etc.

3. The **dislike** operation will be recorded by the server to help realize individuation.
4. Support the function for the user to `delete` dislike or duplicated clothes in the **Photo Management**.
