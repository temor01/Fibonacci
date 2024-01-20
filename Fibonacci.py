"""Hello World and it's Citizens.
I will attempt to make a program that can do Fibonacci sequence of any given two numbers.
Wish me luck for I will a lot."""

num = int(input("Please enter the number of terms: "))

def fibonacciSeries(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacciSeries(num-1) + fibonacciSeries(num-2)
    
n = int(input())
print("Fibonacci series:", end='')
for n in range(0, n):
    print(fibonacciSeries(n), end='')