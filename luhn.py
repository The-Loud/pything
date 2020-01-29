# checksum of numbers

def lunch(c_num):
    def digits_of(n):
        return [int(d) for d in str(n)]

    digits = digits_of(c_num)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    checksum = 0
    checksum += sum(odd_digits)

    for d in even_digits:
        checksum += sum(digits_of(d*2))

    return checksum % 10

def is_valid(c_num):
    return lunch(c_num) == 0

result = is_valid(4532015112830366)
print('Correct:' + str(result))
result = is_valid(6011514433546201)
print('Correct:' + str(result))
result = is_valid(6771549495586802)
print('Correct:' + str(result))
