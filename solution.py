

def unique_sorted(lst: list[int]) -> list[int]:
    if not lst:
        return []
    return sorted(lst)


def rotate_list(lst: list, k: int) -> list:
    if not lst:
        return []
    for i in range(abs(k)):
        lst.insert(0, lst.pop())
    return lst


def char_frequency(text: str) -> dict:
    res = {}
    for char in text:
        if char in res:
            res[char] += 1
        else:
            res[char] = 1
    return res

if __name__ == "__main__":
    pass