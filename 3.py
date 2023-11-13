def max_div3_sum(nums: list) -> int:
    """
    вычисляет максимальную сумму элементов массива, которая делится на 3
    """
    total = sum(nums)
    remainder = total % 3
    if remainder == 0:
        return total

    rem1, rem2 = [float('inf')] * 2, [float('inf')] * 2
    for num in nums:
        if num % 3 == 1:
            if num <= rem1[0]:
                rem1[1] = rem1[0]
                rem1[0] = num
            elif num < rem1[1]:
                rem1[1] = num
        elif num % 3 == 2:
            if num <= rem2[0]:
                rem2[1] = rem2[0]
                rem2[0] = num
            elif num < rem2[1]:
                rem2[1] = num

    if remainder == 1:
        if (rem1[0] == float('inf')) or (sum(rem2) < rem1[0]):
            return total - sum(rem2)
        else:
            return total - rem1[0]

    elif remainder == 2:
        if (rem2[0] == float('inf')) or (sum(rem1) < rem2[0]):
            return total - sum(rem1)
        else:
            return total - rem2[0]


def solution():
    """
    применяет функцию max_div3_sum() для демонстрации решения на примерах
    """
    numbers = [int(x) for x in input().split()]
    result = max_div3_sum(numbers)
    print(result)


solution()
