#!/usr/bin/env python3
# coding: UTF-8


from random import randint
from timeit import default_timer as timer
from typing import List
import json


def _lin_search(arr: List[float], x: float) -> (int, int):
    searches = 0
    for i in range(len(arr)):
        searches += 1
        if arr[i] == x:
            return (i, searches)
    return (-1, searches)


def bin_search(arr: List[float], x: float, reverse=False) -> (int, int):
    searches = 0
    l = -1
    r = len(arr)
    x_on_left = (lambda el, mid_val: el < mid_val) if not reverse else (lambda el, mid_val: el > mid_val)
    while r-l > 1:
        searches += 1
        mid = l + (r-l)//2
        if arr[mid] == x:
            return (mid, searches)
        elif x_on_left(x, arr[mid]):
            r = mid
        else:
            l = mid
    return (-1, searches)


def _rand_arr_gen(length, lower=0, upper=100000000):
    i = 0
    while i < length:
        i += 1
        yield randint(lower, upper)


def _create_sorted_array_json(length=1000000, filename='array.json') -> None:
    print('Creating the json test array...')
    start = timer()
    try:
        last = 0
        with open(filename, 'w') as out:
            out.write('[')
            for rand in _rand_arr_gen(length, 0, 100):
                last += rand
                out.write(f'{last}, ')
            out.write(f'{last}]')
    except Exception as e:
        print('Exception in _create_test_array_json')
        print(e)
        exit()
    end = timer()
    print(f'Json array created, time elapsed: {end-start}')


def _create_test_array(length=1000000, read_json=False, save_json=False, filename='array.json') -> (List[int], int):
    """ Create (or read) a sorted array of integers """
    if read_json:
        print('Reading the test array from json...')
        test_arr = _read_array_from_json(filename)
    else:
        print('Creating a test array...')
        test_arr = [x for x in _rand_arr_gen(length)]
        print('Sorting the test array...')
        test_arr.sort()
        if save_json:
            print('Saving array to json...')
            _save_array_to_json(test_arr, filename)
    print(f'\tlen(array) = {len(test_arr)}')
    print('Picking random element...')
    x_index = randint(0, length-1)
    x = test_arr[x_index]
    print(f'\tx = array[{x_index}] = {x}')
    return (test_arr, x)


def _save_array_to_json(array: List[int], filename='array.json') -> None:
    with open(filename, 'w') as out:
        json.dump(array, out)


def _read_array_from_json(filename='array.json') -> List[int]:
    try:
        with open(filename, 'r') as inp:
            array = json.load(inp)
            return array
    except Exception as e:
        print('Exception in _read_array_from_json:')
        print(f'\t{e}')
        exit()


def _main() -> None:
    test_arr, x = _create_test_array()
    start = timer()
    linear = _lin_search(test_arr, x)
    lin_time = timer() - start
    print(f'linear:\n\tindex = {linear[0]};\n\tsearches = {linear[1]};\n\ttime = {lin_time}')

    start = timer()
    binary = bin_search(test_arr, x)
    bin_time = timer() - start
    print(f'binary:\n\tindex = {binary[0]};\n\tsearches = {binary[1]};\n\ttime = {bin_time}')
    print(f'linear time / binary time = {lin_time/bin_time:.3f}')


if __name__ == '__main__':
    _main()
