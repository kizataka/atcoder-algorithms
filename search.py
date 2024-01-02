# bit全探索
# lの要素を足し合わせてmになるかどうかを調べる関数
def search_bit(l, m):
    n = len(l)
    # bit全探索開始
    for bit in range(1 << n):  # 2進数を作成
        sum = 0
        for i in range(n):
            if bit & (1 << i):  # # 各桁が0か1かをシフト演算とアンド演算で確認する
                sum += l[i]  # 1であればその数字を使うということでsumに足し合わせる
        if sum == m:  # 合計が一致しているかどうかを確認
            return True
    return False