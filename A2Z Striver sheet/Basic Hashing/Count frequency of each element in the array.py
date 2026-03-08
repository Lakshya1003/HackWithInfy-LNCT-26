nums = [1,2,1,3,4,5,1,2,3,6,1]

uni = []
freq = []
for i in nums:
  if i not in uni:
    uni.append(i)
    freq.append(1)
  else:
    freq[freq.index(i)] += 1

for i in range(len(uni)):
  print(f"element : {uni[i]} and its freqency if {freq[i]}")