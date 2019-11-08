#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=W0107, C0330, C0301, W0621, E1101
'''
Решение 03_3

Дана последовательность целых чисел из диапазона (-1000000000 .. 1000000000). 
Длина последовательности не больше 1000000. Числа записаны по одному в строке. 
Количество чисел не указано. 
Пусть количество элементов n, и числа записаны в массиве a = a[i]: i из [0..n-1]. 
Требуется напечатать количество таких пар индексов (i,j) из [0..n-1], что (i < j и a[i] > a[j]). 

Указание: количество инверсий может быть больше 4*1000000000 - используйте int64_t. 
'''
# Подозреваю опять неукладку по памяти или скорости. Но начнем с простых алгоритмов.

import sys
#import cProfile

DEBUG = False
# DEBUG = True
TEST_NUM = None

TESTS = [
("""
4
3
2
1
""", 6),    
(
"""
1
2
3
4
""", 0),
("""
3
2
2
""", 2),
]

TESTS_LINES = [lines.strip().split("\n") for lines in [test[0] for test in TESTS] ]

def fakeinput():
    global TEST_NUM 
    for line in TESTS_LINES[TEST_NUM-1]:
        yield line

# Ужасно некрасиво, но от отчаяния
MAX_SIZE = 1000000
if DEBUG:
    MAX_SIZE = 10

array = [0]*MAX_SIZE
 

def inversion_count_using_mergesort(left, right): 
    '''
Основное соображение для рекурсивного подсчета инверсий:
если разбить произвольным образом массив на два подмассива
то число инверсий в нем, есть 
* сумма инверсий в подмассивах (вычисляем рекурсивно),
* плюс инверсии при слиянии (вычисляем при мерджсорте) 
    '''
    global array
    inversion_count = 0
    if left < right: 
        mid = (left + right) >> 1
        inversion_count += inversion_count_using_mergesort(left, mid) 
        inversion_count += inversion_count_using_mergesort(mid + 1, right) 

        i = left        
        j = wtf = mid + 1     
        ic_ = 0

# 0 0 1 1
# 2 2 3 1
# --> 0 3 1 0
# --> 1 4 2 2
# 0 1 3 3
# 0 1 3 3


        # gen_left = iter(((i, a) for (i, a) in enumerate(array[left: mid+1], start=left)))
        # try:
        #     i, al = next(gen_left) 
        #     for ar in array[mid+1: right+1]:
        #         if al<=ar:
        #             i, al = next(filter(lambda a: a[1]>ar, gen_left))
        #         ic_ += wtf - i
        # except StopIteration:
        #     pass


        try:
            for ar in iter(array[mid+1: right+1]):
                while (array[i] <= ar):
                    i += 1
                    if i > mid:
                        raise Exception('1')    
                ic_ += wtf - i  
        except Exception:
            pass

        # try:
        #     for ar, (i, al) in zip(array[mid+1: right+1], gen_left):
        #         while(al<=ar):
        #             (i, al) = next(gen_left)
        #         print ("-->", i, al, ar, ic_)
        #         ic_ += wtf - i  
        # except StopIteration as ex_:
        #     pass


        # for ar in array[mid+1: right+1]:
        #     while (array[i] <= ar and i <= mid):
        #         i += 1
        #     if i > mid:
        #         break    
        #     print ("-->", i, array[i], ar, ic_)
        #     ic_ += wtf - i  

        # 0 0 1 1
        # 2 2 3 1
# --> 0 3 1 0
# --> 0 3 2 2
# 0 1 3 4
        # 0 1 3 4


        # print (left,mid,right,ic_)





        # # for ar in gen_right:
        #     while (array[i] <= ar and i <= mid):
        #         i += 1
        #     if i > mid:
        #         break    
        #     ic_ += wtf - i  



        # for ar in array[mid+1: right+1]:
        # # for ar in gen_right:
        #     while (array[i] <= ar and i <= mid):
        #         i += 1
        #     if i > mid:
        #         break    
        #     ic_ += wtf - i  


        # for ar in array[mid+1: right+1]:
        #     for ii, al in enumerate(array[i:mid+1], start=i):
        #         i = ii
        #         if al > ar:
        #             ic_ += wtf - i  
        #             break
        #     if i >= mid:
        #         break    

        # for ar in array[mid+1: right+1]:
        #     while (array[i] <= ar and i <= mid):
        #         i += 1
        #     if i > mid:
        #         break    
        #     ic_ += wtf - i  
                
        inversion_count += ic_
        array[left: right+1] = sorted(array[left: right+1]) 

    return inversion_count 

 
# «Проигрываем» реальные или фейковые входные данные 
def playinput(instream=sys.stdin):
    n = 0
    global array    
    try: 
        for line in instream:
            array[n] = int(line, 10)
            n += 1 
    except:
        pass        
    inversion_count = inversion_count_using_mergesort(0, n-1) 
    return inversion_count    

def main():
    global TEST_NUM 
    if DEBUG:
        for TEST_NUM in range(1, len(TESTS)+1):
            res = playinput(fakeinput())
            if res != TESTS[TEST_NUM-1][1]:
                print("TEST_NUM=", TEST_NUM)
                print("Waiting =", TESTS[TEST_NUM-1][1])
                print("Got =", res)
                assert(False)   

    else:
        print(playinput())

if __name__ == "__main__":
    main()
    #cProfile.run('main()')
    # gen1 = iter([1,2,3,4,5])
    # s=next(filter(lambda a: a>3, gen1))
    # print(s)
    # gen2 = iter(['a','b','c','d'])
    # for g1,g2 in zip(gen1,gen2):
    #     g3 = next(gen1)
    #     print(g1,g2)

    pass
