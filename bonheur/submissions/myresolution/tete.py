k = list(map(int, input().split()))[1]
l = list(map(int, input().split()))

left, right = 0, len(l) - 1
s = l[left] + l[right]
while left < right and s != k:
    s = l[left] + l[right]
    if s < k:
        left += 1
    elif s > k:
        right -= 1

print("yes" if s == k else "no")
