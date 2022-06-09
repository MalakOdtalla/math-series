

def fibonacci(n):
    ''' Fun takes one parameter n, Then  return the nth value in the fibonacci serie that start with(integers 0 and 1), using recursion  '''
    if n <= 1:
        return n
    else:
        return (fibonacci(n - 1) + fibonacci(n - 2))


def lucas(n):
    ''' Fun takes one parameter n, Then  return the nth value in the lucas serie that start with(integers 2 and 1), using recursion  '''
    if (n == 0):
         return 2
    if (n == 1):
        return 1


    return lucas(n - 1) + lucas(n - 2)


def sum_series (n,num0=0,num1=1):
    ''' func with one required params that will determine which element in the series to print '''
    for i in range(n):
        num0, num1 = num1, num0 + num1
    return num0





# if __name__ == "__main__":
#       input=input("Enter num :    ")
#       print(fibonacci(int(input)))
#       print(lucas(int(input)))
#       print(sum_series(int(input)))