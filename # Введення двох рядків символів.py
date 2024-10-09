# Введення двох рядків символів
first_string = input("Введіть перший рядок: ")
second_string = input("Введіть другий рядок: ")

# Пошук символів, які є у першому рядку і яких немає у другому рядку
result = ''.join([char for char in first_string if char not in second_string])

# Виведення результату
print("Символи, які є у першому рядку і відсутні у другому:", result)
