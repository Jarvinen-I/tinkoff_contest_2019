a, b = map(int, input().split())
c, d = map(int, input().split())

if a > b:
    a, b = b, a
if c > d:
    c, d = d, c

print(a <= c and b <= d)
