# https://atcoder.jp/contests/abc148/tasks/abc148_b

# B- Strings with the Same Length

N = int(input())
S, T = input().split()
for i in range(N):
  word = S[i] + T[i]
  print(word, end='')
