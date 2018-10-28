---
title: 学习多粒度显著特征用于跨境追踪技术
date: 2018-10-10 12:37:53
tags: # 行人再识别 
    - 多尺度
    - 行人再识别 
categories: 行人再识别
---

(MGN)Learning Discriminative Features with Multiple Granularity for Person Re-Identification

[视频介绍](http://www.sohu.com/a/238041608_633698) ,[Paper](https://arxiv.org/abs/1804.01438),[code1](https://github.com/seathiefwang/MGN-pytorch),[code2](https://github.com/levyfan/reid-mgn)

Market1501： rank1：95.7，mAP：86.9

利用多粒度实现了对全局和局部信息特征的同时提取。其中全局特征模块中对人的整体特征进行的提取可以更好的关注人的整体结构，对图片进行2分和3分的分割对人的局部信息进行提取。该网络依赖ResNet，ResNet大大提高了准确率（ResNet50本身可以达到 Market1501： rank1：89.13，mAP：73.5）

多粒度的思想能充分提取特征。