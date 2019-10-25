# -*- coding:utf-8 -*-
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if not tinput or k > len(tinput):
            return []
        tinput = self.quick_sort(tinput)
        return tinput[:k]
    
    def quick_sort(self,lst):
        if not lst:
            return []
        pivot = lst[0]
        left = self.quick_sort([x for x in lst[1: ] if x < pivot])
        right = self.quick_sort([x for x in lst[1: ] if x >= pivot])
        
        return left + [pivot] + right
	
	# 方法二：堆排序 针对大数据
	# 创建一个大小为K的数据容器来存储最小的K个数，然后遍历整个数组，将每个数字和容器中的最大数进行比较，
	# 如果这个数大于容器中的最大值，则继续遍历，否则用这个数字替换掉容器中的最大值
	import heapq
	def GetLeastNumbers_Solution(self, alist, k):
		max_heap = []
		length = len(alist)
		if not alist or k <= 0 or k > length:
			return
		for ele in alist:
			ele = -ele	# 取负数，变最小堆为最大堆
			if len(max_heap) < k:
				heapq.heappush(max_heap, ele)
			else:
				heapq.heappushpop(max_heap, ele)	# pushpop较小值，将较大值保存在max_heap中（即将相反数最小的值保留在max_heap中）

		return [-x for x in max_heap]
	
	# 方法三
	# 利用快排思路，用类似于二分法来取到最小的k个数
	def partition(nums, low, high):
		i = low
		j = high
		key = nums[i]
		while i<j:
			while i<j and nums[j]>=key:
				j -= 1
			if i<j:
				nums[i] = nums[j]
				i += 1
			while i<j and nums[i]<key:
				i += 1
			if i<j:
				nums[j] = nums[i]
				j -= 1
		# 做完第一轮比较之后,列表被分成了两个半区,并且i=j,需要将这个数设置回base
		nums[i] = key
		return i



	def find_least_k_nums(alist, k):
		length = len(alist)
		#if length == k:
		#    return alist
		if not alist or k <=0 or k > length:
			return
		start = 0
		end = length - 1
		index = partition(alist, start, end)
		while index != k:
			if index > k:
				index = partition(alist, start, index - 1)
			elif index < k:
				index = partition(alist, index + 1, end)
		return alist[:k]
