# -*- coding: utf-8 -*-

#主体例子1：
def test_case():
    print("用例被运行")

#主体例子2：烤鸭1.0
def test_duck():
    print("-----烤鸭店利润计算器开始⼯作------")
    price1 = int(input("请输⼊烤鸭的进货价：")) # input传递来的值，都是str
    price2 = int(input("请输⼊烤鸭的售卖价："))
    num = int(input("请输⼊今天卖出的烤鸭数量："))
    result = (price2 - price1) * num
    print("今天的烤鸭利润是{}元".format(result))















