def reverse_slice(lst: list[int], a: int, b: int) -> list[int]:
    return lst[:a - 1] + lst[a - 1: b][::-1] + lst[b:]



n, x1, y1, x2, y2 = list(map(int, input().split()))
numbers = [*range(1, n + 1)]

fnc = reverse_slice(numbers, x1, y1)
print(*reverse_slice(fnc, x2, y2))
