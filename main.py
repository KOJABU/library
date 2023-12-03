def sum_arrays(lst):
     if sum(lst) == 0:
          return 0
     else:
        return sum(lst)

lst = [1, 5.2, 4, 0, -1]
lst1 = []
# sum_arrays(lst)
# print(sum_arrays(lst1))
def sum_ar(lst):
    lst.remove(max(lst))
    lst.remove(min(lst))
    return sum(lst)

print(sum_ar(lst))