a = int(input())
b = list(map(int, input().split()))


def fast_sort(lists, i, j):
    if i >= j:
        return lists
    low = i
    high = j
    pivot = lists[i]
    while i < j:
        while i < j and lists[j] >= pivot:
            j -= 1
        lists[i] = lists[j]
        while i < j and lists[i] <= pivot:
            i += 1
        lists[j] = lists[i]
    lists[j] = pivot
    fast_sort(lists, low, i-1)
    fast_sort(lists, i+1, high)
    return lists


b = fast_sort(b, 0, a - 1)
for i in b:
    print(i, end=' ')
