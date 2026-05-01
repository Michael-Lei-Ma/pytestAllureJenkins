# -*- coding: utf-8 -*-
import json
import pytest
def test_params(doctest_namespace,params):
    print(f'{params}')
    print(f'doctest_namespace is:{doctest_namespace},type is :{type(doctest_namespace)}')
    sum = doctest_namespace['utils']['sum'](1,2)

    print(f'sum is:{sum}')


def test_json_translation(doctest_namespace,json_write):
    data = {
        "path": "C:/中文目录/文件.txt",
        "symbols": "><&",
        "country": "China(中国)123-456-789"
    }

    # 禁用 Unicode 转义，禁用斜杠转义（默认会转义为 \/）
    json_str = json.dumps(data, ensure_ascii=False, indent=4, separators=(',',':'))
    print(f'json_str is :{json_str}')
    json_str_new = json_str.replace('\\/', '/')  # 手动替换转义后的斜杠
    print(f'json_str_new is :{json_str_new}')
    print(f'doctest_namespace is:{doctest_namespace}')
    js_file_wr = doctest_namespace["test_temp_file"]
    js_file_wr.write(json_str)
    print(f'js_file_wr status is:{js_file_wr.closed}')
    doctest_namespace["test_temp_file"].close()
    print(f'js_file_wr status new is:{js_file_wr.closed}')
    # doctest_namespace.addfinalizer(lambda: temp_file.close())
    # with open("data.json", "w", encoding="utf-8
    # ") as f:
    #     f.write(json_str)
    # f.close()



def test_json_operations(doctest_namespace, json_file_write):
    doctest_namespace["js_wr"] = json_file_write  # 注入已注册清理的对象
    print(f'doctest_namespace is:{doctest_namespace}')
    print(f'js_file_wr status is:{doctest_namespace["js_wr"].closed}')
    doctest_namespace["js_wr"].close()
    print(f'js_file_wr status new is:{doctest_namespace["js_wr"].closed}')




