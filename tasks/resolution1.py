f = open('17-1.txt')
s = f.readlines()
maxx = 0
minn = 10**10
for i in range(len(s)):
    for j in range(i + 1, len(s)):
        a = int(s[i]) + int(s[j])
        if a >= maxx:
            maxx = a
        if a <= minn:
            minn = a
print(maxx, minn)