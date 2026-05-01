# -*- coding: utf-8 -*-

import pytest

import time

value = 0


@pytest.mark.run(order=2)  # 后执行order=2
def test_add2():
    print("我是order_2.py文件！！")
    time.sleep(2)
    assert value == 10


@pytest.mark.run(order=1)  # 先执行order=1
def test_add():
    print("I am add  name_2.py file！")
    global value
    value = 10
    assert value == 10