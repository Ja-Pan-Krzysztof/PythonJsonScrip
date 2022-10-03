import re
import pytest


@pytest.fixture
def args_ip():
    list_args = ['main.py', '123.123.123.133', 'missclick']

    return list_args


def test_get_ip(args_ip):

    test_args_list = []

    for i in args_ip:
        test_args_list.append(i)

        args = []

        for arg in test_args_list:
            args.append(arg)

        if len(args) == 1:
            assert args[0] == 'main.py'

        elif len(args) == 2:
            assert re.match(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', args[1])

        elif len(args) >= 3:
            assert True
