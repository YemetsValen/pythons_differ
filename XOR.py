from functools import reduce
from operator import xor

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
# print(f"Недостающее число: {missing_number}")

# Элемент в единственном экземпляре

def singlNumb(lst):
    res = 0
    for num in lst:
        res = res ^ num
    return res

# Элемент в единственном экземпляре

def singlNumberUniverse(lst):
    '''
     Элемент в единственном экземпляре универсальное решение.
    '''
    bitcCount = [0 for _ in range(64)]
    # делаем подсчёт бит
    for num in lst:
        # делаем + 2 ** 31 чтобы работать с положительными чилами
        # отрицательные в 2-ую систему счисления
        num = num + 2 ** 31
        i = 0
        while num != 0:
            bitcCount[i] += num % 2
            num //= 2
            i += 1

    res = 0
    for i in reversed(range(len(bitcCount))):
        res = res * 2 + bitcCount[i] % 2
    return res - 2 ** 31


# print(singlNumberUniverse([2,2,15,3,3,4,4,5,5,6,6,7,7]))

def singleNumberXORMask(lst):
    numsXor = reduce(xor, lst)
    bitMask = numsXor & (numsXor - 1) ^ numsXor
    A = reduce(xor, filter(lambda num: bitMask & num !=0, lst))
    B = numsXor ^ A
    return A, B

# в массиве находятся случайные целые числа, и одно из них случайно удалено

def find_missing_number(nums):
    n = len(nums)
    expected_xor = 0
    actual_xor = 0

    # XOR всех индексов от 0 до n.
    for i in range(n + 1):
        expected_xor ^= i

    # XOR всех чисел в массиве.
    for num in nums:
        actual_xor ^= num

    # Разница между ожидаемым и фактическим XOR'ами будет удаленным числом.
    missing_number = expected_xor ^ actual_xor

    return missing_number


# в массиве находятся случайные целые числа, и два из них случайно удалено
def find_missing_numbers(nums):
    n = len(nums)
    expected_sum = (n + 2) * (n + 1) // 2
    expected_product = 1
    actual_sum = 0
    actual_product = 1

    for i in range(1, n + 3):
        expected_product *= i

    for num in nums:
        actual_sum += num
        actual_product *= num

    diff_sum = expected_sum - actual_sum
    diff_product = expected_product // actual_product

    # Теперь у нас есть два уравнения:
    # x + y = diff_sum
    # x * y = diff_product

    # Решаем систему уравнений для нахождения x и y.
    for i in range(1, n + 3):
        if (i * (diff_sum - i)) == diff_product:
            missing_numbers = [i, diff_sum - i]
            break

    return missing_numbers