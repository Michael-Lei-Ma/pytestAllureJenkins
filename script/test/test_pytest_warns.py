# -*- coding: utf-8 -*-
import pytest
import warnings

def sub(a, b):
    if a < b:
        warnings.warn("a must greater b", UserWarning)
    return a - b

# 1、调用函数
def test_sub1():
    pytest.warns(UserWarning, sub, 1, 2)

# # 2、字符串传入函数，官网上这样写，但是我尝试是失败的，提示类型错误。
# def test_sub2():
#     pytest.warns(UserWarning,sub(a=1, b=2))


def test_sub3():
    with pytest.warns(UserWarning) as record:
        sub(1, 2)

    # check that only one warning was raised
    assert len(record) == 1
    # check that the message matches
    assert record[0].message.args[0] == "a must greater b"


def test_case_01():
    print("进入test_case_01函数")
    warnings.warn(UserWarning("手动抛出一个警告"))
    assert 1 == 1

@pytest.mark.filterwarnings(category=UserWarning, message="手动抛出一个警告")
def test_case_02():
    print("进入test_case_02函数")
    warnings.warn(UserWarning("手动抛出一个警告"))
    assert 1 == 1
