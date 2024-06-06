from flask import Flask, request, jsonify

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

app = Flask(__name__)
calc = Calculator()

@app.route('/')
def home():
    return "Welcome to the Calculator API!"

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    expression = data.get('expression')
    result = calc.calculate(expression)
    return jsonify({"result": result})

@app.route('/average', methods=['POST'])
def average():
    data = request.get_json()
    numbers = data.get('numbers')
    result = calc.calculate_average(numbers)
    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
