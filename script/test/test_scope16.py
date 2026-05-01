# -*- coding: utf-8 -*-
# 运行的优先级：module > function > class > method > setup、teardown
def setup_function():
    print("setup_function in TestCase outside!")

def teardown_function():
    print("teardown_function in TestCase outside!")

def setup_module():
    print("setup_module")

def teardown_module():
    print("teardown_module")

def test_01():
    print("---用例a执行---")

class TestCase():
    def setup_method(self):
        print("setup_method")

    def teardown_method(self):
        print("teardown_method")

    def setup_class(self):
        print("setup_class")

    def teardown_class(self):
        print("teardown_class")

    def test_02(self):
        print("---用例b执行---")

    def test_03(self):
        print("---用例c执行---")