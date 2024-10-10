#1.Функция с параметрами по умолчанию:
def print_params(a = 1, b = 'строка', c = True):
    print(f'a: {a}, b: {b}, c: {c}')
print_params(b = 25)
print_params(c = [1,2,3])

#2.Распаковка параметров:
values_list = ('пример',True, 3.14)
values_dict = {'a': 42, 'b': 'что-то', 'c': [5, 6, 7]}
print_params(*values_list)
print_params(**values_dict)

#3.Распаковка + отдельные параметры:
values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)
