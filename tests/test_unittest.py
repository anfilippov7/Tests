import unittest
from selenium import webdriver
from parameterized import parameterized
from main import check_document_existance, get_doc_owner_name, get_all_doc_owners_names, get_doc_shelf, add_new_doc, \
    delete_doc, add_new_shelf, show_all_docs_info, move_doc_to_shelf
from selenium_for_chrome import page_yandex

documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}

# Задание №1
# Тесты, выполняемые единым потоком:

class TestFunktion(unittest.TestCase):
    @parameterized.expand([
            ('10006', True),
            ('11-2', True),
            ('2207 876234', True),
            ('2207 876235', False),

    ])
    def test_check_document_existance(self, user_doc_number, results):
        calc_result = check_document_existance(user_doc_number)
        self.assertEqual(calc_result, results)
        self.assertIsInstance(calc_result, bool)

    @parameterized.expand([
            (documents, {'Аристарх Павлов', 'Василий Гупкин', 'Геннадий Покемонов'})
    ])
    def test_get_all_doc_owners_names(self, documents, results):
        calc_result = get_all_doc_owners_names(documents)
        self.assertEqual(calc_result, results)
        self.assertIsInstance(calc_result, set)

    @parameterized.expand([
            ('11-5', 'pass', 'Flex', '1', '1')
    ])
    def test_add_new_doc(self, new_doc_number, new_doc_type, new_doc_owner_name, new_doc_shelf_number, results):
        calc_result = add_new_doc(new_doc_number, new_doc_type, new_doc_owner_name, new_doc_shelf_number)
        self.assertEqual(calc_result, results)

    @parameterized.expand([
            ('5', ('5', True)),
            ('6', ('6', True)),
            ('7', ('7', True))

    ])
    def test_add_new_shelf(self, shelf_number, results):
        calc_result = add_new_shelf(shelf_number)
        self.assertEqual(calc_result, results)

    @parameterized.expand([
            (documents, ('passport "2207 876234" "Василий Гупкин"\n' 'invoice "11-2" "Геннадий Покемонов"\n'
                         'insurance "10006" "Аристарх Павлов"\n'))
    ])
    def test_show_all_docs_info(self, documents, results):
        calc_result = show_all_docs_info(documents)
        self.assertEqual(calc_result, results)
        self.assertIsInstance(calc_result, str)

    @parameterized.expand([
            ('10006', "Аристарх Павлов"),
            ('11-2', "Геннадий Покемонов"),
            ('2207 876234', "Василий Гупкин"),
            ('2207 876235', None),

    ])
    def test_get_doc_owner_name(self, user_doc_number, results):
        calc_result = get_doc_owner_name(user_doc_number)
        self.assertEqual(calc_result, results)

    @parameterized.expand([
            ('11-2', '1'),
            ('10006', '2')
    ])
    def test_get_doc_shelf(self, user_doc_number, results):
        calc_result = get_doc_shelf(user_doc_number)
        self.assertEqual(calc_result, results)
        self.assertIsInstance(calc_result, str)


# Выполняются отдельно, т.к. меняют существующий документ

# class TestFunktion(unittest.TestCase):
#     @parameterized.expand([
#             ('11-2', ('11-2', True)),
#             ('2207 876234', ('2207 876234', True)),
#             ('10006', ('10006', True)),
#     ])
#     def test_delete_doc(self, user_doc_number, results):
#         calc_result = delete_doc(user_doc_number)
#         self.assertEqual(calc_result, results)
#
#     @parameterized.expand([
#             ('11-2', '3', ('Документ номер "11-2" был перемещен на полку номер "3"')),
#             ('2207 876234', '3', ('Документ номер "2207 876234" был перемещен на полку номер "3"')),
#             ('10006', '3', ('Документ номер "10006" был перемещен на полку номер "3"')),
#     ])
#     def test_move_doc_to_shelf(self, user_doc_number, user_shelf_number, results):
#         calc_result = move_doc_to_shelf(user_doc_number, user_shelf_number)
#         self.assertEqual(calc_result, results)
#         self.assertIsInstance(calc_result, str)


# Задание №3


class YandexTestCase(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.addCleanup(self.browser.quit)


    def test_page_yandex(self, driver):
        yandex = page_yandex(driver)
        self.browser.get('https://passport.yandex.ru/auth/list')
        self.assertIn(yandex, self.browser.title)

if __name__ == '__main__':
    unittest.main(verbosity=2)