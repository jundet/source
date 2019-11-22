---
title: Video Person Re-Identification
date: 2018-11-14 18:37:53
tags: # 行人再识别 
    - 行人再识别 
categories: 行人再识别
---

[Paper](https://handong1587.github.io/deep_learning/2015/10/09/re-id.html) [Datasets](http://robustsystems.coe.neu.edu/sites/robustsystems.coe.neu.edu/files/systems/projectpages/reiddataset.html) [Code1](https://github.com/KaiyangZhou/deep-person-reid) [Code2](https://github.com/jiyanggao/Video-Person-ReID)

#### Leaderboard

| rank1/mAP    |iLIDS-VID       | PRID2011 | MARS  | DukeMTMC-VideoReID |
| ------------ | --------- | --------- | --------- | ------------------ |
| [SCAN](#SCAN) | 88.0/89.9 | 95.3/95.8 | 87.2/77.2| /                  |
| [Co-attention](#Co-attention) | 85.4/87.8 | 93.0/94.5 | 86.3/76.1 | / |
| [3DCNN&Non-local](3DCNNNon-local) | 81.3 | 91.2 | 84.3/77.0 | / |
| [STAN](#STAN) | 80.2/ | 93.2/ | 82.3/65.8 | / |
| [RQEN](#RQEN) | 77.1/ | 91.8/ | 77.83/71.14 | / |



##### <span id = "RQEN">(RQEN)Region-based Quality Estimation Network for Large-scale Person Re-identification</span>

paper:https://arxiv.org/abs/1711.08766

code:https://github.com/sciencefans/Quality-Aware-Network

##### <span id = "STAN">(ATAN)Diversity Regularized Spatiotemporal Attention for Video-based Person Re-identification</span>

paper:https://arxiv.org/abs/1803.09882

##### <span id = "Co-attention">(Co-attention)Video Person Re-identification with Competitive Snippet-similarity Aggregation and Co-attentive Snippet Embedding</span>

paper:http://openaccess.thecvf.com/content_cvpr_2018/papers/Chen_Video_Person_Re-Identification_CVPR_2018_paper.pdf

##### <span id = "3DCNNNon-local">(3DCNN&Non-local)Video-based Person Re-identification via 3D Convolutional Networks and Non-local Attention</span>

paper: https://arxiv.org/abs/1807.05073

##### <span id = "SCAN">SCAN: Self-and-Collaborative Attention Network for Video Person Re-identification</span>

paper:https://arxiv.org/abs/1807.05688

##### Revisiting Temporal Modeling for Video-based Person ReID

paper:https://arxiv.org/abs/1805.02104

code:https://github.com/jundet/Video-Person-ReID