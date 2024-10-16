# Функция для "расплющивания" списка списков в один плоский список
def flatten_list(list_of_lists):
    # Генераторное выражение для объединения всех элементов
    return [item for sublist in list_of_lists for item in sublist]

# Пример списка списков
input_list = [[1, 6, 3], [4, 8], [2, 7, 5, 9]]

# Вызов функции для получения плоского списка
flattened_list = flatten_list(input_list)

# Вывод результата
print("Исходный список списков:", input_list)
print("Плоский список:", flattened_list)
