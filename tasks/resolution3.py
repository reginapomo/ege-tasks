f = open('17-1.txt')
s = f.readlines()
minn = 10**10
count = 0
vmo = 300
vm = 30
for i in range(len(s)):
    for j in range(i + 1, len(s)):
        a = int(s[i]) + int(s[j])
        if a % 3 == 0:
            if int(s[i]) > vm and int(s[j]) > vm:
                if int(s[i]) <= vmo and int(s[j]) <= vmo:
                    count += 1
                    if a <= minn:
                        minn = a
print(count, minn)
