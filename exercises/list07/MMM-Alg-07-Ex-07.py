import random as rd


def create_bingo_list():
    bingo_range_dict = {
        "B": [1, 15],
        "I": [16,30],
        "N": [31,45],
        "G": [46,60],
        "O": [61,75] 
    }

    bingo_result_dict = {
        "B": [],
        "I": [],
        "N": [],
        "G": [],
        "O": []
    }
    #rd.randint(bingo_dict["B"][0], bingo_dict["B"][1])
    for key in bingo_result_dict:
        while True:
            aux_set = set()
            random = rd.randint(bingo_range_dict[key][0], bingo_range_dict[key][1])
            if random not in aux_set:
                aux_set.add(random)
                bingo_result_dict[key].append(random)
                if len(bingo_result_dict[key]) == 5:
                    break

    return bingo_result_dict


def main():
    bingo_result_dict = create_bingo_list()
    print(bingo_result_dict)

if __name__ == "__main__":
    main()