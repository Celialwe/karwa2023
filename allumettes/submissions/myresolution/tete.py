n, k = list(map(int, input().split()))
print("Aymeric" if n % (k + 1) == 0 else "Brieuc")