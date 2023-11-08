# Login
user = 'andre.perez'
password = 'andre123'

# Db login
user_register = 'andre.perez'
user_password = 'andre321'

#Auth login
user_verify = user == user_register
password_verify = password == user_password
auth_login = user_verify & password_verify

#Show
print(auth_login)