n = [i.lower() for i in input() if i .isalpha()]
print('YES' if n == n[::-1] else 'NO')
