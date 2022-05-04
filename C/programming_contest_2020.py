
# https://atcoder.jp/contests/keyence2020/tasks/keyence2020_c?lang=ja

# Reference Ans:
# https://atcoder.jp/contests/keyence2020/submissions?f.Language=4006&f.LanguageName=Python3&f.Status=AC&f.Task=keyence2020_c&f.User=

import math

def main() -> None:
    n, k, s = map(int, input().split())

    mx = 10**9
    a = [s] * n
    for i in range(k, n):
        a[i] = (s + 1) % mx
    print(*a)


if __name__ == "__main__":
    main()
