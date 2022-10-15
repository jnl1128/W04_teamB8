# 2xN 타일링
import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline
print = sys.stdout.write

N = int(input())
dp = [0 for _ in range(N+1)]
dp[1] = 1
dp[2] = 2

def tile(n):
    if n <= 2:
        return n
    if dp[n] > 0:
        return dp[n]
    dp[n] = (tile(n-1)%10007 + tile(n-2)%10007) % 10007
    return dp[n]
if N>=2:
    print(f'{tile(N)}')
else:
    print('1')
