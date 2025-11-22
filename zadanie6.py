def listy (l1:list, l2:list)->list:
    tmp = set(l1+l2)
    return [n**3 for n in tmp]
print(listy([1,2,5],[1,4]))