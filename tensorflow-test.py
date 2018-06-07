# import tensorflow as tf
# hello = tf.constant('Hello, TensorFlow!')
# sess = tf.Session()
# print(sess.run(hello))

# a = tf.constant(10)
# b = tf.constant(32)
# print(sess.run(a + b))

# print("Please input your name: ")

'''


def quadratic(a, b, c):
    return b * b - 4 * a * c


print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))

total = 0

for x in range(2, 20, 2):
    total = total + x
print('sum of 2 to 20 is %d' % total)

total2 = 0
n = 20
while n > 0:
    total2 = total2 + n
    n = n - 2
print('sum of 2 to 20 is %d' % total2)

name_list = ['Adam', 'Bob', 'Dove']

for person_name in name_list:
    print('Hello, your name is %s' % person_name)

print('班级成绩单如下：')
name_grade = {'Allen': 90, 'Belly': 95, 'Helen': 98, 'Kelly': 80}

print('Allen : %s' % name_grade['Allen'])
print('Belly : %s' % name_grade['Belly'])
print('Helen : %s' % name_grade['Helen'])
print('Kelly : %s' % name_grade['Kelly'])

print(name_grade)

name_str = input("请输入你要查询的学生姓名：")

grade = name_grade.get(name_str, -1)

if grade == -1:
    print('不存在姓名为%s的学生' % name_str)
else:
    print('你查询的%s的成绩是%s' % (name_str, grade))


# print("Your name is")
# print(name)


# 利用递归函数移动汉诺塔:
def move(n, a, b, c):
    if n == 1:
        print('move', a, '-->', c)
    else:
        move(n - 1, a, c, b)
        move(1, a, b, c)
        move(n - 1, b, a, c)


move(4, 'A', 'B', 'C')


# 利用递归函数计算阶乘
# N! = 1 * 2 * 3 * ... * N
def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


print('fact(1) =', fact(1))
print('fact(5) =', fact(5))
print('fact(10) =', fact(10))


def trim(s):
    if len(s) == 0:
        print('Input string is null or has only backspace character')
        return s
    if s[0] == ' ':
        return trim(s[1:])
    if s[-1] == ' ':
        return trim(s[:-1])

    print(s)
    return s


trim('')
trim('  ')
trim('    hello')
trim('world    ')


def findMinAndMax(L):
    if len(L) == 0:
        return None, None

    max = min = L[0]
    for x in L:
        if x > max:
            max = x
        elif x < min:
            min = x

    return min, max


if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')

from functools import reduce


def str_normalize(name):
    if len(name) != 0:
        if name.isalpha():
            print('string len is %d' % len(name))
            return name[0].upper() + name[1:len(name)]
        else:
            return name
    else:
        return name


L1 = ['', '1A2', 'adam', 'LISA', 'barT']
L2 = list(map(str_normalize, L1))
print(L2)


def mul(x, y):
    return x * y


def prod(data_list):
    return reduce(mul, data_list)


print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))

if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def fn(x, y):
    return x * 10 + y


def char2num(s):
    return DIGITS[s]


def str2int(s):
    if s.isdigit():
        return reduce(fn, map(char2num, s))
        # return reduce(lambda x, y: x * 10 + y, map(char2num, s))
    else:
        print('the string you input is invalid, not all digital characters')
        return None


print('Input string is \'379\', string to integer result is %d' % str2int('379'))
print('Input string is \'A379\', string to integer result is None')


def not_empty(s):
    return s and s.strip()


print('New list after filter is ')
print(list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])))


# 结果: ['A', 'B', 'C']


def is_palindrome(n):
    return str(n) == str(n)[::-1]


output = filter(is_palindrome, range(1, 1000))
print('palindrome in 1~1000 is :', list(output))

f = open('C:\\Users\\linchao\\AnacondaProjects\\gbk_test.txt', 'r', encoding='gbk', errors='ignore')
print(f.read())

from datetime import datetime
import os

pwd = os.path.abspath('.')

print('      Size     Last Modified  Name')
print('------------------------------------------------------------')
print('current work directory is %s ' % pwd)

for f in os.listdir(pwd):
    fsize = os.path.getsize(f)
    mtime = datetime.fromtimestamp(os.path.getmtime(f)).strftime('%Y-%m-%d %H:%M')
    flag = '/' if os.path.isdir(f) else ''
print('%10d  %s  %s%s' % (fsize, mtime, f, flag))

# search_file_by_name('.', 'Anaconda')
search_path = '.'
search_name = 'selfcheck'


def search_file_by_name(file_path, file_name):
    for file in os.listdir(file_path):
        if os.path.isdir(file):
            print('current search path is %s' % os.path.abspath(file))
            search_file_by_name(file, file_name)
        else:
            if file.find(file_name) == -1:
                print('current search path is %s' % os.path.abspath(file))
                print('Can\'t find file %s ' % file_name)
            else:
                print('file that has %s is found , the full file name is %s' % (file_name, file))
                found_file_abs_path = os.path.abspath(file)
                print('file absolute path is %s' % found_file_abs_path)
                print('current work directory is %s' % os.getcwd())
                print('Orig search path is %s' % os.path.abspath(search_path))
                # file_str_index = found_file_abs_path.find(os.path.abspath(search_path))
                # print('file_str_index = %d ' % file_str_index)
                print('file relative path to search directory is %s' % (found_file_abs_path)[
                                                                       len(os.path.abspath(search_path)):])


# absolute_path = search_file_by_name(search_path, search_name)
search_file_by_name(search_path, search_name)
# if absolute_path is None:
#    print('Can\'t find file ')
# else:
#    print('file relative path to search directory is %s' % absolute_path[absolute_path.find(os.path.abspath('.')):])


from tkinter import *
import tkinter.messagebox as messagebox


class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alertButton = Button(self, text='Hello', command=self.hello)
        self.alertButton.pack()

    def hello(self):
        name = self.nameInput.get() or 'world'
        messagebox.showinfo('Message', 'Hello, %s' % name)


app = Application()
# 设置窗口标题:
app.master.title('Hello World')
# 主消息循环:
app.mainloop()

'''

# !/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import csv


with open(r'C:\Users\linchao\.spyder\Normal-Cap-SNR\Results\D65-Cap_summary.csv', mode='r', newline='') as fdReadCSV:
    reader = csv.reader(fdReadCSV)
    rowSel = 0
    resultStr = []
    fdWriteCSV = open(r'C:\Users\linchao\.spyder\Normal-Cap-SNR\result.csv', mode='w', newline='')
    writer = csv.writer(fdWriteCSV)
    for row in reader:
        if (rowSel >= 5 and rowSel <= 10):
            print('Line %02d, colume %02d :  %s ' % (rowSel, 9, row[9]))
            resultStr.append(row[9])
            #rst2 = []
            #rst2.extend(row[9])
            #writer.writerow(rst2)
            writer.writerow(resultStr)
            resultStr.clear()
        rowSel = rowSel + 1
        # print(row)
    fdWriteCSV.close()


