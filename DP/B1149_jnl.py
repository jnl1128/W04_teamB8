# RGB거리
import sys
input = sys.stdin.readline
print = sys.stdout.write

N = int(input()) # 집의 수
homes = []
for _ in range(N):
    homes.append(list(map(int, input().split(' '))))
