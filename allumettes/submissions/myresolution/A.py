
n, k = map(int, input().split())


def gagne(n, k, nom):
    if n <= k:
        if nom == "A":
            return False
        else:
            return True
    else:
        if nom == "A":
            name == "B"
        else:
            name = "A"
        for i in range(1, k + 1):
            if not gagne(n - i, k, name):
                return False

b = gagne(a)