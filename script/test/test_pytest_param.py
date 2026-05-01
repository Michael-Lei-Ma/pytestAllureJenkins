# -*- coding: utf-8 -*-
import pytest

@pytest.mark.parametrize(
    "a, b, expected",
    [
        pytest.param(1, 2, 3),
        pytest.param(5, -3, 2),
    ]
)
def test_add(a, b, expected):
    assert a + b == expected

@pytest.mark.parametrize(
    "value, expected",
    [
        pytest.param(10, 15, marks=pytest.mark.xfail(reason="未实现")),
        pytest.param(5, 5, marks=pytest.mark.xfail(raises=AssertionError)),
        pytest.param(3, 3),  # 正常测试
    ]
)
def test_increment(value, expected):
    assert value + 1 == expected  # 第一个参数组合会触发 XFAIL

@pytest.mark.parametrize(
    "input, output",
    [
        pytest.param("hello", "HELLO", id="lowercase转大写"),
        pytest.param("WORLD", "WORLD", id="大写保持不变"),
    ]
)
def test_uppercase(input, output):
    assert input.upper() == output

@pytest.mark.parametrize(
    "data",
    [
        pytest.param([1, 2, 3], marks=[pytest.mark.slow, pytest.mark.integration]),
        pytest.param([], marks=pytest.mark.skip(reason="空列表暂不支持")),
    ]
)
def test_process_data(data):
    assert data[0]+data[1] == data[2]
    print(f'北京好！！！')


# 定义参数生成函数
def generate_params():
    params = []
    for x in [1, 2]:
        for y in [3, 4]:
            # 动态生成 ID
            test_id = f"x={x}-y={y}"
            params.append(pytest.param(x, y, id=test_id))
    return params

# 使用动态参数化
@pytest.mark.parametrize(
    "x, y",
    generate_params()
)
def test_multiple_params(x, y):
    assert x + y > 0

from contextlib import contextmanager
import pytest


@contextmanager
def does_not_raise():
    yield


@pytest.mark.parametrize(
    "example_input,expectation",
    [
        (3, does_not_raise()),
        (2, does_not_raise()),
        (1, does_not_raise()),
        (4, pytest.raises(ZeroDivisionError)),
    ],
)
def test_division(example_input, expectation):
    """Test how much I know division."""
    with expectation:
        assert (6 / example_input) is not None