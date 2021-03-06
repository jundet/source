---
title: 线性回归
date: 2019-09-24 09:46:53
tags:
	- 机器学习
mathjax: true
toc: true 
categories: 机器学习
---

## 线性回归

### 一元线性回归

给定数据集$D={(x_1,y_1),(x_2,y_2),...,(x_m,y_m)}$试图学得线性回归$f(x_i)=wx_i+b$,使得$f(x_i)\simeq y_i$

采用均方差度量$f(x_i)$与$y_i$之间的差距，最小化均方差
$$
(w^*,b^*)=\arg min_{(w,b)}\sum_{i=1}^m(f(x_i)-y_i)^2=\arg min_{(w,b)}\sum_{i=1}^m(y_i-wx_i-b)^2
$$
求解$w$和$b$使得$E_{(w,b)}=\sum_{i=1}^m(y_i-wx_i-b)^2$最小化的过程，称为线性回归模型的最小二乘参数估计，对$w$和$b$分别求导可得到
$$
\frac{\partial E_{(w,b)}}{\partial w}=2(w\sum_{i=1}^mx_i^2-\sum_{i=1}^m(y_i-b)x_i) \tag{1}
$$

$$
\frac{\partial E_{(w,b)}}{\partial b}=2(mb-\sum_{i=1}^m(y_i-wx_i)) \tag{2}
$$

令式（1）和式（2）为零可得到$w$和$b$的闭式解
$$
w=\frac{\sum_{i=1}^my_i(x_i-\bar{x})}{\sum_{i=1}^mx_ix_i^2-{\frac{1}{m}}(\sum_{i=1}^mx_i)^2}\\
b=\frac{1}{m}\sum_{i=1}^m(y_i-wx_i)
$$
其中$\bar{x}={\frac{1}{m}}(\sum_{i=1}^mx_i)$为$x$的均值。

### 多元线性回归

$f(x_i)=w^Tx_i+b$使得$f(x_i)\simeq y_i$。参数的向量化形式为$\hat{w}=(w;b)$。最小化距离的向量形式为
$$
\hat{w}^*=\arg min_{\hat{w}}(y-X\hat{w})^T(y-X\hat{w})
$$
令$E_{\hat{w}}=(y-X\hat{w})^T(y-X\hat{w})$,对$\hat{w}$求导得到
$$
\frac{\partial E_{(\hat{w})}}{\partial \hat{w}}=xX^T(X\hat{w}-y) \tag{3}
$$
令式（3）为零可以求得$\hat{w}$的最优解的闭式解。

当$X^TX$为满秩矩阵或正定矩阵时可得
$$
\hat{w}^*=(X^TX)^{-1}X^Ty
$$
其中$(X^TX)^{-1}$是矩阵$X^TX$的逆矩阵，令$\hat{x}_i=(x_i;1)$,最终学得的多元线性回归模型为
$$
f(\hat{x}_i)=\hat{x}^T_i(X^TX)^{-1}X^Ty
$$
当$X^TX$不是满秩矩阵时常常引入正则化项。

#### 对数线性回归

$$
\ln{y}=w^Tx+b \tag{4}
$$

式（4）实际上是在试图让$e^{w^Tx+b}$逼近$y$，虽然在形式上仍然是现象回归，但实质上实在求取输入空间到输出空间的非线性函数映射。

## 对数几率回归

对数几率回归的实质是分类问题

对于二分类任务，使用阶跃函数将实值$z$转换为$0/1$值。一种单位阶跃函数如下所示
$$
y=\left\{ \begin{array}{ll}
0,&\textrm{z<0}\\
0.5,&\textrm{z=0}\\
1,&\textrm{z>0}
\end{array} \right.
$$
单位阶跃函数不连续，因此不能直接使用，而对数几率函数单调可微，对数几率函数是一种“Sigmoid函数”
$$
y=\frac{1}{1+e^{-(w^Tx+b)}}
$$
类似于式（4）
$$
\ln \frac{y}{1-y}=w^Tx+b
$$
若将$y$视为样本$x$作为正例的可能性，则$1-y$是其反例可能性，两者的比值称为几率，反应了$x$作为正例的可能性。对几率取对数可得到对数几率（logit）$\ln \frac{y}{1-y}$，因此使用线性回归模型的预测结果取逼近真是标记的对数几率，其模型称为对数几率回归。