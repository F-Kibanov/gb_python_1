# a = [15 * 3, 15 / 3, 15 // 2, 15 ** 2]
# for i in range(len(a)):
#     print(a[i], '  ', type(a[i]))

    
examples = [15 * 3, 15 / 3, 15 // 2, 15 ** 2]
example_type = map(lambda x: type(x), examples)
print(*example_type, sep = '\n')
