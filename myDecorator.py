from time import perf_counter_ns

def time_function(func):
    def decorated_func(*args, **kwargs):
        start = perf_counter_ns()
        ret = func(*args, **kwargs)
        stop = perf_counter_ns()
        temp = []
        temp += [type(a) for a in args]
        f = lambda x: f"{x}={type(kwargs[x])}"
        temp += list(map(f, kwargs))
        print(f"Function {func.__name__}{*temp,}: time elapsed: {(stop - start)*1e-6:.3f} [ms]")
        return  ret
    return decorated_func

if __name__ == '__main__':
    @time_function
    def test(*x, test='test', test3="vier"):
        print("This is the test function")
    print(test(1, test="test"))