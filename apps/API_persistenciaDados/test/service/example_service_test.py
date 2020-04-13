'''
Date: 20190506
User: Semantix
Project: Template for Unit test
'''

import pytest

from src.business.example_business import Simple


class TestService:

    def test_answer(self):
        assert Simple().code_sample(3) == 5


if __name__ == '__main__':
    TestService().test_answer()

