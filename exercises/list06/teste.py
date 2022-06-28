a = '+4'
print(int(a))

def str_is_integer(str):
    try:
        int(str)
        return True
    except ValueError:
        return False