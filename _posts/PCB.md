---
title: 基于局部和精细化分割的行人重识别
date: 2018-10-15 18:37:53
tags: # 行人再识别 
    - 多尺度
    - soft-attention
    - 行人再识别 
categories: 行人再识别
---

(PCB+RPP)Beyond Part Models: Person Retrieval with Refined Part Pooling (and a Strong Convolutional Baseline)

[Paper](https://arxiv.org/abs/1711.09349v3),[code1](https://github.com/GenkunAbe/reID-PCB),[code2](https://github.com/syfafterzy/PCB_RPP_for_reID)

Market1501： rank1：93.8，mAP：81.6

PCB（Part-based Convolutional  Baseline）：基于局部信息能够获得细粒度特征，对人体的水平分割比较符合人体分布，在一定程度上保护有效信息源，使其不被割裂。

RPP（Refined Part Pooling）：实现了人体分割中的软分割，在原有水平分割的基础上再进行相应训练，融入对抗训练的思想使的再分割后的图像更加符合细粒度的特征提取，有效的解决了硬性分割带来的有效信息割裂的问题，保证了信息的完整性。

[相关解读1](https://zhuanlan.zhihu.com/p/31947809) [相关解读2](https://blog.csdn.net/Gavinmiaoc/article/details/80350613)