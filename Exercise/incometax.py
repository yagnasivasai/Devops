income = input()

taxpayable = 0
print("Given income", income)

if income <= 100000:
    taxpayable = 0
elif income <= 200000:
    x = income - 100000
    taxpayable = x * 10/100
else:
    taxpayable = 100000 * 10/100
    taxpayable += (income - 200000) * 20/100

print("total tax pay", taxpayable)
