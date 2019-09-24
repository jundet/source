---
title: transform
date: 2019-09-20 09:58:25
tags:
	- PyTorch
	- 深度学习
	- 机器学习
categories: PyTorch
---

# PyTorch数据处理之transforms

```python
from torchvision import transforms
```

[PyTorch 官方文档](https://pytorch.org/docs/stable/torchvision/transforms.html#transforms-on-pil-image)

transforms主要应用于数据的预处理阶段。PIL Image是PyTorch中默认读取图像的方式，torchvision.transforms在图像处理中主要分为4类。

#### 裁剪——Crop

中心裁剪：transforms.CenterCrop
随机裁剪：transforms.RandomCrop
随机长宽比裁剪：transforms.RandomResizedCrop
上下左右中心裁剪：transforms.FiveCrop
上下左右中心裁剪后翻转，transforms.TenCrop

#### 翻转和旋转——Flip and Rotation

依概率p水平翻转：transforms.RandomHorizontalFlip(p=0.5)
依概率p垂直翻转：transforms.RandomVerticalFlip(p=0.5)
随机旋转：transforms.RandomRotation

#### 图像变换

resize：transforms.Resize
标准化：transforms.Normalize
转为tensor：transforms.ToTensor
填充：transforms.Pad
修改亮度、对比度和饱和度：transforms.ColorJitter
转灰度图：transforms.Grayscale
线性变换：transforms.LinearTransformation()
仿射变换：transforms.RandomAffine
依概率p转为灰度图：transforms.RandomGrayscale
将数据转换为PILImage：transforms.ToPILImage
transforms.Lambda：添加用户自定义的处理过程

#### 随机处理

transforms.RandomChoice(transforms)：从给定的一系列transforms中选一个进行操作
transforms.RandomApply(transforms, p=0.5)：给一个transform加上概率，依概率进行操作
transforms.RandomOrder：将transforms中的操作随机打乱

#### 常用方法

##### transforms.Resize

class torchvision.transforms.Resize(size, interpolation=2)

将输入的PIL图像缩放至size的分辨率

**size**：（输入类型为int或者sequence ）需要输出的图像大小

**interpolation**：采样（插值）方式（输入类型为int）。默认为PIL.Image.BILINEAR

可选项：PIL.Image.NEAREST、PIL.Image.BILINEAR、PIL.Image.BICUBIC、PIL.Image.LANCZOS、PIL.Image.HAMMING、PIL.Image.BOX

##### transforms.Normalize

class torchvision.transforms.Normalize(*mean*, *std*, *inplace=False*)

使用平均或标准差标准化。其作用就是先将输入归一化到(0,1)，再使用公式”(x-mean)/std”，将每个元素分布到(-1,1) 

```python
transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])

tensor.sub_(mean[:, None, None]).div_(std[:, None, None])
```
##### transforms.ToTensor

CLASS torchvision.transforms.ToTensor

将PIL.image或者numpy.ndarray转为tensor

将PIL.image或者numpy.ndarray(H x W x C) [0, 255]转换为 torch.FloatTensor(C x H x W)  [0.0, 1.0]