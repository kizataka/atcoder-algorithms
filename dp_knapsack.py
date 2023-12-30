# 入力
n, w = map(int, input().split())  # nは品物の数、wはナップザックの容量

# 最大価値を示す表を作成
dp = [[0] * (w + 1) for i in range(n + 1)]

# 各品物についてループ
for i in range(1, n+1):
    vi, wi = map(int, input().split())  # 各品物の価値と重さを入力
    for w in range(w+1):
        if w - wi < 0:  # 容量が超える場合
            dp[i][w] = dp[i-1][w]  # i-1番目と同じ最大価値
        else:  # 容量が収まる場合
            dp[i][w] = max(dp[i-1][w], dp[i-1][w-wi] + vi) # i-1番目の最大価値または追加した最大価値の大きい方
            
# 最大価値の出力
print(dp[n][w])