"""Hello World and it's Citizens.
I will attempt to make a program that can do Fibonacci sequence of any given two numbers.
Wish me luck for I will a lot."""

num_1 = int(input("Please input a number: "))
num_2 = int(input("Please input another number: "))

choice_num = list(range(num_1, num_2))

print(choice_num)

result = list()

n = choice_num[-1]

def fib():
    while i != n:
    
        for i in range(choice_num):
            i = i + choice_num[i]
            result.append(i)

print(result)

print(n)

# Program to display the Fibonacci sequence up to n-th term

nterms = int(input("How many terms? "))

# first two terms
n1, n2 = 0, 1
count = 0

# check if the number of terms is valid
if nterms <= 0:
   print("Please enter a positive integer")
# if there is only one term, return n1
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
# generate fibonacci sequence
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1
