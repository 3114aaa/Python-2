python-2 开始介绍函数

函数方便了程序员，并不会提高程序运行速度，可以理解为复制了一份
## 一、函数的定义与调用
使用def可以定义一个函数

例:

    def printName():
      print("Tom")
    
    printName()#调用printName
    printName()
    
    结果:
    Tom
    Tom
例定义了一个printName函数，我们可以用函数名加()来调用函数，例如printName(),调用的函数会执行定义下的代码，例如printName下的代码时print("Tom"),因此调用后会打印出Tom

## 二、函数的参数与返回值

例(参数):

    def add(a,b):
      print(a+b)
    
    add(1,3)
    结果:4
    add(b=1,a=4)
    结果:5
    
例(返回值):

    def add(a,b):
      return a+b
    
    num =add(1,3)
    结果:num被赋值4
    num =add(b=1,a=4)
    结果:num被赋值5
    
<details><summary>进阶</summary>
<p>
1.我们在定义时，也可以给函数提前赋值，来加强函数的兼容性
<a href="https://github.com/3114aaa/Python-2/blob/main/code/def1.py">代码参考</a>
</p>
<p>。。。</p>
</details>
