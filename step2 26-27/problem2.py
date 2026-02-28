import sys


def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n = data[0]
    a = data[1:1 + n]

    need = 0
    for i in range(1, n):
        if a[i] < a[i - 1]:
            need += a[i - 1] - a[i]

    print("YES" if need <= a[0] else "NO")

if __name__ == "__main__":
    solve()
