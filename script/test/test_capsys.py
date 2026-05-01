# -*- coding: utf-8 -*-
def test_output(capsys):
    print("hello")
    captured = capsys.readouterr()
    print(f'captured is:{captured}')
    assert captured.out == "hello\n"

def test_print_output(capsys):
    print("Hello, pytest!")       # 触发标准输出
    captured = capsys.readouterr()
    assert captured.out == "Hello, pytest!\n"  # 断言输出内容

def test_error_logging(capsys):
    import sys
    sys.stderr.write("Error occurred\n")  # 触发标准错误流
    captured = capsys.readouterr()
    print(f'captured is:{captured},type is:{type(captured)}')
    assert captured.err == "Error occurred\n"  # 断言错误流内容

def test_disable_capture(capsys):
    with capsys.disabled():  # 禁用捕获
        print("实时查看此输出")  # 输出直接显示在控制台


def test_output_binary(capsysbinary):
    print("hello")
    captured = capsysbinary.readouterr()
    print(f'captured binary is:{captured}')
    assert captured.out == b"hello\n"

def test_system_echo(capfd):
    import os
    os.system('echo "hello"')
    captured = capfd.readouterr()
    assert captured.out == '"hello"\r\n'
