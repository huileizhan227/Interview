class Solution:
    def NumberOf1(self, n):
        # write code here
		# leetcode 191
        count = 0
        if n < 0:
            n = n & 0xffffffff
        while n != 0:
            count += 1
            n = (n - 1) & n
        return count