
def to_binary(num):
    result = ''
    while num > 0:
        if num % 2 == 0:
            result = '0' + result
        else:
            result = '1' + result
        num = num // 2
    return int(result)

print(to_binary(15))