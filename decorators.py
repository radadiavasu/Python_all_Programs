#############################################################
# Program : 6
#############################################################
# (1)
# def add_all(a1, a2, a3, a4):
#     return a1+a2+a3+a4
# (1)
# vals = (1, 5, 7, 9)
# print(add_all(*vals))

# (2)
# vals = {'a1': 1, 'a2': 5, 'a3': 7, 'a4': 9}
# print(add_all(a1=vals['a1'], a2=vals['a2'], a3=vals['a3'], a4=vals['a4'],))

# (3)
def add_all(*args): # accept any number of single arguments
    return(sum(args))

# print(add_all(1, 3, 7, 9))

def pretty_print(**kwargs): # accept any number of named arguments
    for k, v in kwargs.items():
        print(f'For {k} we have {v}.')

pretty_print(username='vasu123', access_level='admin')


#############################################################
# Program : 5
#############################################################

# import functools

# user = {'username': 'vasu123', 'access_level': 'user'}

# def user_has_permission(access_level):
#     def user_has_permission(func):
#         @functools.wraps(func)
#         def secure_func(panel):
#             if user.get('access_level') == access_level:    
#                 return func(panel)
#         return secure_func
#     return user_has_permission

# @user_has_permission('admin')
# def my_function(panel):
#     """
#     Allowsus to retrieve the password for the admin panel.
#     """
#     return f'Password for {panel} panel is 1234.'


# print(my_function.__name__)
# print(my_function('movies'))


#############################################################
# Program : 4
#############################################################

# import functools

# user = {'username': 'vasu123', 'access_level': 'admin'}

# def user_has_permission(func):
#     @functools.wraps(func)
#     def secure_func(panel):
#         if user.get('access_level') == 'admin':    
#             return func(panel)
#     return secure_func

# @user_has_permission
# def my_function(panel):
#     """
#     Allowsus to retrieve the password for the admin panel.
#     """
#     return f'Password for {panel} panel is 1234.'


# print(my_function.__name__)
# print(my_function('movies'))


#############################################################
# Program : 3
#############################################################

# import functools

# user = {'username': 'vasu123', 'access_level': 'admin'}

# def user_has_permission(func):
#     @functools.wraps(func)
#     def secure_func():
#         """
#         Hey what's going on.
#         """
#         if user.get('access_level') == 'admin':    
#             return func()
#         raise RuntimeError
#     return secure_func

# @user_has_permission
# def my_function():
#     """
#     Allowsus to retrieve the password for the admin panel.
#     """
#     return 'Password for admin panel is 1234.'

# @user_has_permission
# def another():
#     pass

# print(my_function())
# print(my_function.__name__)
# print(another.__name__)


#############################################################
# Program : 2
#############################################################

# user = {'username': 'vasu123', 'access_level': 'admin'}

# def user_has_permission(func):
#     def secure_func():
#         """
#         Hey
#         """
#         if user.get('access_level') == 'admin':    
#             return func()
#         raise RuntimeError
#     return secure_func

# @user_has_permission
# def my_function():
#     """
#     Allowsus to retrieve the password for the admin panel.
#     """
#     return 'Password for admin panel is 1234.'
# @user_has_permission
# def another():
#     pass

# print(my_function())
# print(my_function.__name__)
# # print(my_function.__name__)
# print(my_function.__doc__)


#############################################################
# Program : 1
#############################################################

# user = {'username': 'vasu123', 'access_level': 'admin'}

# def user_has_permission(func):
#     def secure_func():
#      if user.get('access_level') == 'admin':
#         return func()
#      raise RuntimeError
#     return secure_func

# def my_function():
#     return 'Password for admin panel is 1234.'

# my_secure_function= user_has_permission(my_function)

# print(my_secure_function())