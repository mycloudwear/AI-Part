# 基于python的AI计算服务器
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

中文 | [English](README.md)
## 1  API 使用
`Removebg` 是一个用于去除图片背景的第三方包，您可以通过访问 https://www.remove.bg/api 获取API key.
## 2  功能介绍
1. 对用户上传的照片执行预测操作，得到该用户衣服的各类属性:

* 衣服的袖长、摆长、裤长
* 领子设计
* 检测衣物的主要颜色

2. 根据以下因素进行匹配：

* 天气，温度，湿度，风力等信息
* 用户现有的衣物进行匹配
* 用户BMI值

3. 记录用户**不喜欢**的操作，实现个性化。
4. 提供删除照片的功能，用户可以**删除**他们不喜欢或上传错误的衣物。
