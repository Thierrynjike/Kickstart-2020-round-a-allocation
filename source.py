N = int(input())
out = []
for i in range(N):
    n, b = list(map(int, input().split()))
    v = list(map(int, input().split()))
    v.sort()
    j, k = 0, 0
    while (j < len(v)):
        if (b - v[j] < 0):
            break
        else:
            b -= v[j]
            k += 1
            j += 1

    out.append(k)
for z in range(len(out)):
    print('Case #{}: {}'.format(z + 1, out[z]))