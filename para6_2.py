try:
    print('start code')
    print(10/0)
    print('no error')
except NameError:
    print('we have a problem with the name')
print('code after capsule')
except ZeroDivisionError:
print('we have a problem with division by 0')

print('code after capsule')