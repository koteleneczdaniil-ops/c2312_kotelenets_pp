def checker(func, *args, **kwargs):
    try:
        result = func(*args, **kwargs)
    except Exception as exc:
        print(f"we have a problem {exc}")
    else:
        print(f"no problem ! Result = {result}")


def calculate(expression):
    return eval(expression)


checker(calculate,"2+2")
