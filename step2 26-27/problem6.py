n, m = map(int, input().split())

solution = [list(map(int, input().split())) for _ in range(n)]
original = [list(map(int, input().split())) for _ in range(n)]

colors = set()
for row in original:
    for x in row:
        if x != 0:
            colors.add(x)

if not colors:
    print(0.0)
    exit()

total = 0

for color in colors:
    orig_count = 0
    sol_count = 0
    intersection = 0

    for i in range(n):
        for j in range(m):
            if original[i][j] == color:
                orig_count += 1
            if solution[i][j] == color:
                sol_count += 1
            if original[i][j] == color and solution[i][j] == color:
                intersection += 1

    union = orig_count + sol_count - intersection

    if union > 0:
        total += intersection / union

answer = total / len(colors)

print(round(answer, 2))
