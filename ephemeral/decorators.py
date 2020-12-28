import functools


def stdout_separated(f):
    @functools.wraps(f)
    def inner(*args, **kwargs):
        print("------------------------------------------")
        return f(*args, **kwargs)

    return inner
