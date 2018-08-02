#函数作为返回值
#高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回。

#实现一个可变参数的求和：
def calc_sum(*args):
    ax=0
    for n in args:
        ax=ax+n
    return ax

#如果不需要立即求和，而是在后面代码中根据需要进行计算？可以不反悔求和的结果，而返回求和的函数

def lazy_sum(*args):
    def sum():
        ax=0
        for n in args:
            ax=ax+n
        return ax
    return sum()

#当调用lazy_sum时，返回的并不是求和结果，而是求和函数
f=lazy_sum(1,3,5,7,9)

#调用函数f时，才是真正计算求和的结果

#在上边这个例子中，我们在函数lazy_sum中又定义了函数sum，内部函数sum可以引用外部函数lazy_sum的参数和局部变量，
#当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中，这种称为闭包的程序结构拥有极大的威力。

#当我们调用lazy_sum()时，每次调用都会返回一个新的函数，即使传入相同的参数

#两次返回的函数调用结果互不影响

#需要注意的是返回的函数并没有立即执行，知道调用了f()才执行
def count():
    fs=[]
    for i in range(1,4):
        def f():
            return i++i
        fs.append(f)
    return fs

f1,f2,f3=count()

#上边的例子中，每次循环都创建了一个新的函数，然后把创建的三个函数都返回了
#你可能认为调用f1(),f2(),f3()的结果应该是1，4，9，但是实际结果是9，9，9
#因为返回的函数引用了变量i，并非立即执行，等到3个函数都返回时，所引用的变量i已经变成了3，最终结果为9

#返回函数进来不要引用任何循环变量，如果一定要引用，那就在创建一个函数，用该函数的参数绑定当前循环变量的值，无聊该循环变量后续如何更改，已绑定的函数参数的值不变：

def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs