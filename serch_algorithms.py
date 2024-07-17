
#線形探索（ソートされている必要なし、重複なし）
def linear_serch(n,target):
    for i in range(len(n)):
        if target == n[i]:
            return i
    return -1

#二分探索（ソートされている必要あり、重複なし）
def binary_serch(n,target):
    l = 0
    r = len(n)-1
    m = 0
    
    while l <= r:
        m = ( l + r )//2
        if n[m] < target:
            l = m + 1
        elif n[m] > target:
            r = m - 1
        else:
            return m
    return -1
