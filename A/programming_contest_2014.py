# https://atcoder.jp/contests/tenka1-2014-quala/tasks/tenka1_2014_qualA_a

# A - 天下一序数

l = [str(i) for i in range(1, 1001)] #strに変換すると、桁ごとにソートできるようになる
a = sorted(l)
for i in range(len(a)):
  print(a[i])
