# Given two int values, return their sum. Unless the two values are the same, then return double their sum.


def sum_double(a, b):
    sum = a + b
    print(sum)

    # if two are same double it
    if a == b:
        sum = sum * 2
        return sum


sum_double(2, 5)
sum_double(2, 2)

# Given an int n, return the absolute difference between n and 21, except return double the absolute difference if n is over 21.


def diff(n):
    if n <= 21:
        return 21-n
    else:
        return (n-21)*2


y = diff(25)
print(y)

## We have a loud talking parrot. The "hour" parameter is the current hour time in the range 0..23. We are in trouble if the parrot is talking and the hour is before 7 or after 20. Return True if we are in trouble.


def parrot_trouble(talking, hour):
    if talking == True and(hour > 7 or hour < 21):
        return True
    else:
        return False


##

