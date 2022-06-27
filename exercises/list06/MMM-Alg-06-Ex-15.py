def precedence(operator: str):
    operator_list = ['+-', '*/', '^']

    for element in operator_list:
        for char in element:
            if operator == char:
                return operator_list.index(element) + 1

    return -1

def expression_to_token_list(expression: str):
    expression = expression.replace(' ', '')
    token_list = []
    additive_operator_list = ['+', '-']

    token = expression[0]
    i = 1
    while i < len(expression):
        char = expression[i]

        def append_token(append_char: bool):
            if append_char:
                token_list.append(token)
                token = ''
                token_list.append(char)
            else:
                token_list.append(token)
                token = ''

        if char.isdigit():
            token += char
        elif char in additive_operator_list:
            previous_char = expression[i - 1]
            if previous_char == ')' or previous_char.isdigit() or previous_char == '':
                append_token(False)
                token += char
            else:
                append_token(True)
        else:
            append_token(True)

        i += 1
    else:
        token_list.append(token)


    return token_list

def main():
    expression = '1 + 2 * 3 - 4 ^ (-4 * x)'
    token_list = expression_to_token_list(expression)
    print(token_list)

if __name__ == "__main__":
    main()