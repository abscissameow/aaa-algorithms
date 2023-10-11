def max_div3_sum(nums: list) -> int:
    """
    вычисляет максимальную сумму элементов массива, которая делится на 3
    """
    total = sum(nums)
    remainder = total % 3
    if remainder == 0:
        return total

    nums_1 = sorted(x for x in nums if x % 3 == 1)
    nums_2 = sorted(x for x in nums if x % 3 == 2)

    if remainder == 1:
        if len(nums_2) >= 2 and (not nums_1 or sum(nums_2[:2]) < nums_1[0]):
            return total - sum(nums_2[:2])
        else:
            return total - nums_1[0]

    elif remainder == 2:
        if len(nums_1) >= 2 and (not nums_2 or sum(nums_1[:2]) < nums_2[0]):
            return total - sum(nums_1[:2])
        else:
            return total - nums_2[0]

def solution():
    """
    применяет функцию max_div3_sum() для демонстрации решения на примерах
    """
    numbers = [int(x) for x in input().split()]
    result = max_div3_sum(numbers)
    print(result)

solution()