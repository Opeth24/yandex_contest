# Даны две строки строчных латинских символов: строка J и строка S.
# Символы, входящие в строку J, — «драгоценности», входящие в строку S — «камни».
# Нужно определить, какое количество символов из S одновременно являются «драгоценностями».
# Проще говоря, нужно проверить, какое количество символов из S входит в J.


def jewelry(j: str, s: str) -> int:
    count = 0
    for s_i in s:
        if s_i in j:
            count += 1
    return count


if __name__ == '__main__':
    j = input()
    s = input()

    print(jewelry(j, s))