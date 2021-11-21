# Требуется найти в бинарном векторе самую длинную последовательность единиц и вывести её длину.
# Желательно получить решение, работающее за линейное время и при этом проходящее по входному массиву только один раз.
# Первая строка входного файла содержит одно число n, n ≤ 10000.
# Каждая из следующих n строк содержит ровно одно число — очередной элемент массива.
# Выходной файл должен содержать единственное число — длину самой длинной последовательности единиц во входном массиве.


def sequential():
    with open('input.txt', 'r') as f:
        n = int(f.readline())

        best = 0
        current = 0

        for _ in range(n):
            num = int(f.readline())
            if num == 1:
                current += 1
                best = max(best, current)
            else:
                current = 0

        return best


if __name__ == '__main__':
    print(sequential())