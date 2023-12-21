import heapq


def get_kth_element(arr: list, k: int):
    """
    отдаёт k-ый наименьший элемент в списке arr
    уже не так читерски использует кучи
    """
    kheap = []
    for i, elem in enumerate(arr):
        if i < k:
            heapq.heappush(kheap, elem)
        else:
            heapq.heappushpop(kheap, elem)
    return heapq.heappop(kheap)


def solution():
    arr = list(map(int, input().split()))
    k = int(input())
    print(get_kth_element(arr, k))


if __name__ == "__main__":
    solution()
