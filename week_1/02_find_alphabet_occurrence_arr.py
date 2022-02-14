input = "hello my name is sparta"


# 파이썬 내장 함수 is_alpha() 알파벳인 경우 true 반환
# ascii code 가져오기 - ord()
def find_max_occurred_alphabet(string):
    alphabet_arr = [0] * 26
    ord_a = ord('a')
    for char in string:
        if char.isalpha():
            alphabet_arr[ord(char) - ord_a] += 1
    return alphabet_arr

result = find_max_occurred_alphabet(input)
print(result)