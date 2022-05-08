# https://atcoder.jp/contests/abc058/tasks/abc058_b

#B - ∵∴∵

O = input()
E = input()+" "
ans = []
for i, j in zip(O,E): # zip(): forループの中で複数のイテラブルオブジェクト（リストやタプルなど）の要素を同時に取得する際に使う
    ans.append(i)
    ans.append(j)
print(*ans, sep="")
