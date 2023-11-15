import heapq


def get_kth_element(arr: list, k: int):
    """
    отдаёт k-ый наименьший элемент в списке arr
    читерски использует кучи!!
    """
    heapq.heapify(arr)
    return heapq.nsmallest(k+1, arr)[-1]


def solution():
    arr = list(map(int, input().split()))
    k = int(input())
    print(get_kth_element(arr, k))


if __name__ == "__main__":
    solution()
