# 지금 이 조합을 해봤는데여
# 그랫더니 n이 나왓습니다.
# 그걸 dp에 넣어주겟습니다.
# dp라는 리스트는 따라서 저장될 때 작은 인덱스부터 채워질 것입니다.
# 동전
import sys
input = sys.stdin.readline
print = sys.stdout.write


T = int(input())
for _ in range(T):
    N = int(input())
    coins = list(map(int, input().split(' ')))
    M = int(input())
    dp = [0 for _ in range(M+1)]
    dp[0] = 1 # dp[0]이 사용되는 경우는 i == coin일 경우이기 때문이다.
    
    for coin in coins:
        for i in range(1, M+1):
            if i >= coin:
                dp[i] = dp[i] + dp[i-coin]    
    print(f'{dp[M]}\n')
