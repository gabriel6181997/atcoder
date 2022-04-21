# https://atcoder.jp/contests/abc069/tasks/abc069_b

# 問題文
# internationalization という英単語は、i18n と略されることがあります。 これは、先頭文字 i と末尾文字 n の間に 18 文字が挟まっていることに由来します。

# 長さ 3 以上の英小文字のみからなる文字列 s が与えられます。 同様の規則によって s を略してください。

# 制約
# 3≤∣s∣≤100 (ただし、∣s∣ は s の長さを表す。)
# s は英小文字のみからなる。

s = input()
s0 = s[0]
s_last = s[-1]
s_len = str(len(s) - 2)
ans = (s0+s_len+s_last)
print(ans)
