
def quickSort(l:list, lo:int, hi:int) -> None:
    if hi - lo <= 0:
        return
    first = l[lo]
    lf = lo
    rt = hi
    while lf < rt:
        while lf < rt and first < l[rt]:
            rt -= 1
        l[lf] = l[rt]
        
        # while lf < rt and l[lf] <= first:
        while lf < rt and not first < l[lf]:
            lf += 1
        l[rt] = l[lf]
    
    l[lf] = first

    quickSort(l, lo, lf - 1)
    quickSort(l, lf + 1, hi)

def QuickSort(l: list):
    quickSort(l, 0, len(l) - 1)
    return l
