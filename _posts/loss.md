---
title: 损失函数
date: 2019-09-20 15:35:00
tags:
	- loss
	- PyTorch
	- 深度学习
mathjax: true
toc: true 
categories: 深度学习
---

# PyTorch中的损失函数

```python
import torch.nn as nn
```

[PyTorch 官方文档](https://pytorch.org/docs/stable/nn.html#loss-functions)

PyTorch中的损失函数有L1Loss、MSELoss、CrossEntropyLoss、NLLLoss、PoissonNLLLoss、KLDivLoss、BCELoss、BCEWithLogitsLoss、MarginRankingLoss、HingeEmbeddingLoss、MultiLabelMarginLoss、SmoothL1Loss、SoftMarginLoss、MultiLabelSoftMarginLoss、CosineEmbeddingLoss、MultiMarginLoss、TripletMarginLoss等损失函数。

### L1Loss

CLASS torch.nn.L1Loss(size_average=None, reduce=None, reduction='mean')

计算差值的绝对值。

#### 参数

##### reduction

可选项为‘none’、‘mean’、‘sum’。‘mean’返回平均值，‘sum’返回损失值之和。

其他两个参数已经弃用

### MSELoss

CLASS torch.nn.MSELoss(size_average=None, reduce=None, reduction='mean')

计算差值的平方。

#### 参数

##### reduction

可选项为‘none’、‘mean’、‘sum’。‘mean’返回平均值，‘sum’返回损失值之和。

其他两个参数已经弃用

### CrossEntropyLoss

CLASS torch.nn.CrossEntropyLoss(weight=None, size_average=None, ignore_index=-100, reduce=None, reduction='mean')

计算交叉熵损失。

#### 参数

##### weight

tenser，n个元素，代表n类的权重，当样本不平衡时使用会非常有用，默认为None

当weight=None时
$$
loss(x,class)=-log{\frac {e^{x[class]}}{\sum_je^{x[j]}}}=-x[class]+log(\sum_je^{x[j]})
$$
当weight被指定时
$$
loss(s,class)=weights[class]*(-x[class]+log(\sum_je^{x[j]}))
$$


##### reduction

可选项为‘none’、‘mean’、‘sum’。‘mean’返回平均值，‘sum’返回损失值之和。

### TripletMarginLoss

CLASS torch.nn.TripletMarginLoss(margin=1.0, p=2.0, eps=1e-06, swap=False, size_average=None, reduce=None, reduction='mean')

计算三元组损失
$$
L(a,p,n)=max\{{d(a_i,p_i)-d(a_i,n_i)+margin,0}\}
$$
其中$d(x_i,y_i)=||x_i-y_i||_p$

##### margin

边界大小，默认为1

##### reduction

可选项为‘none’、‘mean’、‘sum’。‘mean’返回平均值，‘sum’返回损失值之和。

TripletSemihardLoss和TripletLoss的实现方式

```python
import torch
from torch import nn
from torch.nn import functional as F

class TripletSemihardLoss(nn.Module):
    """
    Shape:
        - Input: :math:`(N, C)` where `C = number of channels`
        - Target: :math:`(N)`
        - Output: scalar.
    """

    def __init__(self, device, margin=0, size_average=True):
        super(TripletSemihardLoss, self).__init__()
        self.margin = margin
        self.size_average = size_average
        self.device = device

    def forward(self, input, target):
        y_true = target.int().unsqueeze(-1)
        same_id = torch.eq(y_true, y_true.t()).type_as(input)

        pos_mask = same_id
        neg_mask = 1 - same_id

        def _mask_max(input_tensor, mask, axis=None, keepdims=False):
            input_tensor = input_tensor - 1e6 * (1 - mask)
            _max, _idx = torch.max(input_tensor, dim=axis, keepdim=keepdims)
            return _max, _idx

        def _mask_min(input_tensor, mask, axis=None, keepdims=False):
            input_tensor = input_tensor + 1e6 * (1 - mask)
            _min, _idx = torch.min(input_tensor, dim=axis, keepdim=keepdims)
            return _min, _idx

        # output[i, j] = || feature[i, :] - feature[j, :] ||_2
        dist_squared = torch.sum(input ** 2, dim=1, keepdim=True) + \
                       torch.sum(input.t() ** 2, dim=0, keepdim=True) - \
                       2.0 * torch.matmul(input, input.t())
        dist = dist_squared.clamp(min=1e-16).sqrt()

        pos_max, pos_idx = _mask_max(dist, pos_mask, axis=-1)
        neg_min, neg_idx = _mask_min(dist, neg_mask, axis=-1)

        # loss(x, y) = max(0, -y * (x1 - x2) + margin)
        y = torch.ones(same_id.size()[0]).to(self.device)
        return F.margin_ranking_loss(neg_min.float(),
                                     pos_max.float(),
                                     y,
                                     self.margin,
                                     self.size_average)

class TripletLoss(nn.Module):
    """Triplet loss with hard positive/negative mining.

    Reference:
    Hermans et al. In Defense of the Triplet Loss for Person Re-Identification. arXiv:1703.07737.

    Code imported from https://github.com/Cysu/open-reid/blob/master/reid/loss/triplet.py.

    Args:
        margin (float): margin for triplet.
    """
    def __init__(self, margin=0.3, mutual_flag = False):
        super(TripletLoss, self).__init__()
        self.margin = margin
        self.ranking_loss = nn.MarginRankingLoss(margin=margin)
        self.mutual = mutual_flag

    def forward(self, inputs, targets):
        """
        Args:
            inputs: feature matrix with shape (batch_size, feat_dim)
            targets: ground truth labels with shape (num_classes)
        """
        n = inputs.size(0)
        # Compute pairwise distance, replace by the official when merged
        dist = torch.pow(inputs, 2).sum(dim=1, keepdim=True).expand(n, n)
        dist = dist + dist.t()
        dist.addmm_(1, -2, inputs, inputs.t())
        dist = dist.clamp(min=1e-12).sqrt()  # for numerical stability
        # For each anchor, find the hardest positive and negative
        mask = targets.expand(n, n).eq(targets.expand(n, n).t())
        dist_ap, dist_an = [], []
        for i in range(n):
            dist_ap.append(dist[i][mask[i]].max().unsqueeze(0))
            dist_an.append(dist[i][mask[i] == 0].min().unsqueeze(0))
        dist_ap = torch.cat(dist_ap)
        dist_an = torch.cat(dist_an)
        # Compute ranking hinge loss
        y = torch.ones_like(dist_an)
        loss = self.ranking_loss(dist_an, dist_ap, y)
        if self.mutual:
            return loss, dist
        return loss
```

