# class Solution:
#     def twoSum(self, numbers: List[int], target: int) -> List[int]:
#         data = {}
#         for i in range(len(numbers)):
#             j = target - numbers[i]
#             if j in data:
#                 return [data[j],i+1]
#             data[numbers[i]] = i+1


# print(chr(76))
# print(ord('A'))


# def convertToTitle(n):
#     dic = {}
#     for i in range(26):
#         dic[i] = chr(65+i)
#     ans = ""
#     while n!=0:
#         t = (n-1)%26
#         ans = dic[t] + ans
#         n = (n-1)//26
#     return ans
# print(convertToTitle(1))

# 找出数列中的众数
nums = [3,2,3]
class Solution:
    def majorityElement(self, nums):
        count = {}
        for i in nums:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
            if count[i] > len(nums)/2:
                return i


import unittest
class Test(unittest.TestCase):
    def test_majorityElement(self):
        s1 = Solution()
        self.assertEqual(s1.majorityElement(nums), 3)

if __name__ == '__main__':
    unittest.main()