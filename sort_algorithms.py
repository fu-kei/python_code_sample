n=[int(i) for i in input().split()]

#挿入ソート（昇順）
def insert_sort(n): #引数 n:ソート対象リスト
    len_n=len(n) #リストの長さ取得
    for i in range(1,len_n):
        target=n[i] #挿入対象を指定
        j=i-1 #ソート済み範囲を取得
        while 0 <= j and target < n[j]: #配列内かつ、挿入対象よりソート済み範囲内の値が大きい場合
            n[j+1] = n[j]
            j-=1    
        n[j+1]=target
    return n

#バブルソート（昇順）
def bubble_sort(n): #引数 n:ソート対象リスト
    len_n=len(n) #リストの長さ取得
    for i in range(len_n-1):
        for j in range(len_n-i-1): 
            if n[j]>n[j+1]: #一つ後ろの値が現在位置の値より小さい場合
                n[j],n[j+1]=n[j+1],n[j] #値入れ替え
    return n
    
#選択ソート（昇順）   
def select_sort(n): #引数 n:ソート対象リスト
    len_n=len(n) #リストの長さ取得
    for i in range(len_n):
        min_idx=i #最小値インデックス初期化
        for j in range(i+1,len_n):
            if n[min_idx]>n[j]: #最小値インデックス探索
                min_idx=j #最小値インデックス上書き
        n[i],n[min_idx]=n[min_idx],n[i] #値入れ替え
    return n

#マージソート（昇順）
#def merge_sort_main(n) ソートのメイン関数　指示出し用　引数　n:ソートを対象リスト
#def merge_sort リストを分割し、mergeを呼び出す。　引数 target_list:ソート対象リスト,st_idx:ソートを始める位置,ed_idx:ソートを終える位置
#def merge 分割されたリストを結合していく。　引数　target_list:ソート対象リスト,st_idx:ソートを始める位置,mid_idx:ソート対象リストの中間位置,ed_idx:ソートを終える位置
def merge_sort_main(n): 
    start_idx=0
    end_idx=len(n)-1
    merge_sort(n,start_idx,end_idx)
    return n
        
def merge_sort(target_list,st_idx,ed_idx):
    #終了条件
    if not (st_idx < ed_idx):
        return
    
    #中央のインデックス
    mid_idx=(st_idx + ed_idx) // 2
    
    #左分割
    merge_sort(target_list,st_idx,mid_idx)
    #右分割
    merge_sort(target_list,mid_idx+1,ed_idx)
    #結合
    merge(target_list,st_idx,mid_idx,ed_idx)

def merge(target_list,st_idx,mid_idx,ed_idx):
    left_cp_list=target_list[st_idx:mid_idx+1]
    right_cp_list=target_list[mid_idx + 1:ed_idx+1]
    
    idx=st_idx
    left_idx=0
    right_idx=0
    left_cnt=len(left_cp_list)
    right_cnt=len(right_cp_list)
    
    while left_idx < left_cnt and right_idx < right_cnt:
        if left_cp_list[left_idx] <= right_cp_list[right_idx]:
            target_list[idx]=left_cp_list[left_idx]
            left_idx+=1
            idx+=1
        else:
            target_list[idx]=right_cp_list[right_idx]
            right_idx+=1
            idx+=1
        
    while left_idx < left_cnt:
        target_list[idx]=left_cp_list[left_idx]
        left_idx+=1
        idx+=1
            
    while right_idx < right_cnt:
        target_list[idx]=right_cp_list[right_idx]
        right_idx+=1
        idx+=1
