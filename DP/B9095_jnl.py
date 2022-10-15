# 1, 2, 3 더하기
import sys
input = sys.stdin.readline
print = sys.stdout.write

T = int(input())
dp = [0 for  _ in range(11)]
dp[1] = 1
dp[2] = 2
dp[3] = 4

def plus123(n):
    if n <=3:
        return dp[n]
    if dp[n] <= 0:
        dp[n] = plus123(n-1)+plus123(n-2)+plus123(n-3)
    return dp[n]

for _ in range(T):
    num = int(input())
    print(f'{plus123(num)}\n')
