print("Hello World")


def print_hello_world_twice() :
    print("Hello World 1")
    print("Hello World 2")
    print("Hello World 3")


def print_hello_world_n_times(n) :
   for i in range (1,n+1):
        print("Hello World ", i)
    

print_hello_world_twice()
print_hello_world_n_times(4)
