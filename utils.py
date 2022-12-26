import numpy as np
import sys


def search_etalase(edict: dict, kasus: list) -> list:
    outx = []
    for x in kasus:
        for d in edict:
            if (x.lower() in edict[d]):
                outx.append(d)
    return list(dict.fromkeys(outx).keys())


def is_nan(arr: list) -> list:
    outx = []
    for x in arr:
        if x is None:
            outx.append(True)
        else:
            outx.append(False)
    return outx


def get_zero_rows(arr: list) -> int:
    outx = []
    for i in range(len(arr)):
        if arr[i] == 0:
            outx.append(i)
    return outx


def sum_except_none(arr: list) -> int:
    sum = 0
    for x in arr:
        if isinstance(x, int):
            sum += x
    return sum


def reduksi_matrix(arr: np.ndarray | list) -> list:
    if isinstance(arr, list):
        arr = np.array(arr)
    test = [is_nan(x) for x in arr]
    masked_matrix = np.ma.MaskedArray(arr, mask=test)
    min_r = masked_matrix.min(axis=1, fill_value=sys.maxsize)

    for i in range(arr.shape[0]):
        for j in range(arr.shape[1]):
            if arr[i][j] is not None:
                arr[i][j] -= min_r[i]

    min_c = masked_matrix.min(axis=0, fill_value=sys.maxsize)
    for i in range(arr.shape[0]):
        for j in range(arr.shape[1]):
            if arr[j][i] is not None:
                arr[j][i] -= min_c[i]

    bound = sum_except_none(min_r)+sum_except_none(min_c)
    return arr, bound
