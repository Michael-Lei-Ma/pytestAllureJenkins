# -*- coding: utf-8 -*-


class TestClass:
    def setup_method(self, method):
        # 方法级别的前置操作
        print("执行方法级别的前置操作")

    def teardown_method(self, method):
        # 方法级别的后置操作
        print("执行方法级别的后置操作")

    def test_example1(self):
        # 测试用例1
        print("执行测试用例test_example1")

    def test_example2(self):
        # 测试用例2
        print("执行测试用例test_example2")

    def test_example3(self):
        # 测试用例3
        print("执行测试用例test_example3")
