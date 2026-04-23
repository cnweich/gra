import os
import sys

# 请在此输入您的代码

def solve():
    # 使用 sys.stdin.read 一次性读取全部数据，加速 I/O
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    # 提取所有操作区间
    ops = []
    idx = 2
    for _ in range(m):
        ops.append((int(input_data[idx]), int(input_data[idx+1])))
        idx += 2
        
    # 1. 差分数组计算“全量执行”后的库存
    diff = [0] * (n + 2)
    for L, R in ops:
        diff[L] += 1
        diff[R + 1] -= 1
        
    inventory = [0] * (n + 1)
    base_zero_count = 0  # 记录全量执行后，库存本来就是 0 的商品种类数
    is_one = [0] * (n + 1) # 标记库存是否恰好为 1
    
    for i in range(1, n + 1):
        inventory[i] = inventory[i - 1] + diff[i]
        if inventory[i] == 0:
            base_zero_count += 1
        elif inventory[i] == 1:
            is_one[i] = 1  # 脆弱点：库存为 1
            
    # 2. 对“脆弱点”建立前缀和数组，以便 O(1) 查询区间内 1 的个数
    prefix_ones = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix_ones[i] = prefix_ones[i - 1] + is_one[i]
        
    # 3. 针对每个操作计算不执行它的后果
    for L, R in ops:
        # 区间内原库存为 1 的数量
        new_zeros = prefix_ones[R] - prefix_ones[L - 1]
        
        # 最终 0 的数量 = 基础 0 的数量 + 新增的 0 数量
        print(base_zero_count + new_zeros)

if __name__ == '__main__':
    solve()
