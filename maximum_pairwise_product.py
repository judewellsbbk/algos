#python3
n = int(input())
a = [int(x) for x in input().split()]

first = a[0]
second = a[1]
if second > first:
    first, second = second, first
a = a[2:]
for element in a:
    if element > second:
        if element >  first:
            first, second = element, first
        else:
            second = element
print(first * second)
