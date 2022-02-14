input = 20


#내 풀이
def find_prime_list_under_number(number):
    prime_arr = []
    for num in range(2, number + 1):
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            prime_arr.append(num)
    return prime_arr

#개선 풀이
def find_prime_list_under_number2(number):
    prime_list = []

    for n in range(2, number + 1):
        for i in prime_list:
            if n % i == 0 and i * i <= n:
                break
        else:
            prime_list.append(n)

    return prime_list


result = find_prime_list_under_number(input)
result = find_prime_list_under_number2(input)
print(result)


result = find_prime_list_under_number(input)
print(result)