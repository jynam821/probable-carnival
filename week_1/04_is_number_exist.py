
input = [3, 5, 6, 1, 2, 4]


def is_number_exist(number, array):
    for num in array: # array의 길이 만큼 아래 연산 실행
        if number == num: #비교 연산
            return True
    return False
#N만큼의 연산 실행
#시간 복잡도 : N (빅오표기법으로 교기함)
#점근표기법
#O(N)빅오표기법 - 최악의 입력값일 경우 N
#Ω(1)오메가표기법 - 최선의 입력값일 경우 1

result = is_number_exist(3, input)
print(result)