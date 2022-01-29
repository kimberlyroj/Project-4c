#Author: Kimberly Rojas
#GitHub username: kimberlyroj
#Date: 1/19/2021
#Description:A function named hailstone that takes a positive integer parameter as the initial number of a hailstone sequence and returns how many steps it takes to reach 1
def hailstone(num):
    count = 1
    """Print the terms of 'hailstone sequence' from n to 1."""
    assert num > 0
    print(num)
    if num > 1:
        if num % 2 == 0:
            count += hailstone(num / 2)
        else:
            count += hailstone((num * 3) + 1)
    return count

result = hailstone(10)
print(result)