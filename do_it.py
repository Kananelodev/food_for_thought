def merge_with_fallback(keys, values1, values2):
    new = {}
    if values2 == [] or len(keys) ==len(values2): 
        values2.extend(values1)
        for x,y in zip(keys,values2):
            new.setdefault(x,y)
        return new
    if len(keys) > len(values2):
        values2.extend(values1[len(values2):])
        for x,y in zip(keys,values2):
            new.setdefault(x,y)


    return new
# print(merge_with_fallback(['a','b','c'], [1,2,3], [10,5]))


def group_numbers_by_parity(nums):
    new = {}
    new['odd'] = [i for i in nums if i % 2 != 0]
    new['even'] = [i for i in nums if i % 2 == 0]
    return new

    
# print(group_numbers_by_parity([1,2,3,4]))

def invert_dict_with_sets(data):
    return {value:set(key for key,value2 in data.items() if value2==value) for key,value in data.items()}
print(invert_dict_with_sets({'x':10,'y':10,'z':20}))

def flatten_mixed_list(items):
    new = []
    for item in items:
        if isinstance(item, list):
            new.extend(flatten_mixed_list(item))
        elif isinstance(item, tuple):
            new.extend(flatten_mixed_list(item))
        else:
            new.append(item)
    return new

def count_unique_elements(items):
    new = set(items)
    return len(new)
    
# print(count_unique_elements([1,1,2,3])) 
import math
def recursive_factorial(n):
    
    if n == 0 or n == 1:
        return 1
    else:
        return n * recursive_factorial(n - 1)
    
# print(recursive_factorial(5))

def recursive_reverse_list(lst):
    if not lst or len(lst) <= 1:
        return lst
    else:
        return recursive_reverse_list(lst[1:]) + [lst[0]]

def tuple_to_frequency_dict(tpl):
    well = {}
    for i in tpl:
        ok = tpl.count(i)
        well.setdefault(i,ok)
    return well
   

# print(tuple_to_frequency_dict((1,2,2)))


def set_intersection_all(sets_list):
    sets = [set(i) for i in sets_list]
    print(sets)
    if sets:
        ok = sets[0].intersection(*sets[1:])
    else:
        ok = set()
    return ok

# print(set_intersection_all([{1,2,3},{2,3},{2}]))
def group_words_by_last_letter(words):
    new = {}
    for i in words:
        new.setdefault(i[-1],[]).append(i)
    return new

# print(group_words_by_last_letter(['cat','bat','car']))

def recursive_flatten(data):
    new = []
    for item in data:
        if isinstance(item, list):
            new.extend(flatten_mixed_list(item))
        elif isinstance(item, tuple):
            new.extend(flatten_mixed_list(item))
        else:
            new.append(item)
    return new

def dict_of_squares(nums):
    new = {}
    for i in nums:
        new.setdefault(i, i*i)
    return new

# print(dict_of_squares([1,2,3]))