input = "abadabac"

def find_not_repeating_character(string):
    alphabet_occurrence_array = [0] * 26
    ord_a = ord('a')
    for char in string:
        if char.isalpha():
            alphabet_occurrence_array[ord(char) - ord_a] += 1

    not_repeating_character_arr = []
    for idx in range(len(alphabet_occurrence_array)):
        alphabet_occurrence = alphabet_occurrence_array[idx]
        if alphabet_occurrence == 1:
            not_repeating_character_arr.append(chr(idx + ord_a))

    for char in string:
        if char in not_repeating_character_arr:
            return char
    else:
        return '_'

result = find_not_repeating_character(input)
print(result)