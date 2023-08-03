

def fake_bin(x):
    result = ''
    for i in x:
        if i in '234':
            result += '0'
        elif i in '56789':
            result += '1'
        else:
            result += i
    return result
    pass

number = '3214323242111100000'

output = fake_bin(number)

print(output)

def fake_bin(x):
    result = ''
    for i in x:
        if i in '01234':
            result += '0'
        elif i in '56789':
            result += '1'
        else:
            result += i
    return result
    pass