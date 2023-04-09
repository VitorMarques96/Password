password = input('Register you password: ')
print('Password Registered!')
password2 = input('Enter your password: ')

if password == password2:
    print('Permited Acess')
else:
    print('Access Denied')
    print('Please try again')