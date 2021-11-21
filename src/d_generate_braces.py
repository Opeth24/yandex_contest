# Дано целое число n. Требуется вывести все правильные скобочные последовательности длины 2 ⋅ n,
# упорядоченные лексикографически (см. https://ru.wikipedia.org/wiki/Лексикографический_порядок).
#
# В задаче используются только круглые скобки.
#
# Желательно получить решение, которое работает за время, пропорциональное общему количеству правильных скобочных
# последовательностей в ответе, и при этом использует объём памяти, пропорциональный n.
#
# Формат ввода
# Единственная строка входного файла содержит целое число n, 0 ≤ n ≤ 11
#
# Формат вывода
# Выходной файл содержит сгенерированные правильные скобочные последовательности, упорядоченные лексикографически.


def generate_braces(n: int, open_counter: int, close_counter: int, answer: str) -> str:
    if open_counter + close_counter == 2 * n:
        print(answer)
    if open_counter < n:
        generate_braces(n, open_counter + 1, close_counter, answer + '(')
    if open_counter > close_counter:
        generate_braces(n, open_counter, close_counter + 1, answer + ')')


if __name__ == '__main__':
    n = int(input())
    generate_braces(n, 0, 0, '')
