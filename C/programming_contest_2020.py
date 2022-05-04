N, K, S = map(int, input().split())
N = 3   # [0,1,2]

new_list = [x+1 for x in range(N)]

# https://atcoder.jp/contests/keyence2020/tasks/keyence2020_c?lang=ja

# 4 2 3
   # [1,2,3,4]
   # 4 は配列にある数字の数
   # 隣にある数字を足したらSになる (Sは和の条件)
   # KはSの組み合わせ

for i in range(N):
  for j in range(N):

    for k in range(N):
      if i == j or j == k or k == i:
        continue
  # # s = len(N)
  # print(str(i))
