from __future__ import annotations

import random
import timeit
from dataclasses import dataclass
from typing import Callable, List, Tuple


def insertion_sort(arr: List[int]) -> List[int]:
    a = arr[:]
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a


def merge(left: List[int], right: List[int]) -> List[int]:
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    if i < len(left):
        merged.extend(left[i:])
    if j < len(right):
        merged.extend(right[j:])
    return merged


def merge_sort(arr: List[int]) -> List[int]:
    if len(arr) <= 1:
        return arr[:]
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


def timsort(arr: List[int]) -> List[int]:
    return sorted(arr)


def make_random(n: int, *, seed: int = 123) -> List[int]:
    rnd = random.Random(seed)
    return [rnd.randint(-10**6, 10**6) for _ in range(n)]


def make_sorted(n: int) -> List[int]:
    return list(range(n))


def make_reversed(n: int) -> List[int]:
    return list(range(n, 0, -1))


def make_nearly_sorted(n: int, *, swaps: int = 10, seed: int = 123) -> List[int]:
    a = list(range(n))
    rnd = random.Random(seed)
    for _ in range(min(swaps, n)):
        i = rnd.randrange(n)
        j = rnd.randrange(n)
        a[i], a[j] = a[j], a[i]
    return a


def make_many_duplicates(n: int, *, seed: int = 123) -> List[int]:
    rnd = random.Random(seed)
    vals = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    return [rnd.choice(vals) for _ in range(n)]


@dataclass(frozen=True)
class Algo:
    name: str
    fn: Callable[[List[int]], List[int]]


def measure_seconds(algo: Algo, data: List[int], *, number: int, repeat: int) -> float:
    def stmt():
        out = algo.fn(data)
        if len(out) != len(data):
            raise RuntimeError("Invalid sort output length")
        return out

    times = timeit.repeat(stmt, number=number, repeat=repeat)
    return min(times) / number


def main():
    algos = [
        Algo("Insertion sort", insertion_sort),
        Algo("Merge sort", merge_sort),
        Algo("Timsort (sorted)", timsort),
    ]

    datasets: List[Tuple[str, Callable[[int], List[int]]]] = [
        ("Random", make_random),
        ("Already sorted", make_sorted),
        ("Reversed", make_reversed),
        ("Nearly sorted", lambda n: make_nearly_sorted(n, swaps=max(10, n // 1000))),
        ("Many duplicates", make_many_duplicates),
    ]

    sizes = [200, 500, 1000, 2000, 10_000]

    repeat = 5

    for n in sizes:
        print(f"\nn = {n}")
        for ds_name, ds_fn in datasets:
            data = ds_fn(n)
            print(f"  Dataset: {ds_name}")
            for algo in algos:
                number = 50 if n <= 500 else 10
                sec = measure_seconds(algo, data, number=number, repeat=repeat)
                print(f"    {algo.name:<16} {sec:.6f} sec/run")


if __name__ == "__main__":
    main()
