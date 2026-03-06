num = 112211
re = str(num)
revre = ""
for i in range(len(re)):
  revre += re[len(re) - 1 - i]


pali = True
for i in range(len(re)):
  if(re[i] != revre[i]):
    print("Not a palindrome")
    pali = False
    break
if(pali):
  print("yes it is a palindorme")
