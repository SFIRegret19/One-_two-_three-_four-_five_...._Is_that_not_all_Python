def calculate_structure_sum(structure_):
    global total_amount
    for i in structure_:
        if isinstance(i, list) or isinstance(i, tuple) or isinstance(i, set):
            list_counter(i)
        elif isinstance(i, dict):
            dict_counter(i)
        elif isinstance(i, str):
            total_amount += len(i)
        elif isinstance(i, int):
            total_amount += i
    return total_amount

def list_counter (list_):
    global total_amount
    for i in list_:
        if isinstance(i, int):
            total_amount += i
        elif isinstance(i, str):
            total_amount += len(i)
        elif isinstance(i, list):
            list_counter(i)
        elif isinstance(i, tuple):
            list_counter(list(i))
        elif isinstance(i, set):
            list_counter(list(i))
        elif isinstance(i, dict):
            dict_counter(i)
    return total_amount

def dict_counter (dict_):
    global total_amount
    for key, value in dict_.items():
        if isinstance(key, int) and isinstance(value, int):
            total_amount += (key + value)
        elif isinstance(key, str) and isinstance(value, int):
            total_amount += (value + len(key))
        elif isinstance(key, int) and isinstance(value, str):
            total_amount += (key + len(value))
        elif isinstance(key, str) and isinstance(value, str):
            total_amount += (len(key) + len(value))

        elif isinstance(key, tuple) and isinstance(value, str):
            list_counter(key)
            total_amount += len(value)
        elif isinstance(key, tuple) and isinstance(value, list):
            list_counter(key)
            list_counter(value)
        elif isinstance(key, tuple) and isinstance(value, tuple):
            list_counter(key)
            list_counter(value)
        elif isinstance(key, tuple) and isinstance(value, set):
            list_counter(key)
            list_counter(value)
        elif isinstance(key, tuple) and isinstance(value, dict):
            list_counter(key)
            dict_counter(value)
        
        elif isinstance(key, str) and isinstance(value, list):
            total_amount += len(key)
            list_counter(value)
        elif isinstance(key, str) and isinstance(value, tuple):
            total_amount += len(key)
            list_counter(value)
        elif isinstance(key, str) and isinstance(value, set):
            total_amount += len(key)
            list_counter(value)
        elif isinstance(key, str) and isinstance(value, dict):
            total_amount += len(key)
            dict_counter(value)
    return total_amount

total_amount = 0

data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

calculate_structure_sum(data_structure)

print(total_amount)