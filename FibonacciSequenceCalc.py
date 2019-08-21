def print_fibonacci(fib_depth,*args):
    prev = None
    act = None
    if len(args) == 0:
        prev = 0
        act = 1
        print(1, end=", ")
    else:
        prev = args[0]
        act = args[1]
    if fib_depth <= 1:
        return
    elif fib_depth == 2:
        print(calc_fibonacci(prev,act))
    else:
        print(calc_fibonacci(prev,act), end=", ")
    temp = act
    act = prev + act
    prev = temp
    print_fibonacci(fib_depth - 1, prev, act)


def calc_fibonacci(prev,act):
    return prev + act


def main():
    print_fibonacci(20)

if __name__ == '__main__':
    main()
