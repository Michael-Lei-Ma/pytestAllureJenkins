# -*- coding: utf-8 -*-


def setup_function():
    # 模块的前置操作，用例开始执行之前先打印出一句开始的提示语
    print("---烤鸭店系统开始工作---")


def teardown_function():
    # 模块的后置操作，用例执行结束后，打印出一句结束的提示语
    print("---即将退出烤鸭店系统---")


def test_duck_40():
    projects = {}  # 装多个商品
    while True:
        oper_type = input("1 - 录入商品\n2 - 查询商品\n3 - 退出\n请做出你的选择：")
        if oper_type == "1":
            pro_list = []
            # 录入逻辑
            print(">>>准备开始录入商品<<<")
            load_txt = ["请输入商品名:", "请输入商品的成本价：", "请输入商品的产地：", "请输入商品的生产日期："]
            for i in load_txt:
                name1 = input("{}".format(i))
                pro_list.append(name1)
            projects[pro_list[0]] = pro_list

        elif oper_type == "2":
            # 查询逻辑
            print(f'projects is:{projects}')
            po_name = input("请输入要查询的商品名:")
            print("你要查询的商品是：{}".format(projects[po_name]))

            # 烤鸭 -- 直接给我烤鸭信息
        elif oper_type == "3":
            break
        else:
            print("无法别操作，请重新输入")
            continue