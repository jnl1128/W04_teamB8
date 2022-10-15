# 피보나치 함수
import sys
input = sys.stdin.readline
print = sys.stdout.write

T = int(input())
dp = [[0, 0] for _ in range(41)]
dp[0] = [1,0]
dp[1] = [0,1]


def fibo(n):
    if dp[n] != [0, 0]:
        return dp[n]
    one = fibo(n-1)
    two = fibo(n-2)
    dp[n][0] += one[0] + two[0]
    dp[n][1] += one[1] + two[1]
    return dp[n]

for _ in range(T):
    N = int(input())
    zero, one = fibo(N)
    print(f'{zero} {one}\n')