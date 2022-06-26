from string import punctuation


def precedence(operator: str):
    operator_list = ['+-', '*/', '^']

    for element in operator_list:
        for char in element:
            if operator == char:
                return operator_list.index(element) + 1

    return -1

def expression_to_token_list(expression: str):
    token_list = []
    token = ''
    punctuation_list = ['(', ')']
    multiplicative_operator_list = ['*', '/', '^']
    additive_operator_list = ['+', '-']
    diverse_list = ['.', ',']
    add_flag = False

    i = 0
    while i < len(expression):
        char = expression[i]
        if i > 0:
            previous_char = expression[i - 1]
        if i < len(expression) - 1:
            next_char = expression[i + 1]

        if char == ' ':
            i += 1
            continue
        elif char in (multiplicative_operator_list + punctuation_list):
            token = char
            add_flag = True
        elif char in additive_operator_list:
            token = char
            if previous_char.isdigit() or previous_char == ')':
                add_flag = True
            else:
                add_flag = False
        elif char in diverse_list or char.isdigit():
            token += char

        if add_flag:
            token_list.append(token)
            token = ''
            add_flag = False

        if next_char in (punctuation_list + multiplicative_operator_list + additive_operator_list + diverse_list) or next_char == ' ':
            token_list.append(token)
            token = ''

        i += 1

    if token != '':
        token_list.append(token)

    return token_list



def main():
    expression = '(1+2)*3^(-4/5)'
    token_list = expression_to_token_list(expression)
    print(token_list)

if __name__ == "__main__":
    main()