import timeit
import random

def generate_unique_numbers(n):
    numbers = list(range(1, n + 1))
    random.shuffle(numbers)
    return numbers

def timsort_sorted(array):
    return sorted(array)

def timsort_sort(array):
    a = array.copy()
    a.sort()
    return a

def insertion_sort(array):
    a = array.copy()
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a

def merge_sort(array):
    if len(array) <= 1:
        return array.copy()

    mid = len(array) // 2
    left_half = merge_sort(array[:mid])
    right_half = merge_sort(array[mid:])

    return merge(left_half, right_half)

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    merged.extend(left[left_index:])
    merged.extend(right[right_index:])
    return merged

def sorting_measurement(size):
    print(f"\nКількість елементів: {size}")
    data = generate_unique_numbers(size)

    time_sorted = timeit.timeit(lambda: timsort_sorted(data), number=3)
    print(f"Timsort (sorted): {time_sorted:.5f} сек")

    time_sort = timeit.timeit(lambda: timsort_sort(data), number=3)
    print(f"Timsort (list.sort): {time_sort:.5f} сек")

    time_merge = timeit.timeit(lambda: merge_sort(data), number=3)
    print(f"Merge sort: {time_merge:.5f} сек")

    if size <= 10000:  # Обмеження, бо insertion_sort довго працює
        time_insertion = timeit.timeit(lambda: insertion_sort(data), number=3)
        print(f"Insertion sort: {time_insertion:.5f} сек")
    else:
        print("Insertion sort: пропущено через велику кількість елементів")

if __name__ == "__main__":
    sorting_measurement(1000)
    sorting_measurement(10000)
    sorting_measurement(100000)
    sorting_measurement(1000000)
