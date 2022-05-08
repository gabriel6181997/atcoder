# https://atcoder.jp/contests/abc042/tasks/abc042_b

# B - 文字列大好きいろはちゃんイージー

N, L = map(int, input().split())
S = [input() for i in range(N)]
print(*sorted(S), sep="")
