# # -*- coding: utf-8 -*-
#
# import pytest
#
#
# # myfunc函数会抛出一个异常，
#
# def myfunc():
#     raise ValueError("Exception 123 raised")
#
#
# def test_match():
#
#
#     # pytest.raises()函数，
#
#     # 可以用元组的形式传递参数，只需要触发其中任意一个即可。
#
#     # 通过match可以设置通过正则表达式匹配异常。
#
#     with pytest.raises((ValueError, RuntimeError), match=r'.* 123 .*') as ve:
#         print(f'ValueError : {ValueError}')
#         myfunc()
#         print(f'Exception : {myfunc()}')
#         # 说明：myfunc()抛出的异常被match设置的字符串匹配到
#
#         # 也就是捕获到了该异常。
#
#         # 然后下面是断言，123是否包含在捕获异常的说明中。
#
#
#         assert "123" in str(ve.value)
#
#
#
#
# def test_exception_value():
#
#     with pytest.raises(ZeroDivisionError) as zero:
#
#         1 / 1  # 此处可以是方法，也可以是表达式
#
#         # print(zero) <ExceptionInfo ZeroDivisionError('division by zero') tblen=1>
#
#         # print(zero.tb)# <traceback object at 0x0000021B6068BD48>
#
#         # print(zero.typename) # 字符串"ZeroDivisionError"
#
#         # print(zero.type) # 异常类型<class 'ZeroDivisionError'>
#
#         print(zero.traceback)
#         print(str(zero.value))
#
#         assert "division by zero" in str(zero.value)
#
#         assert zero.type == ZeroDivisionError
#
#         assert zero.typename == "ZeroDivisionError"
# import warnings
# # 1、 完全匹配
# def test_match1():
#     with pytest.warns(UserWarning, match='must be 0 or None'):
#         warnings.warn("value must be 0 or None", UserWarning)
# # 2、部分匹配
# def test_match2():
#     with pytest.warns(UserWarning, match=r'must be \d+$'):
#         warnings.warn("value must be 44", UserWarning)
# # 3、不匹配
# def test_match3():
#     with pytest.warns(UserWarning, match=r'must be \d+$'):
#         warnings.warn("this is not here", UserWarning)
#
# # 不匹配时，执行测试就会失败。
# # Failed: DID NOT WARN. No warnings of type ...UserWarning... was emitted...
