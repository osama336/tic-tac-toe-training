# Recursion
import utils


# def print_x(num):
#     if num == 0:
#         return 0
#     else:
#         print(num ,"",end="")
#         print_x(num - 1)

def print_y(num):
    if num == 1:
        return 1
    else:
        return print_y(num - 1) + num
def feb(num):
    if num == 1:
        return 1
    if num == 0:
        return 0
    else:
        return feb(num - 1 ) + feb(num - 2)

lst = [96,5,2,3,6,7,9]
print(list(sorted(lst, key=lambda x: x % 3)))
# Generator function
# On the fly iterator - one time free the memory but slow speed

# x = [x for x in range (6)]
# print(x)
x = (x for x in range (6))
print(x)

def loop (num):
    for i in range (num):
        yield i
gen = loop(5)

for i  in gen:
    print(i)
# for i  in gen:
#     print(i)

# print(loop(5))  #<generator object loop at 0x0000026669BBFED0>

if __name__ == '__main__':
# print_x(50)
    # print(print_y(5))
    # print(feb(5))
    # print(feb(6))
    # print(feb(7))

# Anonymous Function

# x = feb
# print(type(feb))
# print(type(x))
# print(x(10))
# print(feb(10))

# Anonymous Function

# summ = lambda x, y, z: x+y+z
# print(type(summ))
# print(summ(5,6,7))
#     summa = lambda x, y, *z: x + y + z[0]  #fast access or in direct call
#     print(type(summa))
#     print(summa(5, 6, 9))
#
# # Inner Function
#
# print() #built-in
# x = 5  #global
#
# def outer():
#     # enclosing
#
#     # global x
#
#     x = 6
#     print(x)
#     def inner():
#     #enclosing
#          #global x
#          nonlocal x
#          x = 67
#
#          print(x)
#          def inner01():
#              #enclosing
#              return 0
#
#              def inner02():
#                  # local
#
#                  return 0
#
#          return 0
#
#     inner()
#     print(x)        # 6 --> 67
#     return
#
# print(x)
# print(outer())
# print(x)
    #Clouers
    def paper(cls):
        # The variable in the outer scope is fixed

        def user(name):
            print(f'{name} is making use of the paper {cls}')

        # I returned a reference to the internal function
        return user

    func = paper('Introduction to AI')

    func("Mohammad Issa")
    func("Hiba")
    func("Osama")
    func("Amro")
    func("Anas")

@utils.timer
def loop(n):
    return [i for i in range(10 ** n)]

loop(4)

