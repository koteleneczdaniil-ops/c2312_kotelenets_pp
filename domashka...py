def safe_calc(func):
  def wrapper(expression):
    try:
      return func(expression)
    except Exception as e:
      return f"Помилка! ({e})"

  return wrapper


@safe_calc
def calculate(expression):
  return eval(expression)

user_input = input("Введіть приклад: ")
print(calculate(user_input))