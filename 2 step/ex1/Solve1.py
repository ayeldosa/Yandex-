import bisect

N = int(input())
A = []
B = []
for _ in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

M = int(input())
students = [int(input()) for _ in range(M)]

for c in students:
    pos = bisect.bisect_right(A, c)

    wait = 0

    if pos > 0 and A[pos - 1] <= c < B[pos - 1]:
        wait = B[pos - 1] - c
    else:
        wait = 0

    print(wait)
