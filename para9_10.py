class AgeError(Exception):
    def __str__(self):
        return f'you are too young'

def check_age(age, limit_value):
    if age > limit_value:
        return 'you are old enough'
    else:
        raise AgeError(age)


age = int(input('age: '))
check_age(age, 18)