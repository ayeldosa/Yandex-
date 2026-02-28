import sys
from collections import OrderedDict


def ints():
    for line in sys.stdin.buffer:
        for token in line.split():
            yield int(token)


def main():
    it = ints()

    try:
        n = next(it)
        k = next(it)
    except StopIteration:
        print(0)
        return

    if n <= 0 or k <= 0:
        print(0)
        return

    last_pos = OrderedDict()
    left = 0
    best = 0

    for i in range(n):
        try:
            x = next(it)
        except StopIteration:
            break

        if x in last_pos:
            del last_pos[x]
        last_pos[x] = i

        if len(last_pos) > k:
            _, pos = last_pos.popitem(last=False)
            left = pos + 1

        cur_len = i - left + 1
        if cur_len > best:
            best = cur_len

    print(best)

if __name__ == "__main__":
    main()
