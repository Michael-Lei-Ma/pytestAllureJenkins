# -*- coding: utf-8 -*-

def setup_method(self):
    print("setup_method defined outside TestClass will not be executed!")

def teardown_method(self):
    print("teardown_method defined outside TestClass will not be executed!")

def test_01():
    print("---用例a执行---")

class TestCase():
    def setup_method(self):
        print("setup_method")

    def teardown_method(self):
        print("teardown_method")

    def test_02(self):
        print("---用例b执行---")

    def test_03(self):
        print("---用例c执行---")