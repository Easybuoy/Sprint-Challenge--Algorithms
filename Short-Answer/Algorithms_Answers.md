#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)
1 -> O(c)
2 -> O(n ^ 3)
3 -> O(c)
Runtime complexity = O(n^3)

b)
1 -> O(c)
2 -> O(n)
3 -> O(c)
4 -> O(c * n)
5 -> O(c)
6 -> O(c)
Runtime complexity = O(n^2)

c)
1 -> O(c)
2 -> O(c)
3 -> O(c + n)
Runtime complexity = O(n)

## Exercise II
Get number of floors => n
Get middle of floors => n / 2
Throw egg on middle floor
if egg breaks, move down and throw egg again 
return last floor the egg breaks

if egg does not break, go up and throw egg
return the floor the egg breaks

Runtime complexity = O(n)
