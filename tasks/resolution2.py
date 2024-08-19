f = open('17-1.txt')
s = f.readlines()
maxx = 0
count = 0
vm = 500
for i in range(len(s)):
    for j in range(i + 1, len(s)):
        a = int(s[i]) + int(s[j])
        if a <= vm:
            count += 1
        if a >= maxx:
            maxx = a
print(count, maxx)

