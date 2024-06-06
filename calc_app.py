class Calculator:
    def __init__(self):
        pass

    @staticmethod
    def validate_input(input_str):
        try:
            eval(input_str)  # Пытаемся вычислить введенное выражение
            return True
        except Exception:
            return False

    @staticmethod
    def calculate(expression):
        if not Calculator.validate_input(expression):
            return "Некорректный ввод!"

        try:
            result = eval(expression)
            return result
        except Exception as e:
            return f"Ошибка при вычислении: {e}"

    @staticmethod
    def calculate_average(numbers):
        if not numbers:
            return "Список чисел пуст!"

        try:
            average = sum(numbers) / len(numbers)
            return average
        except Exception as e:
            return f"Ошибка при вычислении среднего значения: {e}"


def main():
    calc = Calculator()
    print("Для выхода введите 'exit'")
    while True:
        expression = input("Введите выражение: ")
        if expression.lower() == "exit":
            print("До свидания!")
            break

        result = calc.calculate(expression)
        print("Результат:", result)

        # Добавим обработку новой функции
        if expression.lower() == "average":
            numbers_str = input("Введите числа через пробел: ")
            numbers = [float(num) for num in numbers_str.split()]
            average_result = calc.calculate_average(numbers)
            print("Среднее значение:", average_result)


if __name__ == "__main__":
    main()
