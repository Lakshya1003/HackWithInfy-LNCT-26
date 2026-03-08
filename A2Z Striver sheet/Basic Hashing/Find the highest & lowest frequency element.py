nums = [1,2,1,3,4,5,1,2,3,6,1]
uni = []
freq = []
for i in nums:
  if i not in uni:
    uni.append(i)
    freq.append(1)
  else:
    freq[freq.index(i)] += 1

maxfre = max(freq)
maifre = min(freq)

for i in range(len(uni)):
  if freq[i] == maxfre:
    print(f"element : {uni[i]} and its freqency if {freq[i]}")
  if freq[i] == maifre:
    print(f"element : {uni[i]} and its freqency if {freq[i]}")