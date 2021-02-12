def calculate_without_recursion(n,x):
    # x = 2 #assumed
    sum = 0
    for i in range(1,n+1):
         sum += 1/x**i
    return sum

def calculate_with_recursion(n): #denominator is assumed 2 here can also be passes using the arguement
    if n == 1 or n <= 0:
        return 1/2
    sum = 1/2**n + calculate_with_recursion(n-1,)
    return sum

def series(n):
    for i in range(1,n+1):
        if i%2 :
            print(i**2+1, end = ' ')
        else:
            print(i**2-1, end = ' ')

if __name__ == "__main__":
    print("Problem 1")
    calculate_without_recursion(4,2)

    f = calculate_with_recursion(4)
    print(f)

    print("Problem 2")
    series(9)

    print("Problem 3")
    print("Enter 4 space separated numbers for problem 3")
    x,y,a,b =  [int(i) for i in input().split()]
    print( (((x+1/y)**a) * (1-(1/y))**b) /  (((y+1/x)**a)*((y-1/x)**b))  )
