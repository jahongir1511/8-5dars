#   https://www.codewars.com/kata/56e56756404bb1c950000992/train/python


import math


def sum_differences_between_products_and_LCMs(pairs):
    total_savings = 0

    for pair in pairs:
        a, b = pair

        if a == 0 or b == 0:
            lcm = 0
        else:
            gcd = math.gcd(a, b)
            lcm = (a * b) // gcd

        product = a * b
        savings = product - lcm
        total_savings += savings

    return total_savings

