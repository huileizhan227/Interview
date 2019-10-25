class Solution:
    def InversePairs(self, data):
        # write code here
		# 拷贝该数组后对拷贝的数组排序。计算数组中的最小值在原始数组中出现的位置，
		# 统计原始数组中最小值前面的个数，之后在原始数组中去掉最小值
        sortData = sorted(data)
		count = 0
		for i in sortData:
			pos = data.index(i)
			count += pos
			data.pop(pos)
		return count
             
        return count%1000000007
    
    

count = 0
class Solution:
    def InversePairs(self, data):
        global count
        def MergeSort(lists):
            global count
            if len(lists) <= 1:
                return lists
            num = int( len(lists)/2 )
            left = MergeSort(lists[:num])
            right = MergeSort(lists[num:])
            r, l=0, 0
            result=[]
            while l<len(left) and r<len(right):
                if left[l] < right[r]:
                    result.append(left[l])
                    l += 1
                else:
                    result.append(right[r])
                    r += 1
                    count += len(left)-l
                    print 'count: ', count
            result += right[r:]
            result += left[l:]
 
            return result
        MergeSort(data)
        return count%1000000007
