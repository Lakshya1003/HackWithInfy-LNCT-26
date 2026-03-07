def recu(cur,n):
  if cur > n:
    return
  print(cur)
  recu(cur+1,n)

a = 10
recu(1,a)