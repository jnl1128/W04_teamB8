# 가장 큰 증가 부분 수열
import sys, copy
input = sys.stdin.readline
print = sys.stdout.write

N = int(input())
A = list(map(int, input().split(' ')))
dp = copy.deepcopy(A)
for i in range(1, N):
    for j in range(i):
        if A[i] > A[j]:
            dp[i] = max(dp[i], dp[j]+A[i])
            # dp[i] += A[j] # 틀렸습니다.
print(f'{max(dp)}')
