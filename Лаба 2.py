def split_strings(input_list):
    for string in input_list:
        new_list = list(string)  # преобразуем строку в список символов
        print(new_list)

# Пример использования
input_list = ["Кот", "Собака", "Птица"]
split_strings(input_list)
