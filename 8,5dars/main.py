#     https://www.codewars.com/kata/5aa20a964a6b34417c00008d/train/python


def find_page_number(pages):
    incorrect_pages = []
    for i in range(1, len(pages)):
        if pages[i] < pages[i - 1]:
            incorrect_pages.append(pages[i - 1])
    return incorrect_pages

page_list = [1, 2, 10, 3, 4, 5, 8, 6, 7]
incorrect_pages = find_page_number(page_list)
print(incorrect_pages)

print(find_page_number([50, 5, 51, 8, 40, 9]))  #
print(find_page_number([3000, 3, 8, 6, 100, 9, 40, 13]))
print(find_page_number([50, 5, 51, 8]))
print(find_page_number([4, 1, 26, 5, 6, 2]))



