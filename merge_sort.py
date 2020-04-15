#! /c/Users/Joshua/AppData/Local/Programs/Python/Python38/python
import random

def mergeSort(data=[]):
    if len(data) == 1:
        return data
    first_half = data[:len(data)//2]
    second_half = data[len(data)//2:]

    first_half = mergeSort(first_half)
    second_half = mergeSort(second_half)

    return merge(first_half, second_half)

def merge(arr_one=[], arr_two=[]):
    arr_tmp = []
    
    while arr_one and arr_two:
        if arr_one[0] < arr_two[0] :
            arr_tmp.append(arr_two[0])
            arr_two.pop(0)  
        else:
            arr_tmp.append(arr_one[0])
            arr_one.pop(0)

    while arr_one:
        arr_tmp.append(arr_one[0])
        arr_one.pop(0)

    while arr_two:
        arr_tmp.append(arr_two[0])
        arr_two.pop(0)

    return arr_tmp


# TODO
#     Make this function stand alone and add arg parser
# 