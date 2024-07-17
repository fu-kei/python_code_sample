def boyer_moore_serch(n,target):
    target_len=len(target)
    skip_table=make_skip_table(target,target_len)
    target_ed_idx = target_len - 1
    n_idx = target_len - 1
    while n_idx < len(n):
        target_idx = target_ed_idx
        while n[n_idx] == target[target_idx]:
            if target_idx == 0:
                return n_idx
            n_idx -=1
            target_idx -=1
        skip=max(skip_table.get(n[n_idx],target_len),target_len - target_idx)
        n_idx += skip
    
    return -1
        
    
def make_skip_table(target,target_len):
    skip_table=dict()
    for i ,ch in enumerate(target[:-1]):
        skip_table[ch]=target_len - i -1
    return skip_table