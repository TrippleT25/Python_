def merge_dicts(dict1, dict2):
    result = {}  # Новый словарь для результата

    # Добавляем ключи и значения из первого словаря
    for key, value in dict1.items():
        result[key] = value

    # Добавляем ключи и значения из второго словаря
    for key, value in dict2.items():
        if key in result:
            result[key] += value  # Складываем значения одинаковых ключей
        else:
            result[key] = value  # Добавляем новые ключи

    return result

# Пример использования 
dict1 = {'a': 200, 'b': 50}
dict2 = {'a': 100, 'c': 500}

merged = merge_dicts(dict1, dict2)
print(merged)
