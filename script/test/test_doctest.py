# -*- coding: utf-8 -*-
def test_custom_data(doctest_namespace):
    # 向命名空间注入变量
    doctest_namespace["shared_data"] = 42
    doctest_namespace["utils"] = {"sum": lambda a, b: a + b}
    # print(f'doctest_namespace is:{doctest_namespace},type is :{type(doctest_namespace)}')

def test_data_injection(doctest_namespace, user_data):
    doctest_namespace["user"] = user_data
    print(f'doctest_namespace is:{doctest_namespace},type is :{type(doctest_namespace)}')