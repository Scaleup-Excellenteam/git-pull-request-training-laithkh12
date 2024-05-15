import time


def running_2000(f, *param1, **param2):
    start = time.perf_counter()
    f(*param1, **param2)
    return time.perf_counter() - start



print(running_2000(print, "Hello"))
print(running_2000(zip, [1, 2, 3], [3, 4, 5]))
print(running_2000("Hi {name}".format, name="Bug"))
