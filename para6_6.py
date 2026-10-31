def checker(var1):
    if type(var1) != str:
        raise TypeError(f'Sorry, we cant work with {type(var1)}, we need a str type!')
    else:
        return var1


f_var = 'text'
s_var = 10
checker(f_var)
checker(s_var)