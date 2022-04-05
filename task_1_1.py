def convert_time(duration: int) -> str:
    if duration < 0:
        return 'wrong_value!'
    elif duration < 60:
        result = f'{duration} сек'
    elif duration < 3600:
        result = f'{duration // 60} мин {duration % 60} сек'
    elif duration < 86400:
        result = f'{duration // 3600} час {(duration % 3600) // 60} мин {duration % 60} сек'
    else:
        result = f'{duration // 86400} дн {(duration % 86400) // 3600} час {(duration % 3600) // 60} мин {duration % 60} сек '
    return result


# for duration in range(-10, 100000):
#     result = convert_time(duration)
#     print(result)

duration = 368916
result = convert_time(duration)
print(result)
