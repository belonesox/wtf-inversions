#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=W0107, C0330, C0301, W0621, E1101
'''
Генератор тестовых данных.
'''

def main():
    size = 100000
    with open('test04.txt', 'w') as lf:
        for i in range(size):
            v = size - i
            lf.write("%d\n" % v)
            if i < size-1:
                lf.write(" ")
        lf.write("\n")
                
if __name__ == "__main__":
    main()
    pass
