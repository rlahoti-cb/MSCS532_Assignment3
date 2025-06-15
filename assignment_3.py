import random
import time

def quicksort_wrapper(i, strategy="random"):
    if not isinstance(i, list):
        return None
    if len(i) <= 1:
        return i.copy()
    
    ic = i.copy()
    quicksort(ic, 0, len(ic) - 1, strategy)
    return ic

def quicksort(i, l, h, strategy):
    while l < h:
        if strategy == "random":
            pivot_idx = random_partition(i, l, h)
        else:
            pivot_idx = first_element_partition(i, l, h)

        
        if pivot_idx - l < h - pivot_idx:
            quicksort(i, l, pivot_idx - 1, strategy)
            l = pivot_idx + 1
        else:
            quicksort(i, pivot_idx + 1, h, strategy)
            h = pivot_idx - 1

def random_partition(i, l, h):
    pivot_idx = random.randint(l, h)
    i[pivot_idx], i[h] = i[h], i[pivot_idx]
    return partition(i, l, h)

def first_element_partition(i, l, h):
    i[l], i[h] = i[h], i[l]
    return partition(i, l, h)

def partition(i, l, h):
    pivot = i[h]
    x = l - 1
    for y in range(l, h):
        if i[y] <= pivot:
            x = x + 1
            i[x], i[y] = i[y], i[x]
    i[x + 1], i[h] = i[h], i[x + 1]
    return x + 1

# generate random data based
def generate_random_data(size):
    out = [random.randint(0, size) for x in range(size)]
    return out

# generate sorted data based
def generate_sorted_data(size):
    out = list(range(size))
    return out

# generate reversed sorted data
def generate_reversed_sorted_data(size):
    out = list(range(size, 0, -1))
    return out

# generate random
def generate_repeated_data(size):
    num_replace = size // 2
    data = generate_sorted_data(size)
    random_value = data[random.randint(0, size - 1)]
    data[-num_replace:] = [random_value] * num_replace
    random.shuffle(data)
    return data

# checks that the quicksort algorithm 
def part_1_validation():
    sorted_array = generate_sorted_data(10)
    empty_array = []
    repeated_elements = generate_repeated_data(10)

    for array_type in (sorted_array, empty_array, repeated_elements):
        out = quicksort_wrapper(array_type, strategy="random")
        array_type.sort()
        if array_type != out:
            print("part 1 validation failed")

def part_1_comparison():
    data_size = 10000

    random_data = generate_random_data(data_size)
    sorted_data = generate_sorted_data(data_size)
    reversed_sorted_data = generate_reversed_sorted_data(data_size)
    repeated_data = generate_repeated_data(data_size)

    # randomized quicksort on random data
    start_time = time.time()
    quicksort_wrapper(random_data, strategy="random")
    end_time = time.time()
    print(">>>Randomized Quicksort on Random Data")
    print("took " + str(end_time - start_time) + " seconds\n")

    # randomized quicksort on sorted data
    start_time = time.time()
    quicksort_wrapper(sorted_data, strategy="random")
    end_time = time.time()
    print(">>>Randomized Quicksort on Sorted Data")
    print("took " + str(end_time - start_time) + " seconds\n")

    # randomized quicksort on reversed sorted data
    start_time = time.time()
    quicksort_wrapper(reversed_sorted_data, strategy="random")
    end_time = time.time()
    print(">>>Randomized Quicksort on Reversed Sorted Data")
    print("took " + str(end_time - start_time) + " seconds\n")

    # randomized quicksort on repeated random data
    start_time = time.time()
    quicksort_wrapper(repeated_data, strategy="random")
    end_time = time.time()
    print(">>>Randomized Quicksort on Repeated Random Data")
    print("took " + str(end_time - start_time) + " seconds\n")

    # deterministic quicksort on random data
    start_time = time.time()
    quicksort_wrapper(random_data, strategy="deterministic")
    end_time = time.time()
    print(">>>Deterministic Quicksort on Random Data")
    print("took " + str(end_time - start_time) + " seconds\n")

    # deterministic quicksort on sorted data
    start_time = time.time()
    quicksort_wrapper(sorted_data, strategy="deterministic")
    end_time = time.time()
    print(">>>Deterministic Quicksort on Sorted Data")
    print("took " + str(end_time - start_time) + " seconds\n")

    # deterministic quicksort on reversed sorted data
    start_time = time.time()
    quicksort_wrapper(reversed_sorted_data, strategy="deterministic")
    end_time = time.time()
    print(">>>Deterministic Quicksort on Reversed Sorted Data")
    print("took " + str(end_time - start_time) + " seconds\n")

    # deterministic quicksort on repeated random data
    start_time = time.time()
    quicksort_wrapper(repeated_data, strategy="deterministic")
    end_time = time.time()
    print(">>>Deterministic Quicksort on Repeated Random Data")
    print("took " + str(end_time - start_time) + " seconds\n")

if __name__ == "__main__":
    part_1_validation()

    part_1_comparison()

