import heapq


class StreamMedian:
    """
    это класс для нахождения медианы в текущей последовательности чисел
    """

    def __init__(self):
        """
        инициализируем две кучи:
        максимальная куча - для меньшей половины значений,
        и минимальная куча - для большей половины
        """
        self.small = []
        self.large = []

    def add_num(self, num):
        """
        добавление нового числа в последовательность
        """
        if len(self.small) == len(self.large):
            heapq.heappush(self.large, -heapq.heappushpop(self.small, -num))
        else:
            heapq.heappush(self.small, -heapq.heappushpop(self.large, num))

    def find_median(self):
        """
        нахождение медианы
        """
        if len(self.small) == len(self.large):
            return float(self.large[0] - self.small[0]) / 2.0
        else:
            return float(self.large[0])


def solution():
    n = int(input())
    stream = StreamMedian()
    for i in range(n):
        line = input().split()
        command = line[0]
        if command == "ADD":
            stream.add_num(int(line[1]))
        elif command == "FIND_MEDIAN":
            print(f'{stream.find_median():.1f}')


if __name__ == "__main__":
    solution()
