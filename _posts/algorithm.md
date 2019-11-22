---
title: 算法导论
date: 2018-10-08 21:36:57
tags: 算法
mathjax: true
toc: true 
categories: 算法
---

# 算法导论

## 第一章 算法在计算中的应用

### 1.2 作为一种技术的算法

#### 练习

1.2-2 插入排序运行步数为$8n^2$步，而归并排序运行$64nlgn$ 步，问对哪些n值，插入排序优于归并排序？
	$8n^2 < 64nlgn$，n=2,3

1.2.3 n最小值为何值时，运行时间为$100n^2$的一个算法在相同机器上快于运行时间为$2^n$ 的另一个算法？
	$100n^2  < 2^n$,n=15

#### 思考题

1-1 （运行时间比较）假设求解问题的算法需要$f(n)$ 毫秒，对下表中每个函数$f(n)$ 和时间t，确定可以在时间t内求解的问题的最大规模n。

|            | 1秒钟  | 1分钟          | 1小时            | 1天              | 1月                  | 1年                   | 1世纪                 |
| ---------- | ------ | -------------- | ---------------- | ---------------- | -------------------- | --------------------- | --------------------- |
| $lgn$      | $10^4$ | $6\times 10^5$ | $3.6\times 10^7$ | $8.64\times10^8$ | $2.592\times10^{10}$ | $3.1536\times10^{11}$ | $3.1536\times10^{13}$ |
| $\sqrt{n}$ | $10^6$ |                |                  |                  |                      |                       |                       |
| $n$        | $10^3$ |                |                  |                  |                      |                       |                       |
| $nlgn$     | 386    |                |                  |                  |                      |                       |                       |
| $n^2$      | 31     |                |                  |                  |                      |                       |                       |
| $n^3$      | 10     |                |                  |                  |                      |                       |                       |
| $2^n$      | 9      |                |                  |                  |                      |                       |                       |
| $n!$       | 6      |                |                  |                  |                      |                       |                       |



## 第二章 算法基础

### 2.1 插入排序

#### 伪代码

```text
INSERTION-SORT(A)
for j = 2 to A.length
	key = A[j]
	//inster A[j] into the sorted sequence A[1..j-1]
	i = j-1
	while i>0 and A[i]>key
		A[i+1] = A[i]
		i = i-1
	A[j+1] = key
```

#### python 实现

```python
def insertion_sort(A):
    for j in range(1,len(A)):
        key = A[j]
        i = j-1
        while i>-1 and A[i]>key:
            A[i+1] = A[i]
            i -= 1
        A[i+1] = key
    return A
```

#### 练习

2.1-2 重写INSERTION-SORT，使之按降序排序。

```python
def insertion_sort(A):
    for j in range(1,len(A)):
        key = A[j]
        i = j-1
        while i>-1 and A[i]<key: # 将原来的A[i]>k改为 A[i]<k
            A[i+1] = A[i]
            i -= 1
        A[i+1] = key
return A
```

2.1-3 考虑以下查找问题：
	输入：n个数的一个序列A=<a<sub>1</sub>，a<sub>2</sub>,...,a<sub>n</sub>>	和一个数v
	输出：当v=A[i]时输出下标i，当v不在A中时输出特殊值 NIL
	写出线性查找的伪代码，它扫描整个序列来查找v。使用一个循环不变是来证明你的算法正确性。确保你的循环不变式满足三个必要的性质。

```
	j = -1
	for i = 0 to A.length:
		if A[i] == v
			j = i
			break
		else:
        	i++
	if j == -1:
		return NIL
	else:
		return j
```

2.1-4 考虑将将两个n位二进制整数加起来，这两个整数分别存储在两个n位数组中A和B中，这两个整数的和应该按照二进制形式存储在一个（n+1）元数组C中，写出伪代码。

```
z = 0
for j = 1 to n：
	i = n - j
	m = A[i] + B[i] + z
	if m%2==0:
		c[i+1] = 0
	else:
		c[i+1] = 1
	if m>1:
		z = 1
	else:
		z = 0
	j++
```

### 2.2 分析算法

##### 练习

2.2-1 用$\Theta$ 记号表示函数$n^3/1000 - 100n^2 -100n +3$

$\Theta(n^3)$

2.2-1 对储存在数组A中的n个数进行排序：首先找出A中最小元素并将其与A[1]中的元素进行交换。接着找出A中的次最小元素并将其与A[2]中的元素进行交换。对A中前n-1个圆度按照该方式继续，该算法叫做选择排序，写出其伪代码。用$\Theta$给出选择排序的最好情况与最坏情况运行的时间。

