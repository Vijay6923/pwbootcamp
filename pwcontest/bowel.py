
t = int(input())
for _ in range(t):
    n = int(input())  
    ans = 0
    generationmembers = 1  
    for i in range(1, n + 1):
        ans += generationmembers
        if i % 3 == 0:
            generationmembers *= 2

    print(ans)
