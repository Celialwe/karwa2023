from bisect import bisect_left

s = input().split()
n, k = int(s[0]), int(s[1])

l = input().split()
l = list(map(int, l))

def binarySearch(l, start, end, k) :
    mid = (start + end) // 2
    if start - end == 1 or start - end == 0:
        return False
    if l[mid] == k:
        return True
    elif l[mid] < k:
        return binarySearch(l, start, mid - 1, k)
    else:
        return binarySearch(l, mid + 1, end,  k)
    
for i in range(n):
    if l[i] >= k :
        break
    if binarySearch(l, i + 1, n-1,  k - l[i]):
        print("yes")
        exit()

print("no")
