# 最大子数组 分治法
import math
import sys


def max_cross_subarray(A, low, mid, high):
    left_sum = float("-inf")
    sum = 0
    max_left = mid
    max_right = mid
    for i in range(mid-low):
        sum = sum + A[mid-i]
        if sum > left_sum:
            left_sum = sum
            max_left = mid - i
    right_sum = float("-inf")
    sum = 0
    for i in range(mid, high):
        sum = sum + A[i]
        if sum > right_sum:
            left_sum = sum
            max_right = i

    return max_left, max_right, left_sum+right_sum


def max_subarray(A, low, high):
    if high == low:
        return low, high, A[low]
    else:
        mid = math.floor((low+high)/2)
        left_low, left_high, left_sum = max_subarray(A, low, mid)
        right_low, right_high, right_sum = max_subarray(A, mid, high)
        cross_low, cross_high, cross_sum = max_cross_subarray(A, low, mid, high)
        if left_sum > right_sum and left_sum > cross_sum:
            return left_low, left_high, left_sum
        elif right_sum > left_sum and right_sum > cross_sum:
            return left_low, left_high, left_sum
        else:
            return cross_low, cross_high, cross_sum


def main():
    A = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
    low, high, sum = max_subarray(A, 0, len(A)-1)
    print(low, ";", high, ";", sum)


if __name__ == "__main__":
    main()
