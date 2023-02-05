import time as time

def first_fit(items, bins, max_weight):
    for i in range(len(items)):
        added = False
        for j in range(len(bins)):
            if items[i] + bins[j] <= max_weight:
                    bins[j] += items[i]
                    added = True
                    break
        
        if not added:
            bins.append(items[i])
            
    return bins

def best_fit(items, bins, max_weight):
    for i in range(len(items)):
        best_weight, best_index = -1, -1
        for j in range(len(bins)):
            if items[i] + bins[j] <= max_weight and best_weight <= items[i] + bins[j]:
                    best_weight = items[i] + bins[j]
                    best_index = j

        if best_index != -1:
            bins[best_index] += items[i]
        else:
            bins.append(items[i])

    return bins

def bin_pack(items=[], require_sort=True, alg=0, max_weight=1):
    start = time.time()

    if require_sort:
        items.sort(reverse=True)
    
    bins = [0]
    
    if alg == 0:
        bins = first_fit(items, bins, max_weight)
    elif alg == 1:
        bins = best_fit(items, bins, max_weight)
    
    finish = time.time()

    return [bins, len(bins), 1000*(finish - start)]