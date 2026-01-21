from typing import List


def merge_two_lists(a: List[int], b: List[int]) -> List[int]:
    i = j = 0
    out: List[int] = []

    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            out.append(a[i])
            i += 1
        else:
            out.append(b[j])
            j += 1

    if i < len(a):
        out.extend(a[i:])
    if j < len(b):
        out.extend(b[j:])

    return out


def merge_k_lists(lists: List[List[int]]) -> List[int]:
    current = [lst[:] for lst in lists if lst]
    if not current:
        return []

    while len(current) > 1:
        merged: List[List[int]] = []
        for i in range(0, len(current), 2):
            if i + 1 < len(current):
                merged.append(merge_two_lists(current[i], current[i + 1]))
            else:
                merged.append(current[i])
        current = merged

    return current[0]


if __name__ == "__main__":
    lists_ = [[1, 4, 5], [1, 3, 4], [2, 6]]
    merged_list = merge_k_lists(lists_)
    print("Відсортований список:", merged_list)