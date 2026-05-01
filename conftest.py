# -*- coding: utf-8 -*-
import pytest
import uuid

@pytest.fixture
def data():
    return [1, 2, 3, 4, 5, 6]


@pytest.fixture(autouse=True,scope='session')  # autouse自动调用
def auto_print():
    print("这里是自动调用的前置")
    yield
    print("这里是自动调用的后置")

@pytest.fixture(params=[1,2,3],ids=['zero','one','two'])
def params(request):
    return request.param
# # 在 conftest.py 中注册
# pytest.register_assert_rewrite("test_register_assert_rewrite.test_add")

@pytest.mark.parametrize("input,expected", [(2, 4), (3, 9)])
def test_square(doctest_namespace, input, expected):
    doctest_namespace["input"] = input
    doctest_namespace["expected"] = expected
    print(f'doctest_namespace is:{doctest_namespace}')

@pytest.fixture
def user_data():
    return {"id": uuid.uuid4(), "name": "test_user"}

@pytest.fixture
def json_write(doctest_namespace,request):
    temp_file = open("D:\pythonProject\pytestProject\data\data.json", "w", encoding='utf-8')
    doctest_namespace["test_temp_file"] = temp_file
    print(f'doctest_namespace is:{doctest_namespace}')
    doctest_namespace["test_temp_file_close"] = request.addfinalizer(lambda: temp_file.close())
    # print(f'{request.addfinalizer(lambda: temp_file.close())}')

@pytest.fixture
def json_file_write(request):
    temp_file = open("D:\pythonProject\pytestProject\data\data.json", "w", encoding='utf-8')
    def cleanup():
        temp_file.close()  # 清理函数
    request.addfinalizer(cleanup)  # 注册清理钩子
    return temp_file



