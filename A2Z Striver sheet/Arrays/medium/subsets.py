# approach : basically we are going to use recursion (backtracking)
# we are going to have have 2 choices , either choose it or leave it
# suppose we have some List like : [3,1,2]
# and we want an output : [[], [1], [1, 2], [2], [3], [3, 1], [3, 1, 2], [3, 2]]
# so lets get started :
def sub(idx , base: list[int] , given: list[int] , output : list[list[int]] , sizee ):
  if(idx == sizee):
    output.append(base.copy())
    return
  base.append(given[idx])
  sub(idx+1 , base , given , output , sizee)
  base.pop()
  sub(idx+1 , base , given , output , sizee)


input = [3,1,2]
output = []
base = []
n = len(input)
sub(0,base,input,output,n)
output.sort()
print(output)