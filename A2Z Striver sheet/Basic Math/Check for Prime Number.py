import math

num = 41
is_prime = True

if num <= 1:
    is_prime = False
else:
    for i in range(2, int(math.sqrt(num)) + 1):
        if (num % i) == 0:
            is_prime = False
            break

if is_prime:
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")
