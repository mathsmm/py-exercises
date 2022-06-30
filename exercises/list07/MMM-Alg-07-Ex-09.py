import random as rd


def create_bingo_list():
    bingo_range_dict = {
        "B": [1, 15],
        "I": [16,30],
        "N": [31,45],
        "G": [46,60],
        "O": [61,75] 
    }

    bingo_result_dict = {"B": [], "I": [], "N": [], "G": [], "O": []}

    for key in bingo_result_dict:
        aux_set = set()
        while True:
            random = rd.randint(bingo_range_dict[key][0], bingo_range_dict[key][1])
            if random not in aux_set:
                aux_set.add(random)
                bingo_result_dict[key].append(random)
                if len(bingo_result_dict[key]) == 5:
                    bingo_result_dict[key].sort()
                    break

    return bingo_result_dict

def format_bingo_dict_to_str(bingo_dict: dict):
    result = "------------------------------------\n"
    result += "| "
    i = 0
    for key in bingo_dict:
        if i != 4:
            result += f"{key}\t"
        else:
            result += f"{key}"
        i += 1
    else:
        result += "  |\n"
        result += "------------------------------------\n"

    i = 0
    while i < 5:
        j = 0
        for key in bingo_dict:
            if   j == 0:
                result += f"| {bingo_dict[key][i]}\t"
            elif j == 4:
                result += f"{bingo_dict[key][i]}"
            else:
                result += f"{bingo_dict[key][i]}\t"
            j += 1
        result += " |\n"
        i += 1

    result += "------------------------------------"
    return result

def verify_bingo_dict(bingo_dict: dict):
    i = 0
    # Verify columns
    while i < 5:
        sum = 0
        for key in bingo_dict:
            sum += bingo_dict[key][i]
        if sum == 0:
            return True
        i += 1

    # Verify rows
    for key in bingo_dict:
        sum = 0
        for value in bingo_dict[key]:
            sum += value
        if sum == 0:
            return True

    #Verify diagonals
    sum1 = 0
    sum2 = 0
    i = 0
    j = 4
    for key in bingo_dict:
        sum1 += bingo_dict[key][i]
        sum2 += bingo_dict[key][j]
        i += 1
        j -= 1
    if sum1 == 0 or sum2 == 0:
        return True

    return False

def return_all_valid_bingo_numbers():
    bingo_list = ['B', 'I', 'N', 'G', 'O']
    result = []

    multiplier = 1
    for element in bingo_list:
        i = (15 * multiplier) - 14
        while i <= (15 * multiplier):
            result.append(element + str(i))
            i += 1
        multiplier += 1

    return result


def main():
    # bingo_dict = create_bingo_list()
    # print(format_bingo_dict_to_str(bingo_dict))
    bingo_dict = create_bingo_list()
    bingo_numbers = return_all_valid_bingo_numbers()
    rd.shuffle(bingo_numbers)
    

if __name__ == "__main__":
    main()