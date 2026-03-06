num = 64
divisors = []
te = num ** (1/2)
for i in range(1,int(te)+1):
  if num % i == 0:
    divisors.append(i)
    if (num / i) not in divisors:
      divisors.append(num/i)

print(divisors)

