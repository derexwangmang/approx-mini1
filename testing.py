import random
import bins
import os
import csv

def generate_data(num_items):
    res = []
    for _ in range(num_items):
        res.append(random.random())

    os.makedirs(str(num_items))
    with open("{}/data.csv".format(num_items), "w") as f:
        write = csv.writer(f)
        write.writerow(res)
    
    return res

def test(num_items=10):
    data = generate_data(num_items)

    first_fit = bins.bin_pack(data, False, 0, 1)
    with open("{}/first_fit.csv".format(num_items), "w") as f:
        write = csv.writer(f)
        write.writerow(first_fit)

    best_fit = bins.bin_pack(data, False, 1, 1)
    with open("{}/best_fit.csv".format(num_items), "w") as f:
        write = csv.writer(f)
        write.writerow(best_fit)

    sorted_first_fit = bins.bin_pack(data, True, 0, 1)
    with open("{}/sorted_first_fit.csv".format(num_items), "w") as f:
        write = csv.writer(f)
        write.writerow(sorted_first_fit)

    sorted_best_fit = bins.bin_pack(data, True, 1, 1)
    with open("{}/sorted_best_fit.csv".format(num_items), "w") as f:
        write = csv.writer(f)
        write.writerow(sorted_best_fit)

    return first_fit, best_fit, sorted_first_fit, sorted_best_fit

if __name__ == "__main__":
    for num in [10, 100, 1000]:
        test(num)    
