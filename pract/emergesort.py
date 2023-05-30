def merge_sort(data, l, r):
    if l >= r:
        return
    mid = (r+l)//2
    merge_sort(data, l, mid)
    merge_sort(data, mid+1, r)
    i = l
    j = mid + 1
    tmp = []
    while i <= mid and j <= r:
        if data[j] >= data[i]:
            tmp.append(data[i])
            i += 1
        else:
            tmp.append(data[j])
            j += 1
    tmp += data[i:mid+1]
    tmp += data[j:r+1]
    data[l:r+1] = tmp



if __name__ == "__main__":
    n = [34, 14, 64, 64, 23, 64]
    merge_sort(n, 0, 5)
    print(n)
#    n = int(input())
#    data = [int(x) for x in input().split()]
#    l = 0
#    r = n - 1
#    merge_sort(data, l, r)
#    print(' '.join(map(str, data)))
