# -*- coding: utf-8 -*-
import pytest
import os

# # 在 conftest.py 中检查关键环境变量
# def test_configure():
#     if not os.environ.get("API_KEY"):
#         pytest.exit("API_KEY 未设置，终止测试", returncode=1)
#
# # 测试前检查配置文件是否存在
# def test_requires_config():
#     if not os.path.exists("config.yaml"):
#         pytest.exit("缺少配置文件 config.yaml", returncode=2)
#     # ...后续测试代码...
# def critical_service():
#     pass
# def test_critical_system():
#     try:
#         critical_service.connect()
#     except Exception as e:
#         pytest.exit(f"{e}关键服务不可用，终止所有测试", returncode=3)

