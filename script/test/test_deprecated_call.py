# -*- coding: utf-8 -*-
import warnings
import pytest

# ‌无参形式‌：作为上下文管理器包裹可能触发弃用警告的代码块。
def test_deprecated_function():
    with pytest.deprecated_call():
        warnings.warn("This API is deprecated", DeprecationWarning)  # 触发警告
        
# ‌函数参数形式‌：将待测试函数直接作为参数传入，自动验证其调用是否触发弃用警告
def deprecated_api():
    warnings.warn("Use v2 instead", PendingDeprecationWarning)

def test_deprecated_api():
    pytest.deprecated_call(deprecated_api)  # 直接传入函数

def test_deprecated_message():
    with pytest.deprecated_call() as record:
        warnings.warn("Deprecated feature", DeprecationWarning)
        # print(f'{record[0]},{str(record[0].message)}')
    assert "Deprecated feature" in str(record[0].message)  # 检查消息内容

def deprecated_func():
    warnings.warn("Deprecated method", DeprecationWarning, stacklevel=1)
def test_deprecated_func() : # 警告指向调用`deprecated_func()`的代码行而非函数内部
    deprecated_func()

def deprecated_add(a, b):
    warnings.warn("Use new_add()", DeprecationWarning)
    return a + b

def test_deprecated_with_args():
    pytest.deprecated_call(deprecated_add, a=2, b=3)  # 传递参数







