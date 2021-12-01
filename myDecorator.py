from time import perf_counter_ns

def time_function(func):
    def decorated_func(*args, **kwargs):
        start = perf_counter_ns()
        ret = func(*args, **kwargs)
        print(f"Function {func.__name__}(*args, **kwargs): time elapsed: {(perf_counter_ns() - start)*1e-6:.3f} [ms]")
        return  ret
    return decorated_func

@time_function
def test(x):
    print("This is the test function")
    print(x)
    return x*x

# print(test(x))