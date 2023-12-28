# グラフの各頂点の最短移動距離問題に使える幅優先探索
# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_11_C&lang=ja

from collections import deque

# 入力
n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]

# 繋がっている頂点のリストを作成
connect = [[] for _ in range(n+1)]
for i in range(n):
    for j in data[i][2:]:
        connect[data[i][0]].append(j)
        connect[j].append(data[i][0])
        
# 距離を記録するリスト
distances = [-1] * (n+1)  # 未訪問は-1とする
distances[1] = 0  # スタート地点の確定

# 次に探索する頂点の情報を保存するための筒を用意
que = deque([1])

# 幅優先探索開始
while que:
    now = que.popleft()  # queから現在の頂点を取り出す
    for to in connect[now]:  # 現在の頂点と繋がっている頂点について調べる
        if distances[to] == -1:  # 未訪問の場合
            distances[to] = distances[now] + 1
            que.append(to)

# 各頂点の最短距離を出力
for i in range(1, n+1):
    print(i, distances[i])


# 迷路の最短経路問題に使える幅優先探索
# https://atcoder.jp/contests/abc007/tasks/abc007_3

from collections import deque

# 入力
r, c = map(int, input().split())  # マスの大きさ
sy, sx = map(int, input().split())  # スタート地点の座標
sy, sx = sy - 1, sx - 1  # 1ベースから0ベースに
gy, gx = map(int, input().split())  # ゴール地点の座標
gy, gx = gy - 1, gx - 1  # 1ベースから0ベースに
board = [input() for _ in range(r)]  # 迷路の盤面

# 最短距離の情報
dist = [[-1] * c for _ in range(r)]  # 未訪問の座標は-1とする

# 移動範囲を定義
dy = [1, -1, 0, 0]
dx = [0, 0, -1, 1]

# 次に探索する座標情報を保存するための筒
que = deque()  # dequeを用いることで計算量を削減

# スタート地点を確定
dist[sy][sx] = 0
que.append((sy, sx))

# 幅優先探索開始
while que:
    y, x = que.popleft()  # 筒から現在の座標情報を取り出す
    for i in range(4):
        next_y = y + dy[i]  # 次に進む座標の定義
        next_x = x + dx[i]
        if 0 <= next_y <= r and 0 <= next_x <= c and board[next_y][next_x] == '.':  # 迷路の枠内かつ次の座標が壁でないか
            if dist[next_y][next_x] == -1:  # 未訪問のマスかどうかの確認
                dist[next_y][next_x] = dist[y][x] + 1  # 未訪問であればその座標を訪問済みにする
                que.append((next_y, next_x))  # 次の座標として筒に追加

# ゴール地点の情報を出力
print(dist[gy][gx])