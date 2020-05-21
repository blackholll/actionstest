from tests.base import ActionTest


class TestAccountView(ActionTest):
    def test_sum_func(self):
        """
        加法运算
        :return:
        """

        self.assertEqual(0-1, -1)

    def test_division_func(self):
        """
        除法运算
        :return:
        """

        self.assertEqual(2/1, 2.0)


