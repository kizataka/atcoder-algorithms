# 深さ優先探索による探索時刻の記録の実装
# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_11_B&lang=ja

# 再帰回数の上限を設定
import sys
sys.setrecursionlimit(10**6)

# 入力
n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]

# 繋がっている頂点のリストを作成
connect = [[] for _ in range(n+1)]
for i in range(n):
    u = data[i][0]
    for v in data[i][2:]:
        connect[u].append(v)

time = 1
answer = [[0, 0] for _ in range(n+1)]  # 探索開始時刻と終了時刻を記録

# 深さ優先探索の関数を定義
def dfs(now):
    global time  # グローバル変数を定義
    answer[now][0] = time  # 探索開始時刻を記録
    time += 1
    for to in connect[now]:
        if answer[to][0] == 0:  # 未訪問の場合
            dfs(to)  # 再帰
    answer[now][1] = time  # 探索終了時刻を記録
    time += 1

# 深さ優先探索開始
for i in range(1, n+1):
    if answer[i][0] == 0:  # 未訪問の場合
        dfs(i)

# 答えを出力
for i in range(1, n+1):
    print(f"{i} {answer[i][0]} {answer[i][1]}")


# 深さ優先探索による移動経路の記録の実装
# https://atcoder.jp/contests/abc213/tasks/abc213_d
    
# 再帰回数の上限を設定
import sys
sys.setrecursionlimit(10**6)

# 入力
n=int(input())

# 道の情報格納リスト
connect=[[] for i in range(n+1)]

# 道の情報受け取り
for i in range(n-1):
    A,B=map(int, input().split())
    connect[A].append(B)
    connect[B].append(A)  # 無向グラフなので双方向の道を格納

# 小さい順に回るからソート
for i in range(n+1):
    connect[i].sort()

# 答えの格納用リスト
ans=[]

# 幅優先探索の関数を定義
def dfs(now,pre):  # nowは今いる町、preは前にいた町
    # 今いる町を答えに入れる
    ans.append(now)
    # to=今いる町から行ける町
    for to in connect[now]:
        # もしtoが前にいた町と違うなら
        if to!=pre:
            # 更に先へ探索する
            dfs(to,now)
            # 戻ってきたら答えへ格納
            ans.append(now)

# 最初の町=1,前にいた町=-1(前にいた町がないので便宜上-1)としてスタート
dfs(1,-1)

# 答えの出力
print(*ans)