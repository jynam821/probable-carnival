# 최대값 찾기 예제
input = [3, 5, 6, 1, 2, 4]

# for-else문, for문을 돌 동안 break가 되지 않았을 경우 else문을 탐.

def find_max_num(array):
    for num in array:
        for compare_num in array:
            if num < compare_num:
                break
        else:
            return num
    return 1


result = find_max_num(input)
print(result)