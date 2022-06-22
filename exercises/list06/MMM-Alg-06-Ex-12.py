# Verifica se está em ordem crescente
# def is_ordered(list):
#     for i in range(len(list)-1):
#         if list[i] > list[i+1]:
#             return False
#     return True

def input_to_int_list():
    int_list = []
    while True:
        int_input = int(input("Informe um número inteiro (zero para parar): "))
        if int_input == 0:
            break

        int_list.append(int_input)

    return int_list

def is_ordered(list):
    sorted_aux_list = list.sort()
    sorted_reverse_aux_list = list.sort(reverse=True)

    if list == sorted_aux_list or list == sorted_reverse_aux_list:
        return True
    return False

def main():
    list = input_to_int_list()
    if is_ordered(list):
        print("A lista está ordenada")
    else:
        print("A lista não está ordenada")
        
if __name__ == "__main__":
    main()