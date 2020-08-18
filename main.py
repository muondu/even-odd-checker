import time
input1 = int(input("Enter a number: "))
def even_odd(number = input1):
    if input1 % 2 == 0:
         even = print("The number is even")
         return even
    else:
        odd = print("The number is odd")
        return odd
print(even_odd())
