def recu(n):
  if(n == 0):
    return
  if(n >= 1):
    print("Hello Stranger")
  recu(n-1)


a = 5
recu(a)