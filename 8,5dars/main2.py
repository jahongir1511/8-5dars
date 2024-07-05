#        https://www.codewars.com/kata/57a4a3e653ba3346bc000810/train/python


def describeList(lst):
    if len(lst) == 0:
        return "empty"
    elif len(lst) == 1:
        return "singleton"
    else:
        return "longer"
