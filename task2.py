def password_level(x):
    if len(x) < 6:
        print('Invalid password')
    elif x.isdigit() or x.isalpha():
        print('Unreliable password')
    elif (x.isdigit() and x.lower()) or (x.isalpha() and x.lower()) or (x.isdigit() and x.upper()) or (x.isalpha() and x.upper()):
        print('Weak password')
    else:
        print('Strong password')

password_level(input())
