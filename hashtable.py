# 入力
words = list(input().split())

# 空の辞書を作成
d = {}
for word in words:
    if word in d:
        d[word] += 1
    else:
        d[word] = 1
        
max_word = max(d, key=d.get)
print(max_word)