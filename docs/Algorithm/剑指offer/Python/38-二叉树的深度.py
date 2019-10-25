# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def TreeDepth(self, pRoot):
        # write code here
		# leetcode 104
		# 平衡二叉树 leetcode 110
        if not pRoot:
            return 0
        return max(self.TreeDepth(pRoot.left),self.TreeDepth(pRoot.right)) + 1