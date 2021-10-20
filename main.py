#!/usr/bin/env python3

strs = ['Alemania', 'Francia', 'Camerún', 'Italia', 'Nueva Zelanda']
lengths = []

def solve(arr):
    for word in arr:
        size = len(word)
        lengths.append(size)

    max_value = max(lengths)
    max_index = lengths.index(max_value)

    print(f"El string más largo es: {strs[max_index]}")

if __name__ == '__main__':
    solve(strs)