# -*- coding:utf-8 -*-
class Solution:
    def IsContinuous(self, numbers):
        # write code here
        if not numbers or len(numbers) == 0:
            return False
        
        transdict = {'A':1,'J':11,'Q':12,'K':13}
        for i in range(len(numbers)):
            if numbers[i] in transdict.keys():
                numbers[i] = transdict[numbers[i]]
                
        numbers = sorted(numbers)
        number_0 = 0
        number_gap = 0
        
        i = 0
        while i < len(numbers) and numbers[i] == 0:
            number_0 += 1
            i += 1
            
        front = number_0
        behind = front + 1
        while behind < len(numbers):
            if numbers[front] == numbers[behind]:
                return False
            number_gap += numbers[behind] - numbers[front] - 1
            front = behind
            behind += 1
        return False if number_gap > number_0 else True
	
	def IsContinuous(self, numbers):
        # write code here
        if len(numbers) == 0:
            return False
        # 对数字进行排序
        numbers.sort()
        # 大小王个数
        number_0 = numbers.count(0)
        number_gap = 0
        for i in range(number_0, len(numbers) - 1):	# 已排序，number_0的位置即为首个非0数字位置
            if numbers[i] == numbers[i + 1]:	# 出现对子，就不可能是顺子
                return False
            else:
                # 统计相邻数字之间的空缺数
                number_gap += (numbers[i + 1] - numbers[i] - 1)
        if number_gap <= number_0:
            return True
        else:
            return False