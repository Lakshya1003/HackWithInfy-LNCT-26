# approach : basically we are going to use recursion (backtracking)
# we are going to have have 2 choices , either choose it or leave it
# suppose we have some List like : [3,1,2]
# and we want an output : [0,1,2,3,3,4,5,6]
# so lets get started :
def sub(idx , sum , given: list[int] , output : list[list[int]] , sizee ):
  if(idx == sizee):
    output.append(sum)
    return

  sub(idx+1 , sum + given[idx] , given , output , sizee)
  sub(idx+1 , sum , given , output , sizee)


input = [3,1,2]
output = []
n = len(input)
sub(0,0,input,output,n)
output.sort()
print(output)
