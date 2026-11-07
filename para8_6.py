def adder(*args, **kwargs):
    result = 00
    for n in args:
        if type(n)==int or type(n)== bool or type(n)==float:
            result += n
        else:
            try:
                result += float(n)
                continue
            except (ValueError, TypeError):
                pass
            try:
                result += int(n)
                continue
            except (ValueError, TypeError):
                pass

    for m in kwargs.values():
        if type(m) == int or type(m) == bool or type(m) == float:
            result += m
        else:
            try:
                result += float(m)
                continue
            except (ValueError, TypeError):
                pass
            try:
                result += int(m)
                continue
            except (ValueError, TypeError):
                pass
    return result