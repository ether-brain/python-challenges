"""
Задача:
посчитать количество подстрок в строке
"""


def count_substr(str_in, substr):
    count: int = 0
    str_len = len(str_in)
    substr_len = len(substr)
    print('str_in lenght: ', str_len)
    for i in range(str_len):
        print('letter index: ', i, ' letter: ', str_in[i])
        if str_in[i] != substr[0]:
            pass
        else:
            comparsion_substr = ''
            for j in range(substr_len):
                comparsion_substr = comparsion_substr + str_in[i + j]
            if comparsion_substr != substr:
                pass
            else:
                count += 1
        return count


a = 'helohehhllelelghehellhe'
b = 'll'
print(count_substr(a, b))
