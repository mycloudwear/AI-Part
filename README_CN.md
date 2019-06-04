# 基于python的AI计算服务器
[![Badge](https://img.shields.io/badge/Website-MyCloudwear-%2322B8DB.svg)](https://mycloudwear.com)
[![LICENSE](https://img.shields.io/badge/License-Anti%20996-%23FF4D5B.svg?style=flat-square)](https://github.com/996icu/996.ICU/blob/master/LICENSE_CN)

中文 | [English](README.md)
## 1  环境配置

## 2  功能介绍
1. 服务器首先会对用户上传的照片执行预测操作，得到该用户衣服的各类属性，包括衣服的袖长、摆长、领子设计、裤长等参数，并检测衣物的主要颜色。
2. 然后服务器会根据用户的需求和客户端接收的天气，温度，湿度，风力等信息，再结合用户现有的衣物进行匹配，并将结果返回给客户端。
3. 后端记录用户**不喜欢**的操作，实现个性化。
4. 除此之外，后端提供删除照片的功能，用户可以删除他们不喜欢或上传错误的衣物。
