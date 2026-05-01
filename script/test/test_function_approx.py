# -*- coding: utf-8 -*-
import pytest
import math
class Test():


    def test_approx(self):
        print(f'approx function study!{0.3 == pytest.approx(0.3)}')
        assert 0.3 == pytest.approx(0.3)
        print(f'rel :{1.001 == pytest.approx(1.0001,rel= 1e-3)}')
        print(f'abs :{1.01 == pytest.approx(1.001,abs= 1e-2)}')
        print(f'nan_ok = False :{math.nan == pytest.approx(math.nan,nan_ok=False)}, nan_ok = True :{math.nan == pytest.approx(math.nan,nan_ok=True)}, math.nan :{math.nan} ')


    def test_login(self):
        username = "admin"
        if username != "admin":
            pytest.fail("用户名错误，必须为admin", pytrace=True)

    # pytest.skip("关键服务未启动，跳过整个模块", allow_module_level=False)
    def test_custom_exception(self):
        class AuthError(Exception):
            def __init__(self, code, message):
                self.code = code
                self.message = message

        with pytest.raises(AuthError) as exc_info:
            raise AuthError(code=403, message="Forbidden")

        # 验证异常属性
        assert exc_info.value.code == 403
        assert "Forbidden" in exc_info.value.message






