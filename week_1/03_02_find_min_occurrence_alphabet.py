# ascii -> str chr()
def find_alphabet_occurrence_array(string):
    alphabet_occurrence_array = [0] * 26
    ord_a = ord('a')
    for char in string:
        if char.isalpha():
            alphabet_occurrence_array[ord(char) - ord_a] += 1

    max_idx = 0
    for idx in range(len(alphabet_occurrence_array)):
        if alphabet_occurrence_array[idx] > alphabet_occurrence_array[max_idx]:
            max_idx = idx
    return chr(max_idx + ord_a)


print(find_alphabet_occurrence_array("hello my name is sparta"))