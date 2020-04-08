# def sayhi():
#     print('say hello')

# def decorator(func):
#     def inner():
#         print("事先装饰一下")
#         #返回接受的函数的调用
#         return func()
#     #返回对inner的调用
#     return inner()

# #调用函数装饰器
# decorator(sayhi)
#使用python语法糖的装饰器形式，装饰器函数需要放到原函数的上面
#再包一层
def decorator1(func):
    print("装饰器一的外面修饰")
    def inner(name):
        print("使用装饰器1事先装饰一下(使用Python语法糖)")
        #返回接受的函数的调用
        return func(name)
    #返回对inner的调用
    return inner
def decorator2(func):
    print("装饰器二的外面修饰")
    def inner(name):
        print("使用装饰器2事先装饰一下(使用Python语法糖)")
        #返回接受的函数的调用
        return func(name)
    #返回对inner的调用
    return inner
@decorator1
@decorator2
def sayhi(name):
    print('say hello,'+ name)

sayhi("lisi")
