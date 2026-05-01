# -*- coding: utf-8 -*-
import pytest
def test_add(a=1,b=2,c=3):
     d = a+b+c
     assert d >10
pytest.register_assert_rewrite("test_register_assert_rewrite.test_add")