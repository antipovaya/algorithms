# Быстрая сортировка


def quck_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i < pivot]
        great = [i for i in arr[1:] if i > pivot]
        return quck_sort(less) + [pivot] + quck_sort(great)

print(quck_sort([10, 88, 1, 2, 22, 6]))


# если для алгоритма бастрой сортировки выбирать слчайный элемент,
# то среднее время выполнения составит O(n*log(n))
from random import randint


def quck_sort2(arr):
    if len(arr) < 2:
        return arr
    else:
        # Генерируем случайный индекс внутри функции
        random_el = randint(0, len(arr) - 1)
        pivot = arr[random_el]

        # Разделяем массив на элементы меньше, равные и больше опорного
        less = [i for i in arr if i < pivot]
        equal = [i for i in arr if i == pivot]
        great = [i for i in arr if i > pivot]

        # Рекурсивно сортируем и объединяем
        return quck_sort(less) + equal + quck_sort(great)


arr = [10, 88, 1, 2, 22, 6]
print(quck_sort2(arr))  # [1, 2, 6, 10, 22, 88]
import timeit
import random


def quck_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        random_el = random.randint(0, len(arr) - 1)
        pivot = arr[random_el]
        less = [i for i in arr if i < pivot]
        equal = [i for i in arr if i == pivot]
        great = [i for i in arr if i > pivot]
        return quck_sort(less) + equal + quck_sort(great)


# Тестируем на разных размерах данных
sizes = [100, 1000, 5000]
for size in sizes:
    test_data = [random.randint(0, 1000) for _ in range(size)]

    # Замер времени выполнения
    time_taken = timeit.timeit(lambda: quck_sort(test_data.copy()), number=1)
    print(f"1 функция: Размер массива: {size}, Время: {time_taken:.6f} секунд")
    time_taken = timeit.timeit(lambda: quck_sort2(test_data.copy()), number=1)
    print(f"2 функция: Размер массива: {size}, Время: {time_taken:.6f} секунд")