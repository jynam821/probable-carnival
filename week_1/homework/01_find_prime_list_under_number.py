input = 20


def find_prime_list_under_number(number):
    prime_arr = []
    for num in range(2, number):
        for i in range(2, num - 1):
            if num % i == 0:
                break
        else:
            prime_arr.append(num)
    return prime_arr


result = find_prime_list_under_number(input)
print(result)