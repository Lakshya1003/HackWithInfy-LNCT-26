num = 12345
tens = 10
t = num
ans = 0
while(t != 0):
  temp = t % 10
  ans = ans * 10 + temp
  t //= 10


print(ans)