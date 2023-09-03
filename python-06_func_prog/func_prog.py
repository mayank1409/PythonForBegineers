def mult_by_2(data):
    return data*2


def mult_by_3(data):
    return data*3


def do_this_and_print(func, data):
    print(func(data))

do_this_and_print(mult_by_2, 125)
do_this_and_print(mult_by_3, 125)
func_example_ref = mult_by_2
print(func_example_ref(23))


do_this_and_print(lambda data:data*5, 100)
do_this_and_print(lambda data:data*data, 125)
do_this_and_print(lambda data:data**3, 125)
do_this_and_print(lambda data:len(data), 'Hello')
