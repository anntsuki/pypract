n, k = map(int, input().split())
a = [int(x) for x in input().split()]
def fast_sort(lists, i, j):
    if i >= j:
        return lists
    pivot = lists[i]
    low = i
    high = j

