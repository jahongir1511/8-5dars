#      https://www.codewars.com/kata/56b4bae128644b5613000037/train/python


def repeat_sum(lists):
    num_count = {}

    for sublist in lists:
        seen = set()
        for num in sublist:
            if num not in seen:
                num_count[num] = num_count.get(num, 0) + 1
                seen.add(num)

    repeated_numbers = [num for num, count in num_count.items() if count >= 2]
    total_sum = sum(repeated_numbers)

    return total_sum

print(repeat_sum([[1, 2, 3], [2, 8, 9], [7, 123, 8]]))
print(repeat_sum([[1], [2], [3, 4, 4, 4], [123456789]]))
print(repeat_sum([[1, 8, 8], [8, 8, 8], [8, 8, 8, 1]]))

