
def add_two_numbers(a, b):
    if a is None and b is None:
        raise ValueError('inputs are wrong')
    sum = a + b
    return sum


def add_two_numbers_by_operation():
    result = add_two_numbers(2,3)
    op = get_operation()
    return op, result


def get_operation():
    return 'add'
