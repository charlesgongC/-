# -*- coding:utf-8 -*-
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