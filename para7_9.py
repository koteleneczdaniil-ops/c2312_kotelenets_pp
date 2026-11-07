def checker(func):

    def checker(func, *args, **kwargs):
         try:
             result = func(*args, **kwargs)
         except Exception as exc:
             print(f"we have a problem {exc}")
         else:
             print(f"no problem ! Result = {result}")
    return checker
@checker
def calculate(expression):
    return eval(expression)


calculate("2+2")

