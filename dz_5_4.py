def get_numbers(src: list):
    pass

    result = []
    tmp_list = [result.append(src[i + 1]) for i in range(len(src) - 1) if src[i] < src[i + 1]]

    return result


src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print(*get_numbers(src))
