def max_even_sum(numbers: list) -> int:
    """
    эта функция вычисляет максимальную сумму элементов массива, которая делится на 2
    """
    total_sum = sum(numbers)
    if total_sum % 2 == 0:
        return total_sum
    else:
        odd_numbers = []
        min_odd = None

        for num in numbers:
            if num % 2 != 0:
                odd_numbers.append(num)
                if min_odd is None or num < min_odd:
                    min_odd = num
        return total_sum - min_odd if odd_numbers else 0

def solution():
    """
    применяет функцию max_even_sum() для демонстрации решения на примерах
    """
    numbers = [int(x) for x in input().split()]
    result = max_even_sum(numbers)
    print(result)

solution()