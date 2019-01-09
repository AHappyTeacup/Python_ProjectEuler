import time


def timed(my_func):
    """Wrapper to print the runtime of a function"""
    def timed_func(*args, **kwargs):
        start_time = time.time()
        result = my_func(*args, **kwargs)
        end_time = time.time()
        run_time = end_time - start_time
        print "runtime: %s" % run_time
        return result
    return timed_func
