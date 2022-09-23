import pytest
from main import put_folder, del_folder

# В переменную fixture вместо "TOKEN" нужно подставить валидный токен яндекс диска

fixture = [
    ('Test_folder', "TOKEN", 201)
    ]

# Тестирование классов
@pytest.mark.parametrize('folder_name, token, result', fixture)
def test_put_folder(folder_name, token, result):
    calc_result = put_folder(folder_name, token)
    assert calc_result == result
    delete = del_folder(folder_name, token) # удаляем созданную папку при выполнении теста
    etalon = 204
    assert delete == etalon # проверяем код ответа сервера при удалении ранее созданной папки