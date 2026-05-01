# -*- coding: utf-8 -*-
import pytest
from pathlib import Path
import ast
import time


def test_create_dir(cache):
    # pytest.skip("不执行test_create_dir函数")  #用pytest.skip()内置函数，执行函数跳过
    dir_path = cache.makedir("config_cache01")  # 创建名为 test_data 的目录
    print(dir_path)  # 输出类似 /path/to/.pytest_cache/v/test_data
    cache.set("config_cache01_dir_path",str(dir_path))
    time.sleep(1)

def test_set_data_in_dir(cache):
    dir_path_str = cache.get("config_cache01_dir_path", default="")
    if dir_path_str:
        dir_path =Path(dir_path_str)
        print(f'dir_path is:{dir_path}')
        data_file = dir_path.joinpath("token")
        print(f'data_file is:{data_file}')
        with open(data_file,'a+') as file:
            file.write('{"key": "value"}')
        cache.set("config_cache01_file_path", str(data_file))
        time.sleep(1)

def test_get_data_from_dir(cache):
    dir_path_str = cache.get("config_cache01_dir_path", default="")
    data_file_path = cache.get("config_cache01_file_path", default="")
    if dir_path_str and data_file_path:
        data_file = Path(data_file_path)
        with open(data_file,'r') as file:
            content = file.read()
            print(f'content type is:{type(content)},content is:{content}')
        # assert eval(content)["key"] == "value"
        assert ast.literal_eval(content)["key"] == "value"
    time.sleep(1)





# @pytest.mark.skip(reason = "cache set function 不用了！")#用pytest装饰器执行函数跳过
def test_set_cache(cache):
    cache.set("test_config_cache01/token", "abc123")  # 存储 token 到缓存
    cache.set("test_config_cache01/user_info", {"name": "Alice", "id": [1,23,345]})  # 存储字典


# @pytest.mark.skip(reason = "cache get function 不用了！")
# @pytest.mark.skipif('test_config_cache01/token' or 'test_config_cache01/user_info' is None,reason="token、user_info 不存在！")
def test_get_cache(cache):
    token = cache.get("test_config_cache01/token", default=None)  # 读取 token
    user_info = cache.get("test_config_cache01/user_info", default={})  # 读取字典
    print(f'set_cache/token is:{token},set_cache/user_info is: {user_info}')
    assert token == "abc123"



