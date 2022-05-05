# B - ボウリングゲーム

# https://atcoder.jp/contests/code-formula-2014-quala/tasks/code_formula_2014_qualA_b

a,b = map(int,input().split())
p = list(map(int,input().split()))
q = list(map(int,input().split()))
pin = ["x"]*10
for i in p:
  pin[i-1] = "."
for i in q:
  pin[i-1] = "o"
print(*pin[6:10])
print(*pin[3:6])
print(*pin[1:3])
print(pin[0])
