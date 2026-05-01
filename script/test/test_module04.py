# -*- coding: utf-8 -*-
def test_example1():
    # 测试用例1
    print("执行测试用例test_example1")

def test_example2():
    # 测试用例2
    print("执行测试用例test_example2")

def setup_function():
    # 函数级别的前置操作
    print("执行函数级别的前置操作")

def teardown_function():
    # 函数级别的后置操作
    print("执行函数级别的后置操作")

def setup_module():  # ---> setup
    # 前置操作
    print("执行模块级别前置操作")

def teardown_module():  # ---> teardown
    # 后置操作
    print("执行模块级别后置操作")

