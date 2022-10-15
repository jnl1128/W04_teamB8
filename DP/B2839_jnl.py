# 설탕 배달
import sys
input = sys.stdin.readline
print = sys.stdout.write

N = int(input())
dp = [0 for _ in range(N+1)]
if N >= 3:
    dp[3] = 1
if N>= 5:
    dp[5] = 1

def solution():
    for i in range(6, N+1):
        if i % 5 == 0:
            dp[i] = dp[i-5] + 1
        elif i % 3 == 0:
            dp[i] = dp[i-3] + 1
        else:
            if dp[i-3] != 0 and dp[i-5] != 0:
                dp[i] = min(dp[i-3]+1, dp[i-5]+1)
    if dp[N] == 0:
        return '-1'
    else:
        return str(dp[N])
        
print(solution())  
