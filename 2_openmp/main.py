import time

from multithread import countNumber, countNumberUsingOpenmp


def stop_watch(func):
    """Time measurement decorator

    reference：https://qiita.com/hisatoshi/items/7354c76a4412dffc4fd7
    """
    @wraps(func)
    def wrapper(*args, **kargs):
        start = time.time()
        result = func(*args, **kargs)
        elapsed_time = time.time() - start
        print(f"{func.__name__} took {elapsed_time}秒かかりました")
        return result
    return wrapper


def count_num_py(num):
    start = time.time()
    for i in range(num):
        print(i)
    elapsed_time = time.time() - start
    return elapsed_time


def count_num_cpp(num):
    start = time.time()
    countNumber(100)
    elapsed_time = time.time() - start
    return elapsed_time


def count_num_cpp_openmp(num):
    start = time.time()
    countNumberUsingOpenmp(100)
    elapsed_time = time.time() - start
    return elapsed_time


def main():
    loop_num = 100000
    # normal python loop
    py_sec = count_num_py(loop_num)
    cpp_sec = count_num_cpp(loop_num)
    cpp_openmp_sec = count_num_cpp_openmp(loop_num)

    # show time
    print("python normal loop: {} sec".format(py_sec))
    print("cpp normal loop: {} sec".format(cpp_sec))
    print("cpp openmp loop: {} sec".format(cpp_openmp_sec))


if __name__ == "__main__":
    main()
