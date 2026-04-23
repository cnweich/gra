import sys

# 一次性读取所有数据并切分为列表
tokens = sys.stdin.read().split()

if tokens:
    it = iter(tokens)
    n = int(next(it))
    
    # 将书本编号映射为 0 索引的 target 坐标
    # 书本编号为 x，其目标位置应该是索引 x-1
    # arr[i] 表示当前索引 i 处的书本原本应该去的索引位置
    arr = [int(next(it)) - 1 for _ in range(n)]
    
    visited = [False] * n
    ans = 0
    
    # 遍历每个位置，寻找并统计所有的置换环
    for i in range(n):
        if not visited[i]:
            # 发现一个新的环，开始遍历这个环
            curr = i
            cycle_len = 0
            while not visited[curr]:
                visited[curr] = True
                # 移动到当前书本“本该去”的那个索引位置
                curr = arr[curr]
                cycle_len += 1
            
            # 如果环长度为 L，需要 L-1 次交换
            if cycle_len > 1:
                ans += (cycle_len - 1)
                
    print(ans)
