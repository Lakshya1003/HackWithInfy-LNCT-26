def recu(n):
  if(n == 0):
    return
  if(n >= 1):
    print(n)
  recu(n-1)


a = 5
recu(a)