'''
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5V4A46AdIDFAWu
'''

import sys
sys.stdin = open('sample_input.txt', 'r')

def main():
    T = int(input())

    for test_case in range(1, T+1):
        N, M, C = map(int, input().split())
        arr = [list(map(int, input().split())) for _ in range(0, N)]

    honey_sum = 0
    visited = [[0] * N for _ in range(N)]

    for i in range(0, N):
        for j in range(0, N):
            arr[i]

#1 visited를 이용한 나머지 case에서 찾기
# 행에서 M개의 조합에서 C보다 작은 case 중 최대 일경우
# 채취 가능 visited 행의 앞 뒤로 N개의 인덱스가 존재한지
