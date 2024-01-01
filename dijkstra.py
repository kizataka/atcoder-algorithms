import heapq

def dijkstra(graph, V, start):
    INF = float('inf')
    dist = [INF] * V  # 初期状態ではすべての頂点の距離が無限大として設定する
    dist[start] = 0  # 始点の距離は0
    queue = [(0, start)]  # 優先度付きキューの使用

    while queue:  # キューが空になるまで繰り返し
        d, v = heapq.heappop(queue)  # キューから最小の距離を持つ頂点を取り出す
        if dist[v] < d:
            continue
        for u, cost in graph[v]:
            if dist[v] + cost < dist[u]:
                dist[u] = dist[v] + cost  # 距離を更新
                heapq.heappush(queue, (dist[u], u))  # 優先度付きキューに追加

    return dist