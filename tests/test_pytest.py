import pytest
from main import YandexDisk

# fixture = [
#             (1, 2, 2),
#             (-1, -1, 1),
#             (5, 5, 25)
#         ]
#
# class TestFunktion:
#     def setup(self):
#         print('setup ==>')
#
#     def teardown(self):
#         print('teardown ==>')
#
#     @pytest.mark.parametrize('a, b, result', fixture)
#     def test_multiplication_int(self, a, b, result):
#         # etalon = 4
#         calc_result = multiplication_int(a, b)
#         # result = result
#         assert calc_result == result
#         # assert isinstance(calc_result, int)


# @pytest.mark.parametrize('a, b, result', fixture)
# def test_multiplication_int(a, b, result):
#     # etalon = 4
#     calc_result = multiplication_int(a, b)
#     # result = result
#     assert calc_result == result
#     # assert isinstance(calc_result, int)

# fixture = 201

# Тестирование классов
# @pytest.mark.parametrize('folder_name, result', fixture)
def test_put_folder(folder_name):
    # folder_name = '15'
    etalon = 201
    inst = YandexDisk()
    # self_token = inst.get_headers
    calc_result = inst.put_folder(folder_name)

    # result = result
    assert calc_result == etalon
    # assert calc_result == result
    # assert isinstance(calc_result, int)