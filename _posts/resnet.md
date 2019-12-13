---
title: 深度残差网络ResNet
date: 2019-12-10 16:06:31
tags:  
    - 深度网络 
categories: 深度学习
---

# 深度残差网络ResNet

[arxiv](https://arxiv.org/pdf/1512.03385.pdf)

ResNet是目前应用最为广泛的特征提取网络之一。在Deep Residual Learning for Image Recognition中，作者将ResNet的网络层数做到了152层，其主要实现的方式是残差学习（Residual Learning）

## 残差学习

![](resnet/1.jpg)

如上图所示，假设输入为$X$，两层网络层与relu组成常用的网络块$F(X)$。一般的网络VGG、Alexnet等实现的$X \to H(X)$，其学习的参数层$F(X)=H(X)$.残差学习通过直接把恒等映射(identity mapping)作为网络的一部分，实现了残差函数$F(X)=H(X)-X$,即学习的参数由原来的$H(X)$转为$H(X)-X$。在前向传播过程中为$F(X)+X$，在经过relu后输出结果。用公式表示为
$$
y=relu(F(x,\{w_i\})+x)
$$
[ResNet解决了什么问题](https://www.zhihu.com/question/64494691?sort=created)

ResNet解决了训练很深网络时出现的梯度退化（不是梯度消失），由于非线性激活函数Relu的存在每次输入到输出的过程几乎是不可逆的，都会造成信息损失。随着网络层的增加这种损失会越来越大。使用残差网络能够使得特征在层层前行传播的过程中保留更多的信息。

不是过拟合欠拟合问题：

深度CNN的训练误差和测试误差都很大

不是梯度爆炸/消失问题：

梯度爆炸/消失问题在使用Bacth Normalization(BN)时已经基本被解决

