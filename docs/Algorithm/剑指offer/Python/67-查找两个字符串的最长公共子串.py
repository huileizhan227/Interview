def find_lcsubstr(s1, s2):
    # 查找两个字符串的最长公共子串
    if not s1 or not s2:
        return['',0]
    dp = [[0 for j in range(len(s2)+1)] for i in range(len(s1)+1)]
    maxx = 0
    index = 0
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i]==s2[j]:
                dp[i+1][j+1] = dp[i][j] + 1
                if dp[i+1][j+1]>maxx:
                    maxx = dp[i+1][j+1]
                    index = i + 1
    return [s1[index-maxx:index], maxx]
