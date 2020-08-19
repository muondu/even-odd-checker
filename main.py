import time
# input1 = int(input("Enter a number: "))
# def even_odd(number = input1):
#     """Dock strings"""
#     if input1 % 2 == 0:
#          even = print("The number is even")
#          return even
#     else:
#         odd = print("The number is odd")
#         return odd
# print(even_odd())

def take_input():
    """Input taken"""
    global input1
    input1 = int(input("Enter a number: "))
    return input1
take_input()
def is_even():
    if input1 % 2 == 0:
         even = print("The number is even")
         return even
    else:
        odd = print("The number is odd")
        return odd
is_even()