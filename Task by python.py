
print("Введите ваш масив как строку или нажмите Enter и будет использован стандартный тестовый масив")
input_array = input()

if len(input_array) < 1:
    input_array = "123 12345 1234567 12345678 123 12 1"

result_array = []
for i in input_array.split():
    if len(i) <= 3:
        result_array.append(i)

print(result_array)
