num = 153
t = num
c = 0
nums = []
while(t != 0):
  nums.append(t%10)
  t = t // 10
  c += 1
sum = 0
for i in nums:
  sum += (i**c)

if sum == num :
  print("yes it is armstrong")

else:
  print("it is not armstrong number")