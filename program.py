def calculator():
    print("Введите математическое выражение (например, 2 + 3 * (5 - 2)):")

    while True:
        expression = input("Выражение: ")
        try:
            result = eval(expression)
            print(f"Результат: {result}")
        except Exception as e:
            print(f"Ошибка: {e}")

        next_calculation = input("Хотите выполнить еще один расчет? (да/нет): ")
        if next_calculation.lower() != 'да':
            break


if __name__ == "__main__":
    calculator()
