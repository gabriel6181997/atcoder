# B - Maritozzo

# https://atcoder.jp/contests/abc219/tasks/abc219_b

S=[input() for i in range(3)]
T=input()
for i in range(len(T)):
    print(S[int(T[i])-1], end="")
