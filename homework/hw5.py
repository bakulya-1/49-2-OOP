#внутри написать любой алгоритм из уровней сложности Big (o) - Нотация
#O(log n) Логарифмическая сложность
#Бинарный поиск
#from unittest.mock import right
#from requests.packages import target


def binary_search(numbers, target):
    left, right = 0, len(numbers) - 1

    while left <= right:
        mid = (left + right)//2
        if numbers[mid] == target:
            return mid
        elif numbers[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return - 1

numbers = [1, 5, 7, 9, 12, 16, 18, 21, 23]
target = 16
result = binary_search(numbers, target)

if result:
    print(f"Число {target} найдено.")
else:
    print(f"Число {target} не найдено.")



