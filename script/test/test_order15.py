# -*- coding: utf-8 -*-

import pytest

import time

value = 0


@pytest.mark.run(order=2)  # 后执行order=2
def test_add2():
    print("I am 2")
    time.sleep(2)
    assert value == 10


@pytest.mark.run(order=1)  # 先执行order=1
def test_add():
    print("I am add")
    global value
    value = 10
    assert value == 10
# @pytest.mark.parametrize()
# def test_1():
#     pass

def get_info():
    print(f'非test命名开头函数，配置文件指定类型运行测试！！！')

