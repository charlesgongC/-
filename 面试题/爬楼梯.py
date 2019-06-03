class Solution:
    def climbStairs(self,n):
        if n <= 1:
            return 1
        arr = [1,1,0]
        for i in range(2,n + 1):
            arr[2] = arr[0] + arr[1]
            arr[0] , arr[1] = arr[1] + arr[2]
        return arr[2]

print('abcdefg'.find(''))