```
for i = 0 to A.length      
	min = a[i]
	tempj = i
	for j = A.length - i to A.length  
		if a[j] < min:
			min = a[j]
			tempj = j
	temp = a[i]
	a[i] = min
	a[j] = temp
```

最好情况时即已经排序好，则为$\Theta(n)$，最坏的情况为逆序，则为$\Theta(n^2)$

2.2-3 线性查找平均需要检查输入序列的多少个元素，最坏的情况又如何？

平均查找需要$\theta(n/2)$,最坏需要$\theta(n)$

### 2.3 设计算法

#### 2.3.1 分治法

```
MERGE(A, p, q, r)
n1 = q - p + 1
n2 = r - q
let L[1..n1 + 1] and R[1..n2 + 1] by new arrays
for i = 1 to n1
	L[i] = A[p + i -1]
for j =  1 to n2
	R[j] = A[q + j]
L[n1 + 1] = & infin;
L[n2 + 1] = & infin;
i = 1
j = 1
for k = p to r
	if L[i] <= R[j]
		A[k] = L[i]
		i = i + 1
	else 
		A[k] = R[j]
		j = j + 1
```

```
MEGRE-SORT(A, p, r)
if p < r
	q = [(p+r)/2]
	MEGRE-SORT(A, p, q)
	MEGRE-SORT(A, q+1, r)
	MERGE(A, p, q, r)
```

归并排序算法python实现

```python
# 分
def sort(A):
    # 分
    if len(A)<=1:
        return A

    middle = len(A)//2
    left = sort(A[:middle])
    right = sort(A[middle:])
    # 治
    return merge(left,right)

# 治
def merge(left,right):
    c = []
    h = j = 0
    while j<len(left) and h<len(right):
        if left[j]<right[h]:
            c.append(left[j])
            j+=1
        else:
            c.append(right[h])
            h+=1

    if j==len(left):
        for i in right[h:]:
            c.append(i)
    if h==len(right):
        for i in left[j:]:
            c.append(i)

    return c
```



## 第3章 函数的增长

## 第7章 快速排序

### 7.1 快速排序的描述

```
QUICKSOURT(A, p, r)
	if p<r
		q = PARTITION(A, p, r)
		QUICKSOURT(A, p, q-1)
		QUICKSOURT(A, q+1, r)

PARTITION(A, p, r)
	x = A[r]
	i = p-1
	for j=p to r-1
		if A[j]<x
			i = i+1
			exchange A[i] with A[j]
	exchange A[i+1] with A[r]

```

快速排序的python实现
```python
def quicksort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quicksort(A, p, q-1)
        quicksort(A, q+1, r)

def partition(A, p, r):
    x = A[r]
    i = p-1
    for j in range(p, r):
        if A[j]<=x:
            i += 1
            A[i], A[j] = A[j], A[i] # 交换位置，将小于x的放到左边，i是划分的位置点
    A[i+1], A[r] = A[r], A[i+1]  # 最后将主元x放到两个序列中间
    return i+1
```

### 7.2 快速排序的性能

1、最坏情况划分

当每次划分的两个子问题分别含有n-1个元素和0个元素时，此时快速排序的时间复杂度为$O(n^2)$

2、最好情况划分

在最平衡划分时每个子问题的规模都不大于n/2，此时时间复杂度为$O(nlgn)$

3、平衡的划分

最一般的情况下，两个子问题都不是最坏的情况也不是最平衡时，时间复杂度同样为$O(nlgn)$

### 7.3 快速排序的随机化版本

在上面的快速排序中主元每次都是取A[r]，随机化的版本则是每次随机化的选取数组中的一个元素作为主元，这样会使得数组的划分更为均衡化。

```
RANDOMIZED-PARTITION(A, p, r)
	i = RANDOM(p, r)
	exchange A[r] with A[i]
	return PARTITION(A, p, r)
# 随机化的快速排序不在调用PARTITION,而是调用RANDOMIZED-PARTITION
RANDOMIZED-QUICKSOURT(A, p, r)
	if p<r
		q = RANDOMIZED-PARTITION(A, p, r)
		RANDOMIZED-QUICKSOURT(A, p, q-1)
		RANDOMIZED-QUICKSOURT(A, q+1, r)
```

随机化的快速排序python实现

```python
import random

def randomzed_quicksort(A, p, r):
    if p < r:
        q = randomzed_(A, p, r)
        randomzed_quicksort(A, p, q-1)
        randomzed_quicksort(A, q+1, r)
        
#随机化过程
def randomzed_(A, p, r):
    i = random.randint(p, r)
    A[r],A[i] = A[i],A[r]
    return partition(A, p, r)

def partition(A, p, r):
    x = A[r]
    i = p-1
    for j in range(p, r):
        if A[j]<=x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1
```

