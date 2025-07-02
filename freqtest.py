def count_values_frequency(dictt):
    frequency = {}
    for value in dictt.values():
        if value in frequency:
            frequency[value] += 1
        else:
            frequency[value] = 1
    return frequency

dictt = {
    'V': 10,
    'VI': 10,
    'VII': 40,
    'VIII': 20,
    'IX': 70,
    'X': 80,
    'XI': 40,
    'XII': 20
}

print(count_values_frequency(dictt))