"""Hello World and it's Citizens.
I will attempt to make a program that can do Fibonacci sequence of any given two numbers.
Wish me luck for I will a lot."""

num = int(input("Please input the number of terms: "))

nums = list(range(0, num+1))

print(nums)

result = list()

for i in nums:
    new_num = i
    result.append(new_num)
    nums.remove(i-1)

print(result)