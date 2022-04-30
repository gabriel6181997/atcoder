# https://atcoder.jp/contests/abc191/tasks/abc191_b

# B = Remove It

N, X = map(int, input().split())
A = list(map(int, input().split()))[:N] # 配列の中にある数字の数をN個に限定する
ans = list(filter((X).__ne__, A)) # filterでX以外の要素を取り出し、ansに格納
print(" ".join(map(str, ans))) # mapでansを文字列に変換し、printで出力



