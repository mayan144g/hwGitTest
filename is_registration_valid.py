username = input("Enter your username:")
if ('@' in username and '.' in username):
    password = input("Enter your password:")
    if ('#' in password and len(password) >= 8):
        print('These are valid inputs!!')
    else:
        print('Password Invalid')
else:
    print('Username Invalid')