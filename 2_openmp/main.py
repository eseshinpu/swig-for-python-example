import time

from multithread import countNumber, countNumberUsingOpenmp, sleep, sleepUsingOpenmp


def count_num_py(num):
    start = time.time()
    array = []
    for i in range(num):
        array.append(i * i)
    elapsed_time = time.time() - start
    return elapsed_time


def count_num_cpp(num):
    start = time.time()
    countNumber(num)
    elapsed_time = time.time() - start
    return elapsed_time


def count_num_cpp_openmp(num):
    start = time.time()
    countNumberUsingOpenmp(num)
    elapsed_time = time.time() - start
    return elapsed_time


def sleep_py(num):
    start = time.time()
    for i in range(num):
        time.sleep(i)
    elapsed_time = time.time() - start
    return elapsed_time


def sleep_cpp(num):
    start = time.time()
    for i in range(num):
        sleep(i)
    elapsed_time = time.time() - start
    return elapsed_time


def sleep_cpp_openmp(num):
    start = time.time()
    for i in range(num):
        sleepUsingOpenmp(i)
    elapsed_time = time.time() - start
    return elapsed_time


def cout_num_time_measurement():
    count_num = 1000000
    print("count num: {}".format(count_num))
    # normal python loop
    py_sec = count_num_py(count_num)
    # print("py finish.")
    cpp_sec = count_num_cpp(count_num)
    # print("cpp finish.")
    cpp_openmp_sec = count_num_cpp_openmp(count_num)
    # print("cpp openmp finish.")

    # show time
    print("python normal loop: {:.10f} sec".format(py_sec))
    print("cpp normal loop: {:.10f} sec".format(cpp_sec))
    print("cpp openmp loop: {:.10f} sec".format(cpp_openmp_sec))


def sleep_time_measurement():
    sleep_num = 7
    print("max sleep time: {} sec".format(sleep_num))
    # normal python loop
    py_sec = sleep_py(sleep_num)
    # print("py finish.")
    cpp_sec = sleep_cpp(sleep_num)
    # print("cpp finish.")
    cpp_openmp_sec = sleep_cpp_openmp(sleep_num)
    # print("cpp openmp finish.")

    # show time
    print("python normal loop: {:.10f} sec".format(py_sec))
    print("cpp normal loop: {:.10f} sec".format(cpp_sec))
    print("cpp openmp loop: {:.10f} sec".format(cpp_openmp_sec))


def main():
    print("---simple number count---")
    cout_num_time_measurement()
    print("---simple sleep---")
    sleep_time_measurement()


if __name__ == "__main__":
    main()
