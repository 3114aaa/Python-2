def add(a=1, b=2):
    print(a + b)


add(1)  # b没有赋值就会使用你直接定义的2
add(b=1)  # 我们也可以直接赋值与b，让a默认
