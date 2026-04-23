import os
import sys

# 请在此输入您的代码

# 放宽递归深度限制（虽然最多 18 层，加个保险）
sys.setrecursionlimit(2000)

def solve():
    # 快速读取输入数据
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N_str = input_data[0]
    A = int(input_data[1])
    B = int(input_data[2])
    
    # 记忆化字典，用于保存已经计算过的状态结果
    memo = {}
    
    # dfs(idx, a, b) 返回：从第 idx 位开始，拥有 a 个操作1，b 个操作2 时能生成的最大后缀字符串
    def dfs(idx, a, b):
        # 边界条件：如果所有数字都处理完了，返回空字符串
        if idx == len(N_str):
            return ""
            
        # 如果当前状态已经计算过，直接返回答案
        if (idx, a, b) in memo:
            return memo[(idx, a, b)]
            
        d = int(N_str[idx])
        
        # 贪心：从 9 往下遍历，尝试让当前数字变成最大的 v
        for v in range(9, -1, -1):
            # 计算变成 v 需要消耗的代价
            cost_a = (v - d) % 10
            cost_b = (d - v) % 10
            
            can_a = a >= cost_a
            can_b = b >= cost_b
            
            # 只要有一种方式能达到当前的 v
            if can_a or can_b:
                candidates = []
                
                # 分支 1：使用操作 1
                if can_a:
                    candidates.append(str(v) + dfs(idx + 1, a - cost_a, b))
                    
                # 分支 2：使用操作 2
                if can_b:
                    candidates.append(str(v) + dfs(idx + 1, a, b - cost_b))
                
                # 从有效分支中选取能够组成最大数字的那条路径
                # 字符串比较在这里等同于数值大小比较（因为长度总是相同的）
                best_res = max(candidates)
                
                # 记录进备忘录
                memo[(idx, a, b)] = best_res
                
                # 核心剪枝：因为我们是从 9 往下找的，只要找到了能达到的最大 v，
                # 任何更小的 v 组成的数字绝对比不过当前选 v 组成的数字，直接 break！
                break
                
        return memo[(idx, a, b)]

    # 从第 0 位开始，传入初始的 A 和 B
    ans = dfs(0, A, B)
    print(ans)

if __name__ == '__main__':
    solve()