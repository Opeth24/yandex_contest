from collections import defaultdict


def is_anagrams_nln(a: str, b: str) -> bool:
    a = sorted(a)
    b = sorted(b)
    return a == b


def is_anagrams_n(a: str, b: str) -> bool:
    counter = defaultdict(int)
    for letter in a:
        counter[letter] += 1

    for letter in b:
        counter[letter] -= 1
        if counter[letter] < 0:
            return False
    return True


def print_result(result: bool) -> None:
    print(1 if result else 0)


if __name__ == '__main__':
    a = input()
    b = input()

    print_result(is_anagrams_nln(a, b))
