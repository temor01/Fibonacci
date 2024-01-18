"""Hello World and it's Citizens.
I will attempt to make a program that can do Fibonacci sequence of any given two numbers.
Wish me luck for I will a lot."""

num = int(input("Please input the number of terms: "))

nums = list(range(0, num+1))

print(nums)

result = [0,]

while True:

    for i in range(len(nums)+1):

        if i != nums[-1]:
            new_num = nums[i] + nums[i+1]
            
            result.append(new_num)
            
            nums.remove(i)

        else:
            new_num = new_num + nums[i]

            result.append(new_num)

            nums.remove(i)

print(result)