from unittest.mock import right


#Пример 1: 0(1) - Константная сложность
#Доступ к элементу списка по индексу
def get_element(lst, index):
    return lst[index]

lst = [1, 2, 3, 4, 5]
print(get_element(lst))


#пример 2
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 22, 43]
print(sum_of_numbers)



#пример 3
lst = [1, 2, 3]
def find_pairs(lst):
    pairs = []
    for i in range(len(lst)):
        for j in range(len(lst)):
            pairs.append((lst[i], lst[j]))
    return pairs

print(find_pairs(lst))

#пример 4
#
def binary_search(lst, target):
    left, right = 0, len(lst) - 1
    while left <= right:
        mid = (left + right)//2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:





