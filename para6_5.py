try:
    try:
        print('start code')
        print(error)
        print('no error')
    except SyntaxError:
        print('Wrong syntax')
except NameError as error:
    print(error)
    