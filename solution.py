

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

if __name__ == "__main__":
    pass