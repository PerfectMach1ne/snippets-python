def multiply_for_each(values, multiplier):
    temp_values = list()
    for value in values:
        temp_values.append(value * multiplier)
    print(temp_values)
    return temp_values


multiply_for_each([3, 7.1, 3, 1.0], 3)
