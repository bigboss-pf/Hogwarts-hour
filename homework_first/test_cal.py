"""
~~~~~~~~~~~~~~~~~~~~~~~
author:hour
time:2020/12/11
E-mail:58166728@qq.com
~~~~~~~~~~~~~~~~~~~~~~~
"""
import pytest
from homework_first.cal import Calculator

class TestCal():
    def setup_class(self):
        self.cal=Calculator()
        print("start testing")
    def teardown_class(self):
        print("testing done")
    #加法测试用例
    @pytest.mark.parametrize("a",[1,2])
    @pytest.mark.parametrize("b", [3,4])
    def test_add(self,a,b):
        assert self.cal.add(a,b) == a+b

    #减法测试用例
    @pytest.mark.parametrize("a", [1, 2])
    @pytest.mark.parametrize("b", [3, 4])
    def test_sub(self,a,b):
        assert self.cal.sub(a,b) == a-b

    # 乘法测试用例
    @pytest.mark.parametrize("a", [1, 2])
    @pytest.mark.parametrize("b", [3, 4])
    def test_mul(self,a,b):
        assert self.cal.mul(a,b) == a * b

    # 除法测试用例
    @pytest.mark.parametrize("a", [1, 2])
    @pytest.mark.parametrize("b", [3, 4])
    def test_div(self,a,b):
        assert self.cal.div(a,b) == a / b

