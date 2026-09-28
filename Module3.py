
# 10.1
# list = ['Harry', 'Ron', 'Hermione']

# def good():
#     print(list)
    
# good()

# 10.2
# def get_odds():
#     for number in range(10):
#         if number % 2 != 0:
#             yield number

# count = 0
# for value in get_odds():
#     count += 1
#     if count == 3:
#         print(value)
#         break

# 10.3
# from functools import wraps

# def test(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         print("start")
#         result = func(*args, **kwargs)
#         print("end")
#         return result
#     return wrapper
#10.4
# class OopsException(Exception):
#     pass

# try:
#     print("Raising OopsException...")
#     raise OopsException()
# except OopsException:
#     print("Caught an oops")

#12.1
# import zoo

# def hours():
#     print("Open 9-5 daily")
    
 

# zoo.hours()

# #12.2

#  import zoo
# # import zoo as menagerie

# # menagerie.hours()

# #12.3
#  import zoo

# # from zoo import hours

# # def hours():
#  #     print("Open 9-5 daily")

# # hours()

# #12.4

#  import zoo
# # from zoo import hours as info

# # info()

# 12.5

# plain = {'a': 1, 'b': 2, 'c': 3}

# print(plain)

# 12.6

# from collections import OrderedDict

# # Create OrderedDict from plain or the key-value pairs
# fancy = OrderedDict([('a', 1), ('b', 2), ('c', 3)])

# # Print OrderedDict
# print(fancy)