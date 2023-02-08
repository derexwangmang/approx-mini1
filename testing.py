import random
import bins
import os
import csv

def generate_data(num_items, distribution, data_directory_name):
    res = []
    for _ in range(num_items):
        probability_generated = random.random()
        if probability_generated <= distribution[0]:
            generated_num = random.uniform(distribution[1][0], distribution[1][1])
        else:
            generated_num = random.uniform(distribution[1][1], 1)

        res.append(generated_num)

    os.makedirs(data_directory_name)
    with open("{}/data.csv".format(data_directory_name), "w") as f:
        write = csv.writer(f)
        write.writerow(res)
    
    return res

def test(num_items=1000, distribution=(1, [0, 1]), data_directory_name="None"):
    data = generate_data(num_items, distribution, data_directory_name)

    first_fit = bins.bin_pack(data, False, 0, 1)
    with open("{}/first_fit.csv".format(data_directory_name), "w") as f:
        write = csv.writer(f)
        write.writerow(first_fit[0])
        write.writerow([first_fit[1]])
        write.writerow([first_fit[2]])

    best_fit = bins.bin_pack(data, False, 1, 1)
    with open("{}/best_fit.csv".format(data_directory_name), "w") as f:
        write = csv.writer(f)
        write.writerow(best_fit[0])
        write.writerow([best_fit[1]])
        write.writerow([best_fit[2]])

    sorted_first_fit = bins.bin_pack(data, True, 0, 1)
    with open("{}/sorted_first_fit.csv".format(data_directory_name), "w") as f:
        write = csv.writer(f)
        write.writerow(sorted_first_fit[0])
        write.writerow([sorted_first_fit[1]])
        write.writerow([sorted_first_fit[2]])

    sorted_best_fit = bins.bin_pack(data, True, 1, 1)
    with open("{}/sorted_best_fit.csv".format(data_directory_name), "w") as f:
        write = csv.writer(f)
        write.writerow(sorted_best_fit[0])
        write.writerow([sorted_best_fit[1]])
        write.writerow([sorted_best_fit[2]])

    return first_fit, best_fit, sorted_first_fit, sorted_best_fit

if __name__ == "__main__":
    test(1000, (0.75, [0, 0.25]), "right_tailed_1000")
    test(1000, (0.25, [0, 0.75]), "left_tailed_1000")