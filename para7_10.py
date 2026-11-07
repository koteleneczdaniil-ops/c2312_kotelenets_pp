from c2312_kotelenets_pp.para7_9 import calculate


def checker(*exc_types):
    def checker(func):

        def checker(func, *args, **kwargs):
            try:
                result = func(*args, **kwargs)
            except Exception as exc:
                print(f"we have a problem {exc}")
            else:
                print(f"no problem ! Result = {result}")
            return checker()
        return checker

    @checker(NameError, TypeError, SyntaxError )
    def calculate(expression):
        return eval(expression)


calculate('2+3')