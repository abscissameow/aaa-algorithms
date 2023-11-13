def max_even_sum(numbers: list) -> int:
    """
    вычисляет максимальную сумму элементов массива, которая делится на 2
    """
    total_sum = sum(numbers)
    if total_sum % 2 == 0:
        return total_sum
    else:
        min_odd = float('inf')
        for num in numbers:
            if num % 2 != 0 and num < min_odd:
                min_odd = num
        return total_sum - min_odd


def solution():
    """
    применяет функцию max_even_sum() для демонстрации решения на примерах
    """
    numbers = [int(x) for x in input().split()]
    result = max_even_sum(numbers)
    print(result)


solution()
