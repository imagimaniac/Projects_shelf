""" 
For given list of numbers & target sum find number of pairs & the pairs of numbers 
using user defined functions
"""


def paisr_sum(numbers, target_sum):
    numbers = set(numbers)
    numbers = list(numbers)
    pair = list()
    new_pair =list()
    new_pair_2 = []
    for i in numbers:
        if i not in pair:
            requ_num = target_sum - i
            new_num = numbers.copy()
            new_num.remove(i)
            if requ_num in new_num:
                tup = (i,requ_num)
                pair.append(tup)
            else:
                continue
        else:
            continue
    for i in range(len(pair)):
        pair[i] = sorted(pair[i])
        new_pair.append(pair[i])
    for elem in new_pair:
        if elem not in new_pair_2:
            new_pair_2.append(elem)
    pair_count = len(new_pair_2)
    print("Pairs Count is :",pair_count)
    print("list of pair sum is",new_pair_2)

#%%
# Examples:

n = [1,2,3,9,8,17,4,-6,2,4,1]
s = 11
paisr_sum(a,n)

#%%
a = [1,2,0,9,18,7,4,5,2,-4,1]
s = 14
paisr_sum(a,n)

#%%
