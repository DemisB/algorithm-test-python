from random import randint
import timeit


def smallest_positive_absent_integer_v1(arr):
    sorted_a = sorted(arr)

    i = 1
    try:
        while sorted_a[i] - sorted_a[i - 1] <= 1:
            i += 1
    except IndexError:
        pass
    return max(sorted_a[i - 1] + 1, 1)


def smallest_positive_absent_integer_v2(arr):
    sorted_a = sorted(arr)

    prev_v = sorted_a[0]
    for v in sorted_a[1:]:
        if v - prev_v > 1:
            break
        prev_v = v

    return max(prev_v + 1, 1)


if __name__ == "__main__":
    start = randint(-1000, 900000)

    le_array = [start + i for i in range(100000)]
    missing_nb_idx = randint(0, len(le_array))
    le_array[missing_nb_idx] = le_array[missing_nb_idx] + randint(-10, 10)

    res_v1 = timeit.timeit(lambda: smallest_positive_absent_integer_v1(le_array), number=1000)
    res_v2 = timeit.timeit(lambda: smallest_positive_absent_integer_v2(le_array), number=1000)

    print(f"v1 -> {res_v1}")
    print(f"v2 -> {res_v2}")
