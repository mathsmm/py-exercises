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
    expression = expression.replace(' ', '')

    additive_operator_list = ['+', '-']
    diverse_list = ['*', '/', '^', '(' , ')']

    i = 0
    while i < len(expression):
        char = expression[i]

        if char in additive_operator_list:
            
        i += 1
    return token_list

def main():
    pass

if __name__ == "__main__":
    main()