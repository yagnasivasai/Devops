import sys

# x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(sys.getsizeof(x))
# print(sys.getsizeof(range(1,11)))
# for element in x:
#     print(element)
# for i in range(1,11):
#     print(i)

# y = map(lambda i: i**2, x)

# print(next(y))
# print(y.__next__)
# print("looping starting")

# for i in y:
#     print(i)

# # this while loop and for loop does the same thing

# while True:
#     try:
#         value = next(y)
#         print(value)
#     except StopIteration:
#         print("Done")
#         break


x = range(1, 11)

for ii in x:
    print(ii)
