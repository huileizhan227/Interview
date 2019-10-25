 def longestPalindrome(self, s: 'str') -> 'str':
		# leetcode 5
        # 以index或者（index,index+1）为中心扩展，看是否能构成回文字符串
        def findlongest(s, index, offset):
            left = index
            right = index + offset
            while left>=0 and right<len(s) and s[left]==s[right]:
                left -= 1
                right += 1
            # 当前的left和right为超限部分，估应该取[left+1:right]
            return s[left+1:right]

            # if len(current_longest) > len(longest):
            #     longest = current_longest
        
        longest = ''
        for i in range(len(s)):
            # 计算奇数子字符串，如果得到的字符串比longest长，则替换之
            odd_longest = findlongest(s, i, 0)
            if len(odd_longest) > len(longest):
                longest = odd_longest
            # 计算偶数子字符串，如果得到的字符串比longest长，则替换之
            even_longest = findlongest(s, i, 1)
            if len(even_longest) > len(longest):
                longest = even_longest
        return longest
