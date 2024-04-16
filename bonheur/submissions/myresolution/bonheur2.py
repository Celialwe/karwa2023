
s = input().split()
n, k = int(s[0]), int(s[1])

l = input().split()
l = list(map(int, l))

s = set()

for elem in l:
    if k - elem in s:
        print("yes")
        exit()
    s.add(elem)

print("no")