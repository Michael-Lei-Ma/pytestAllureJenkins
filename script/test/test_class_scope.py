# -*- coding: utf-8 -*-

def setup_class(self):
    print("setup_class defined outside TestClass will not be executed!")

def teardown_class(self):
    print("teardown_class defined outside TestClass will not be executed!")


def test_01():
    print("---用例a执行---")

class TestCase():

    def test_02(self):
        print("---用例b执行---")
    def setup_class(self):
        print("setup_class")

    def teardown_class(self):
        print("teardown_class")

    def test_03(self):
        print("---用例c执行---")