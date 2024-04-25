t = int(input())
for _ in range(t):
    s = input().upper()
    total = 0
    for i, char in enumerate(s):
        total += ord(char)
        if total > 270:
            print(len(s[:i+1]))
            break
    else:
        print("-1")
