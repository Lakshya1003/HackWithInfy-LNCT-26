def recu(n):
    if n == 1:
        return 1
    return n + recu(n-1)

a = 20
print(recu(a))