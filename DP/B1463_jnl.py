# 1로 만들기 #재귀
import sys
input = sys.stdin.readline
print = sys.stdout.write

N = int(input())
dp = {1:0, 2:1, 3:1}
def makeOne(n):
    if n not in dp:
        dp[n] = 1 + min(makeOne(n//2)+n%2, makeOne(n//3)+n%3)
    return dp[n]
print(f'{makeOne(N)}')

# 1로 만들기 #반복
N = int(input())
dp = [0 for  _ in range(N+1)]
if N>=2:
    dp[2] = 1
if N>=3:
    dp[3] = 1
def makeOne():
    for i in range(4, N+1):
        dp[i] = 1 + min(dp[i//2] + i%2, dp[i//3] + i%3)
    return dp[N]
print(f'{makeOne()}')