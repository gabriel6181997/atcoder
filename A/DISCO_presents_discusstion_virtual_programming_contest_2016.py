# https://atcoder.jp/contests/discovery2016-qual/tasks/discovery_2016_qual_a

# A - DISCO presents ディスカバリーチャンネルプログラミングコンテスト 2016

import math
W = int(input())
s = "DiscoPresentsDiscoveryChannelProgrammingContest2016"
for i in range(math.ceil(len(s)/W)): # math.ceil() method rounds a number UP to the nearest integer
    print(s[W*i:W+W*i])
