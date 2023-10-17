def find_missing_number(nums, n):
    xor_sum = 0

    # Вычисляем XOR для чисел от 1 до n
    for i in range(1, n + 1):
        xor_sum ^= i

    # Вычисляем XOR для всех чисел в списке
    for num in nums:
        xor_sum ^= num

    return xor_sum

# Пример использования
n = 10  # Задайте значение n
nums = [2, 5, 1, 8, 9, 3, 10, 4, 7]  # Задайте список чисел с одним удаленным числом

missing_number = find_missing_number(nums, n)
print(f"Недостающее число: {missing_number}")