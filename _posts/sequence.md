---
title: 排序算法
date: 2019-10-18 13:43:52
tags: 算法
mathjax: true
toc: true 
categories: 算法
---

# 常用排序算法的实现

基本排序算法：冒泡，选择，插入，希尔，归并，快排

## 冒泡排序

重复地走访过要排序的元素列，依次比较两个相邻的元素，如果他们的顺序（如从大到小、首字母从A到Z）错误就把他们交换过来。走访元素的工作是重复地进行直到没有相邻元素需要交换，也就是说该元素已经排序完成。

```python
def bubbleSort(data):
    '''
    冒泡排序
    :param data: 原序列
    :return: 升序排列后序列
    '''
    i = len(data)
    while i > 0:
        j = 0
        while j < i-1:
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1],data[j]
            j += 1
        i -= 1
    return data
```

## 选择排序

重复的走访要排序的元素列，(升序)选出最小的元素与第一个元素交换，第二次选出除第一个元素外的最小的元素与第二个元素交换，直到所有排序完成结束。

```python
def selectionSort(data):
    '''
    选择排序
    :param data: 原序列
    :return: 升序排列后序列
    '''
    i = 0
    while i < len(data)-1:
        j = i
        while j < len(data):
            if data[i] > data[j]:
                data[i], data[j] = data[j], data[i]
            j += 1
        i += 1
    return data
```

## 插入排序

创建一个空数组，从待排序的数组中依次选择一个元素，将该元素插入到新建数组的合适位置。

```python
def insertSort(data):
    '''
    插入排序
    :param data: 原序列
    :return: 升序排列后序列
    '''
    datatemp = [data[0]]
    for i in range(1, (len(data)-1)):
        for j in range(len(datatemp)):
            if data[i] > datatemp[-1]:
                datatemp.append(data[i])
                break
            elif data[i] < datatemp[0]:
                datatemp.insert(0, data[i])
                break
            elif datatemp[j] < data[i] < datatemp[j+1]:
                datatemp.insert(j+1, data[i])
                break
    data = datatemp
    return data
```

## 希尔排序

## 归并排序

分治法，先原序列进行递归二分，在最后一层对两个元素进行排序，然后开始利用递归合并成排序后的序列。

```python
def mergeSort(data):
    '''
    归并排序
    :param data: 原序列
    :return: 升序排列后序列
    '''
    if len(data)<=1:
        return data

    middle = len(data)//2
    left = mergeSort(data[:middle])
    right = mergeSort(data[middle:])
    # 治
    return merge(left, right)


def merge(left,right):
    # 分
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



## 快速排序

通过一趟排序将要排序的数据分割成独立的两部分，其中一部分的所有数据都比另外一部分的所有数据都要小，然后再按此方法对这两部分数据分别进行快速排序，整个排序过程可以递归进行，以此达到整个数据变成有序序列。

```python
def quickSort(data, p, r):
    '''
    快排排序
    :param data: 原序列
    :return: 升序排列后序列
    '''
    if p<r:
        q = partition(data, p, r)
        quickSort(data, p, q-1)
        quickSort(data, q+1, r)

    return data


def partition(data, p, r):
    # 快速排序，原址重排
    key = data[r]  # 中间分割点
    i = p-1
    for j in range(p, r):
        if data[j] <= key:
            i += 1
            data[i], data[j] = data[j], data[i]

    data[i+1], data[r] = data[r], data[i+1]
    return i+1
```

