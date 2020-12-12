# -*- coding: utf-8 -*-
"""
@author lanqilu
@date Created in 2020/12/12  16:44
@file 0376.摆动序列.py
@description 
"""
from typing import List

"""
如果连续数字之间的差严格地在正数和负数之间交替，则数字序列称为摆动序列。
第一个差（如果存在的话）可能是正数或负数。少于两个元素的序列也是摆动序列。

例如，[1,7,4,9,2,5] 是一个摆动序列，因为差值 (6,-3,5,-7,3)是正负交替出现的。
相反, [1,4,7,2,5]和[1,7,4,5,5] 不是摆动序列，第一个序列是因为它的前两个差值都是正数，第二个序列是因为它的最后一个差值为零。

给定一个整数序列，返回作为摆动序列的最长子序列的长度。 
通过从原始序列中删除一些（也可以不删除）元素来获得子序列，剩下的元素保持其原始顺序。

示例 1:
输入: [1,7,4,9,2,5]
输出: 6 
解释: 整个序列均为摆动序列。

示例 2:
输入: [1,17,5,10,13,15,10,5,16,8]
输出: 7
解释: 这个序列包含几个长度为 7 摆动序列，其中一个可为[1,17,10,13,10,16,8]。

示例 3:
输入: [1,2,3,4,5,6,7,8,9]
输出: 2

进阶:你能否用O(n) 时间复杂度完成此题?

链接：https://leetcode-cn.com/problems/wiggle-subsequence
"""


def method1(nums: List[int]) -> int:
    if len(nums) < 2:
        return len(nums)
    down = up = 1
    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            up = down + 1
        elif nums[i] < nums[i - 1]:
            down = up + 1
    if down > up:
        return down
    else:
        return up


def method2(nums: List[int]) -> int:
    n = len(nums)
    if n < 2:
        return n
    prevdiff = nums[1] - nums[0]
    ret = (2 if prevdiff != 0 else 1)
    for i in range(2, n):
        diff = nums[i] - nums[i - 1]
        if (diff > 0 and prevdiff <= 0) or (diff < 0 and prevdiff >= 0):
            ret += 1
            prevdiff = diff

    return ret


if __name__ == '__main__':
    nums = [1, 1, 17, 5, 10, 13, 15, 10, 5, 16, 8]
    nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    nums3 = []

    print(method1(nums))
    print(method1(nums2))
    print(method1(nums3))
    print(method2(nums))
    print(method2(nums2))
    print(method2(nums3))
