# -*- coding:utf-8 -*-
'''
在一个二维数组中，每一行都按照从左到右递增的顺序排序
每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
'''
import unittest
# 二维数组中的查找

class Solution:
    def Find(self, target, array):
        # write code here
        if not array:
            return False
        row = 0
        col = len(array[0])-1
        while row < len(array) and col >=0:
            if array[row][col] == target:
                return True
            elif array[row][col] < target:
                row = row + 1
            else:
                col = col - 1
        return False