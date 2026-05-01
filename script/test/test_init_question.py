# -*- coding: utf-8 -*-

import pytest


@pytest.fixture
def x_fixture():
    x = 10
    return x


class TestClass:
    def setup_method(self, x):
        self.x = x

    def test_add(self, x_fixture):
        self.x += 5
        assert self.x == 15




