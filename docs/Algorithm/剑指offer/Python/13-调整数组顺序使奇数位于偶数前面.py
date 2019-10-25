class Solution:
    def reOrderArray(self, array):
        # write code here
        return sorted(array,key=lambda c:c%2==0)	# 即偶数判断为较大数，放在后面