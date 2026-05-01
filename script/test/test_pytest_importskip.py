# -*- coding: utf-8 -*-
import pytest

def test_requires_numpy():
    # 尝试导入 numpy，若失败则跳过测试
    np = pytest.importorskip("numpy")
    result = np.array([1, 2, 3])
    assert len(result) == 3

def test_requires_new_pandas():
    # 要求 pandas>=2.0.0，否则跳过
    pd = pytest.importorskip("pandas", minversion="2.0.0")
    df = pd.DataFrame({"data": [1, 2, 3]})
    assert not df.empty

def test_with_custom_reason():
    # 导入失败时显示自定义提示
    skimage = pytest.importorskip("skimage", reason="scikit-image 未安装，跳过图像处理测试")
    # ...测试代码...

def test_broken_feature():
    pytest.xfail("待修复 Bug #123")
    # ...会失败的测试代码...

def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        pytest.xfail(reason="已知除零错误未处理")  # 标记为 XFAIL
        1 / 0

def some_function():
    return "expected"

@pytest.mark.xfail(strict=True, reason="若通过则说明问题已修复")
def test_fixed_bug():
    result = some_function()
    assert result == "expected"  # 若通过，触发 FAILED（而非 XPASS）
