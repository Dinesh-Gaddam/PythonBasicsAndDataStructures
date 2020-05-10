
#Fibonacci get the next number in the sequence by adding the two previous numbers. Here is an example of the sequence:

#0,1,1,2,3,5,8,13,21,34...


def getFib(position) :
  if (position == 0) : return 0; 
  if (position == 1) : return 1; 
  first = 0,
  second = 1,
  next = first + second;
  i=2
  for i in i < position:
    first = second;
    second = next;
    next = first + second;  
  return next;

#Recursive 
def get_fib(position,first=0,second=1,startPosition=2):
    if (position == 0) : return 0; 
    if (position == 1) : return 1; 
        
    next = first + second
    
    if startPosition < position:
        return ( get_fib(position,second,next,startPosition+ 1))
    else:
        return next
   
#Optimized 

def get_fib(position):
    if position == 0 or position == 1:
        return position
    return get_fib(position - 1) + get_fib(position - 2)

"""
You may have noticed that this solution will compute the values of some inputs more than once.
For example get_fib(4) calls get_fib(3) and get_fib(2), get_fib(3) calls get_fib(2) and get_fib(1) etc. 
The number of recursive calls grows exponentially with n.
In practice if we were to use recursion to solve this problem we should use a hash table to store and fetch previously calculated results. 
This will increase the space needed but will drastically improve the runtime efficiency.

"""

# Test cases
print (get_fib(9))
print (get_fib(11))
print (get_fib(0))