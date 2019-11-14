---
title: LDA与PDA
date: 2019-11-14 15:45:45
tags:
	- 机器学习
	- 降维
mathjax: true
toc: true 
categories: 机器学习
---

## 线性判别分析（LDA）

LDA是一种经典的线性学习方法，也称为“Fisher判别分析”。

LDA的基本思想：给定训练集，设法将样例投影到一条直线上，使得同类样例的投影点尽可能接近，不同种类样例的投影点尽可能远。

为实现同类样例的投影点尽可能接近，可让同类样例投影点的协方差尽可能小。而实现不同种类样例的投影点尽可能远，则不同种类样例投影中心的距离尽可能大。

### 二分类问题

同时实现以上两种情况则可最大化$J$.
$$
J= \frac{\|\omega^T\mu_0 - \omega^T\mu_1\|_2^2}{\omega^T \Sigma_0\omega + \omega^T\Sigma_1\omega}\\
=\frac{\omega^T(\mu_0-\mu_1)(\mu_0-\mu_1)^T\omega}{\omega^T(\Sigma_0+\Sigma_1)\omega}
$$
其中$\mu_i$为第i类的均值向量、$\Sigma_i$为第i类的协方差矩阵，$\omega$为投影直线。$\omega^T\mu_i$为第i类投影到$\omega$上的投影中心，$\omega^T \Sigma_i\omega$为第i类投影到$\omega$上的协方差矩阵

设$S_\omega$为类内散度矩阵
$$
\begin{aligned}
S_\omega&=\Sigma_0+\Sigma_1\\
&=\sum_{x\in X_0}(x-\mu_0)(x-\mu_0)^T + \sum_{x\in X_1}(x-\mu_1)(x-\mu_1)^T
\end{aligned}
$$
设$S_b$为类间散度矩阵
$$
S_b=(\mu_0-\mu_1)(\mu_0-\mu_1)^T
$$
则
$$
J=\frac{\omega^TS_b\omega}{\omega^TS_\omega\omega}
$$
此时$J$就是LDA的最大化目标，即$S_b$与$S_\omega$的广义瑞利商。

为求$\omega$令$\omega^TS_\omega\omega=1$,此时优化目标转变为
$$
min_\omega -\omega^TS_b\omega\\
s.t. \omega^TS_\omega\omega=1
$$
由拉格朗日乘子式,
$$
S_b\omega=\lambda S_\omega \omega
$$
令$S_b\omega=\lambda(\mu_0-\mu_1)$则
$$
\omega=S_\omega^{-1}(\mu_0-\mu_1)
$$

### 多分类问题

假定存在N个类，且第i类示例数为$m_i$。

设全局散度矩阵为$S_t$
$$
S_t=S_b+S_\omega\\
=\sum_{i=1}^{m}(x_i-\mu)(x_i-\mu)^T
$$
其中$\mu$是所有示例的均值向量，此时
$$
S_\omega=\sum_{i=1}^N S_{\omega i}
$$
其中
$$
S_{\omega i}=\sum_{x \in X_i}(x-\mu_i)(x-\mu_i)^T
$$
则
$$
S_b=S_t-S_\omega\\
=\sum_{i=1}^N m_i(x-\mu_i)(x-\mu_i)^T
$$
多分类的优化目标为
$$
max_W \frac{tr(W^TS_bW)}{tr(W^TS_\omega W)}
$$
其中$W\in R^{d\times (N-1)}$,
$$
S_bW=\lambda S_\omega W
$$
$W$的闭式解则是$S_\omega^{-1}S_b$的$d'$个最大非零广义特征值所对应的特征向量组成的矩阵。

LDA是一种经典的有监督降维技术，其流程为

1.计算类内散度矩阵$S_\omega$

2.计算类间散度矩阵$S_b$

3.对$S_\omega^{-1}S_b$进行特征分解

4.返回最大非零广义特征值对应的特征向量

## 主成分分析（PCA）

PCA是一种典型的无监督降维方法。如果用一个超平面对所有样本进行恰当的描述，则超平面应满足的性质有：

* 最近重构性：样本点到这个超平面的距离都足够近。

* 最大可分性： 样本点在这个超平面上的投影尽可能分开。

从最大可分性分析，样本点$x_i$在超平面上的投影为$W^Tx_i$，为实现所有样本点的投影尽可能分开这一目标，则应该使投影后的样本点之间方差最大化。投影后样本点的方差为$\sum_iW^Tx_ix_i^TW$,则最优化目标为
$$
max_W  tr(W^TXX^TW)\\
s.t. W^TW=I
$$
对上式使用拉格朗日乘子式可得
$$
XX^T\omega_i=\lambda \omega _i
$$
于是对$XX^T$进行特征分解，对特征值进行排序，取前$d'$个特征值对应的特征向量构成特征矩阵。

PCA的流程为

1.对所有样本进行中心化：$x_i\gets x_i -\mu$,其中$\mu$是均值

2.计算样本的协方差矩阵$XX^T$

3.对矩阵进行特征值分解

4.取最大的$d'$个特征值对应的特征向量构成特征矩阵（投影矩阵）。

输出投影矩阵

## 异同点比较

### 相同点

1、LDA与PCA都是典型的降维方法。

2、LDA与PCA都假设样本符合高斯分布。

3、LDA与PCA都应用可特征值分解

### 不同点

1、LDA为有监督，PCA为无监督

2、PCA是去掉原有数据的冗余的维度，LDA是选择一个最佳的投影方向，使得投影后相同类别的数据分布紧凑，不同类别的数据尽量相互远离。

3、LDA最多可以降到k-1维（k是训练样本的类别数量，k-1是因为最后一维的均值可以由前面的k-1维的均值表示）；PCA无限制

4、LDA可能会过拟合数据。

  