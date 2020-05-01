import itertools


nested_list = [1, 2, 3, [5, 6, [7, 8]], 9]
flat_list = []


def flatten(some_list):         # recursion
    for i in some_list:
        if type(i) == list:
            flatten(i)
        else:
            flat_list.append(i)


def flatten_list(some_list):
    for i in some_list:
        if isinstance(i, list):
            yield from flatten_list(i)
        else:
            yield i


print("Nested list:", nested_list)
flatten(nested_list)
print("Flat list:", flat_list)

gen = flatten_list(nested_list)
print(list(gen))

