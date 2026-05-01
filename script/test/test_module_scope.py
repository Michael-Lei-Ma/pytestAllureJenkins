# -*- coding: utf-8 -*-
def setup_module():
    print("setup_module in TestCase outside!")

def teardown_module():
    print("teardown_module in TestCase outside!")

def test_01():
    print("---用例a执行---")

class TestCase():

    def setup_module(self):
        print("setup_module in TestCase inside!")

    def teardown_module(self):
        print("teardown_module in TestCase inside!")

    def test_02(self):
        print("---用例b执行---")

    def test_03(self):
        print("---用例c执行---")

def test_04():
    print("---用例d执行---")