python-2 开始介绍函数

函数方便了程序员，并不会提高程序运行速度，可以理解为复制了一份
## 一、函数的定义
使用def可以定义一个函数

例一:

    def printName():
      print("Tom")
    
    printName()#调用printName
    printName()
    
    结果:
    Tom
    Tom
例一定义了一个printName函数，我们可以用函数名加()来调用函数，例如printName(),调用的函数会执行定义下的代码，例如printName下的代码时print("Tom"),因此调用后会打印出Tom
