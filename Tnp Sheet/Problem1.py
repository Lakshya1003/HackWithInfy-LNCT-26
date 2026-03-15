"""
Problem 1: Maximum Non-Adjacent Same Dish

Ramu has N dishes of different types arranged in a row: A1,A2,…,AN where Ai denotes the type of the ith dish. He wants to choose as many dishes as possible from the given list but while sa sfying two conditions:
•	He can choose only one type of dish.
•	No two chosen dishes should be adjacent to each other.
Ramu wants to know which type of dish he should choose from, so he can pick the maximum number of dishes.
If multiple types give the same maximum count, return the smallest dish type.
Example
Input
N = 9
A = [1,2,2,1,2,1,1,1,1]

Output
1
Explanation:
For type 1 , Ramu can choose at most four dishes. One of the ways to choose four dishes of type 1 is A1,A4, A7 and A9.
For type 2 , Ramu can choose at most two dishes. One way is to choose A3 and A5.
So in this case, Ramu should go for type 1 , in which he can pick more dishes.
So answer = 1.

INPUT FORMAT:
•	The first line contains T, the number of test cases. Then the test cases follow.
•	For each test casem the first line contains a single integer N.
•	The second line contains N integers A1, A2, … AN.

OUTPUT FORMAT:
For each test case, print a single line containing one integer – the type of the dish that Ramu should choose from. If there are multiple answers, print the smallest one.
"""


# so basically we gonna first do the hashing for every element , and then we gonna take out the min element with decent max frequency we consider it as main
# but if our min element have very less freqnecy then we will approach the next max element


def fun(dish : list[int]):
  uni = []
  freq = []
  for i in dish :
    if i not in uni:
      uni.append(i)
      freq.append(1)

    else:
      temp = uni.index(i)
      freq[temp] += 1

  minel = uni[0]
  maxfre = freq[0]


  for i in range(len(uni)):
    if(uni[i] < minel):
      if(freq[i] > maxfre):
        minel = uni[i]
        maxfre = freq[i]

  count = 0

  minelidx = []
  if(dish[0] == minel):
    minelidx.append(0)

  for i in range(1, len(dish)):
    if(dish[i] == minel):
      if(dish[i] != dish[i-1]) and ((i+1 != len(dish) ) and (dish[i] != dish[i+1])):
        if i -1 not in minelidx :
          minelidx.append(i)

      elif (dish[i] == dish[i-1]) and ((i+1 != len(dish) ) and (dish[i] == dish[i+1])):
        if i -1 not in minelidx :
          minelidx.append(i)
    if(i+1 == len(dish)):
      if(dish[i] == minel):
        if i - 1 not in minelidx:
          minelidx.append(i)



  return minelidx




dish = [1,2,2,1,2,1,2,1,1,1,1]
print(fun(dish))






