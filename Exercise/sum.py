# Given two integer numbers return their product only if the product is greater than 1000, else return their sum.



def function(number1, number2):
    product = number1 * number2
    if product <= 1000:
        return product
    else:
        return number1 + number2


result = function(20,60)
print(result)
result = function(20,30)
print(result)

