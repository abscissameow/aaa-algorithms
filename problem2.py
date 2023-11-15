import heapq


def merge_k_sorted(arrs: list) -> list:
    """
    объединяем k отсортированных массивов
    """
    min_heap = [(lst[0], i, 0) for i, lst in enumerate(arrs) if lst]
    heapq.heapify(min_heap)
    merged = []

    while min_heap:
        val, arr_index, element_index = heapq.heappop(min_heap)
        merged.append(val)

        if element_index + 1 < len(arrs[arr_index]):
            next_tuple = (arrs[arr_index][element_index + 1],
                          arr_index,
                          element_index + 1)
            heapq.heappush(min_heap, next_tuple)
    return merged


def solution():
    arrs = read_multiline_input() # эта функция уже написана
    merged = merge_k_sorted(arrs)
    print(' '.join([str(el) for el in merged]))


if __name__ == "__main__":
    solution()
