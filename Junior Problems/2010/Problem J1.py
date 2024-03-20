n = int(input())

for i in range(n, 0, -1):
    if (i >= n / 2):
        if (n == i):
            print('%d는 %d입니다.' %(n, i))
        else:
            print('%d는 %d과(와) %d입니다.' %(n, i, n // i))
