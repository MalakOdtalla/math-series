

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


def sum_series (nth,num0=0,num1=1):
    if nth ==True:
        return fibonacci(nth)
    elif (num0==2 and num1==1):
        return lucas(nth)
    else:
        return




#print(sum_series (7))




#if __name__ == "__main__":
 #     input=input("Enter num :    ")
  #    print(fibonacci(int(input)))