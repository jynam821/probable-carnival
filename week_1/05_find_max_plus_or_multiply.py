#더하거나 곱했을 때 가장 큰 값 찾기
input = [0, 3, 5, 6, 1, 2, 4]


def find_max_plus_or_multiply(array):
    output = 0 # 대입연산 1
    for num in array: #array의 길이만큼 실행됨
        if num < 2 or output < 2:
            output += num
        else:
            output *= num
    return output


result = find_max_plus_or_multiply(input)
print(result)