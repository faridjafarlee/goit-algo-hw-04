from typing import List
from sorting_benchmark import merge

def merge_k_lists(lists: List[List[int]]) -> List[int]:
    if not lists:
        return []
    
    if len(lists) == 1:
        return lists[0]
    
    mid = len(lists) // 2
    left = merge_k_lists(lists[:mid])
    right = merge_k_lists(lists[mid:])
    
    return merge(left, right)

def main():
    lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
    merged_list = merge_k_lists(lists)
    print("Відсортований список:", merged_list)

if __name__ == "__main__":
    main()