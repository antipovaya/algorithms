# Сортировка выбором: О(n**2)

def find_small_el(arr):
    """ Функция производит поиск наименьшего значения и отдает его индекс """
    smallest = arr[0]
    smallest_index = 0
    for el in range(1, len(arr)):
        if arr[el] < smallest:
            smallest = arr[el]
            smallest_index = el
    return smallest_index

def selection_sort(arr):
    new_arr = []
    for i in range(len(arr)):
        smallest = find_small_el(arr)
        new_arr.append(arr.pop(smallest))
    return new_arr


print(selection_sort([22,3,5,90,3,1]))