from copy import deepcopy

import numpy as np

from u_numpy import notInplace, inplace


def not_inplace_arr_dim1(array):
    print("---not inplace---")
    print("before: ", array)
    notInplace(array)
    print("after: ", array)


def inplace_arr_dim1(array):
    print("---inplace---")
    print("before: ", array)
    notInplace(array)
    print("after: ", array)


if __name__ == "__main__":
    arr = np.array([0, 0, 0], dtype=np.float)
    # not inplace
    not_inplace_arr_dim1(deepcopy(arr))
    # inplace
    inplace_arr_dim1(deepcopy(arr))
