# создать декоратор который будет считать сколько раз была запущена функция
# и будет выводит это значение после каждого запуска функци

def count(func):
    counters = 0

    def wrapper(*args, **kwargs):
        nonlocal counters
        counters += 1
        print(f' {func.__name__} count : {counters} ')
        return func(*args, **kwargs)

    return wrapper


@count
def double_function(a):
    return a * 2


@count
def triple_function(a):
    return a * 3


if __name__ == "__main__":
    print(list(map(double_function, range(2))))
    print(list(map(triple_function, range(4))))
    print(list(map(double_function, range(10, 11))))
    print(list(map(triple_function, range(12, 13))))
