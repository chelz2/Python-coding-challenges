'''
problem - for a given array/list of integer return all tuple pair in list that sum up to equal a given no.
eg - i/p : ([1,2,3,4], 5) 
    --> o/p: (1,4) (1,4)
'''


def pair_sum(arr, k):

    if len(arr) < 2:
        return "None"

    # set for tracking
    seen = set()
    output = set()

    for num in arr :
        target = k - num

        if target not in seen:
            seen.add(num)
        else:
            output.add((min(target,num), max(target,num)))

    return output

pair_sum([1,3,4,2],5)