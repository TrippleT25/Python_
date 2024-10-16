import os

def get_full_path(directory: str, filename: str) -> str:
    return os.path.join(directory, filename)

# Пример использования
directory = '/home/user/documents'
filename = 'file.txt'
full_path = get_full_path(directory, filename)

print(full_path)  # /home/user/documents/file.txt
