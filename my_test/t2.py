import os
import sys

# 请在此输入您的代码
import sys
from collections import Counter

def solve():
    # 使用 sys.stdin.read() 快速读取全部输入，并用 strip() 去除首尾的空白字符（如换行符）
    s = sys.stdin.read().strip()
    if not s:
        return
    
    # 1. 统计每个字符出现的次数
    # Counter 会返回一个类似字典的对象，例如：{'B': 3, 'A': 3, 'C': 2}
    #counts = Counter(s)
    counts = {}
    for i in s:
      counts[i] = counts.get(i, 0) + 1
    
    # 2. 找到最大的出现次数
    max_count = max(counts.values())
    
    # 3. 收集所有出现次数等于最大次数的字母
    ans = []
    for char, count in counts.items():
        if count == max_count:
            ans.append(char)
            
    # 4. 按字母表顺序进行排序
    ans.sort()
    
    # 5. 拼接成字符串并输出
    print("-".join(ans))

if __name__ == '__main__':
    solve()