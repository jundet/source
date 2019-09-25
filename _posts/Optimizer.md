---
title: 优化器
date: 2019-09-19 08:50:00
tags:
	- 机器学习
	- 深度学习
	- PyTorch
mathjax: true
toc: true 
categories: 深度学习
---

## PyTorch中的优化器

```python
import torch.optim as optim
```

PyTorch提供个多个优化器，其中常用的有SGD、ASGD、RMSprop、Adam等。

### SGD

CLASS torch.optim.SGD(params, lr=<required parameter>, momentum=0, dampening=0, weight_decay=0, nesterov=False)

随机梯度下降

#### 参数

##### params(iterable)

待优化参数的iterable或者是定义了参数组的dict

##### lr(float)

学习率

##### momentum(float)

动量因子（默认为0）

##### dampening(float)

动量的抑制因子（默认为0）

##### nesterov(bool)

使用Nesterov动量（默认为False）
$$
\begin{aligned}
&Require:学习率\varepsilon,动量\alpha \\
&Require:初始参数\theta,初始速度v \\
	&while 没有达到停止准则do\\
	&从训练集中采用包含m个样本\{x^1,...,x^m\}的小批量，对应目标为y^i\\
	&应用临时更新:\widetilde{\theta} \gets\theta +\alpha v\\
	&计算梯度(在临时点):g\gets \frac{1}{m}\nabla_{\widetilde{\theta}}\sum_i L(f(x^i;\widetilde{\theta}),y^i)\\
	&计算速度更新:v\gets \alpha v-\varepsilon g\\
	&应用更新:\theta \gets \theta+v\\
	&end while
\end{aligned}
$$


### ASGD

class torch.optim.ASGD(params, lr=0.01, lambd=0.0001, alpha=0.75, t0=1000000.0, weight_decay=0)[source]

平均随机梯度下降

#### 参数

##### params(iterable)

待优化参数的iterable或者是定义了参数组的dict

##### lr(float)

学习率，默认为（1e-2）

##### lambd(float)

衰减项，默认为（1e-4）

##### alpha(float)

eta更新指数，默认为0.75

##### t0(float)

指明在哪一次开始平均化，默认为（1e6）

##### weight_decay(float)

权重衰减（L2惩罚）默认为0

### Adam

class torch.optim.Adam(params, lr=0.001, betas=(0.9, 0.999), eps=1e-08, weight_decay=0)

来源于adaptive moments

#### 参数

##### params (iterable) 

待优化参数的iterable或者是定义了参数组的dict

##### lr (float, 可选)

 学习率（默认：1e-3）

##### betas (Tuple[float, float], 可选)

 用于计算梯度以及梯度平方的运行平均值的系数（默认：0.9，0.999）

##### eps (float, 可选) 

 为了增加数值计算的稳定性而加到分母里的项（默认：1e-8）

##### weight_decay (float, 可选) 

 权重衰减（L2惩罚）（默认: 0）
$$
\begin{aligned}
&Require:步长\varepsilon(建议默认为0.001) \\
&Require:矩估计的指数衰减速度，\rho_1和\rho_2在区间[0,1]zhong (建议默认为[0.9,0.999]) \\
&Require:用于数值稳定的小常熟\delta(建议默认为1e-8) \\
&Require:初始参数\theta;\\
& 初始化一阶矩和二阶矩变量s=0,r=0;\\
& 初始化时间步t=0;\\
	&while 没有达到停止准则do\\
	&从训练集中采用包含m个样本\{x^1,...,x^m\}的小批量，对应目标为y^i\\
	&计算梯度:g\gets \frac{1}{m}\nabla_{\widetilde{\theta}}\sum_i L(f(x^i;\widetilde{\theta}),y^i)\\
	&t\gets t+1\\
	&更新有偏一阶矩估计:s\gets \rho_1s+(1-\rho_1)g\\
	&更新有偏二阶矩估计:s\gets \rho_1r+(1-\rho_2)g\odot g\\
	&修正一阶矩的偏差:\hat{s}\gets \frac{s}{a-\rho_1^t}\\
	&修正二阶矩的偏差:\hat{r}\gets \frac{s}{a-\rho_2^t}\\
	&计算更新:\Delta\theta=-\varepsilon \frac{\hat{s}}{\sqrt{\hat{r}+\delta}}\\
	&应用更新:\theta \gets \theta+\Delta\theta\\
	&end while
\end{aligned}
$$
