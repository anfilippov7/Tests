import unittest
from parametrized import parametrized
from nose_parameterized import parameterized
from main import name_people, name_shelf, name_list, name_add, name_delete, name_movie, name_add_self
# from main import multiplication_int

# Задание №1

class TestFunktion(unittest.TestCase):
#     @parametrized(
#         [
#             (1,  2, 2),
#             (2, 2, 4),
#             (3, 3, 9)
#         ]
#     )
#     def test_multiplication_int(self, a, b, result):
#         # etalon = 4
#         # result = multiplication_int(1, 4)
#         # self.assertEqual(result, etalon)
#         calc_result = multiplication_int(a, b)
#         self.assertEqual(calc_result, result)
#         # self.assertIsInstance(result, str)

    def test_name_people(self):
        etalon = 'Имя человека, которому принадлежит документ 11-2: Геннадий Покемонов'
        result = name_people('11-2')
        self.assertEqual(result, etalon)
        # calc_result = name_people(people)
        # self.assertEqual(calc_result, result)
        self.assertIsInstance(result, str)

    @parametrized.expand(
        [
            ('10006',  'Имя человека, которому принадлежит документ 10006: Аристарх Павлов'),
            ("2207 876234", 'Имя человека, которому принадлежит документ 2207 876234: Василий Гупкин'),
            ("11-2", 'Имя человека, которому принадлежит документ 11-2: Геннадий Покемонов')
        ]
    )
    def test_name_people(self, people, results):
        # etalon = 'Имя человека, которому принадлежит документ 11-2: Геннадий Покемонов'
        # result = name_people('11-2')
        # self.assertEqual(result, etalon)
        calc_result = name_people(people)
        self.assertEqual(calc_result, results)
        self.assertIsInstance(calc_result, str)

    @parametrized.expand(
        [
            ('2207 876234',  'Номер полки, на которой находится документ 2207 876234: 1'),
            ("11-2", 'Номер полки, на которой находится документ 11-2: 1'),
            ("5455 028765", 'Номер полки, на которой находится документ 5455 028765: 1'),
            ("10006", 'Номер полки, на которой находится документ 10006: 2'),
            ("", 'В базе данных нет такого документа'),
            (" ", 'В базе данных нет такого документа')
        ]
    )
    def test_name_shelf(self, shelf, results):
        calc_result = name_shelf(shelf)
        self.assertEqual(calc_result, results)
        self.assertIsInstance(calc_result, str)

    @parametrized.expand(
        [
            ([
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}],  'Данные сотрудника № 1: [passport, 2207 876234, Василий Гупкин]\n'
                                                                           'Данные сотрудника № 2: [invoice, 11-2, Геннадий Покемонов]\n'
                                                                           'Данные сотрудника № 3: [insurance, 10006, Аристарх Павлов]')
        ]
    )
    def test_name_list(self, documents, results):
        calc_result = name_list(documents)
        self.assertEqual(calc_result, results)
        self.assertIsInstance(calc_result, str)


    @parametrized.expand(
        [
            (11-2, "passport", 'Геннадий Покемонов', 1,  'directories = {1: [2207 876234, 11-2, 5455 028765, 11-2], 2: [10006], 3: []}\n'
                                                         'documents = [{type: passport, number: 2207 876234, name: Василий Гупкин}, '
                                                         '{type: invoice, number: 11-2, name: Геннадий Покемонов}, '
                                                         '{type: insurance, number: 10006, name: Аристарх Павлов}, '
                                                         '{type: Геннадий Покемонов, number: 11-2, name: Геннадий Покемонов}]'),
            (11-2, "passport", 'Геннадий Покемонов', 4, "Нет такой полки!")
        ]
    )
    def test_name_add(self, number, type, name, num_directories, results):
        calc_result = name_add(number, type, name, num_directories)
        self.assertEqual(calc_result, results)
        self.assertIsInstance(calc_result, str)


    @parametrized.expand(
        [
            ("2207 876234",  'directories = {1: [11-2, 5455 028765], 2: [10006], 3: []}\n'
                                                         'documents = [{}, '
                                                         '{type: invoice, number: 11-2, name: Геннадий Покемонов}, '
                                                         '{type: insurance, number: 10006, name: Аристарх Павлов}]'),
            ('11-2', 'directories = {1: [2207 876234, 5455 028765], 2: [10006], 3: []}\n'
                                                         'documents = [{type: passport, number: 2207 876234, name: Василий Гупкин}, '
                                                         '{},'
                                                         '{type: insurance, number: 10006, name: Аристарх Павлов}]'),
            ('10006', 'directories = {1: [2207 876234, 11-2, 5455 028765], 2: [], 3: []}\n'
                                                         'documents = [{type: passport, number: 2207 876234, name: Василий Гупкин}, '
                                                         '{type: invoice, number: 11-2, name: Геннадий Покемонов},'
                                                         '{}]'),
            ('11-6', "Вы вводите несуществующий документ!")
        ]
    )
    def test_name_delete(self, number_del, results):
        calc_result = name_delete(number_del)
        self.assertEqual(calc_result, results)
        self.assertIsInstance(calc_result, str)


    @parametrized.expand(
        [
            ("11-2", '3',  'directories = {1: [2207 876234, 5455 028765], 2: [10006], 3: [11-2]}'),
            ('2207 876234', '3', 'directories = {1: [11-2, 5455 028765], 2: [10006], 3: [2207 876234]}'),
            ('10006', '3', 'directories = {1: [2207 876234, 11-2, 5455 028765], 2: [], 3: [10006]}'),
            ("11-2", '2', 'directories = {1: [2207 876234, 5455 028765], 2: [10006, 11-2], 3: []}'),
            ('11-2', '4', "Нет такой полки!"),
            ('11-6', None, "Нет такого документа!")
        ]
    )
    def test_name_movie(self, number_movie, number_rack, results):
        calc_result = name_movie(number_movie, number_rack)
        self.assertEqual(calc_result, results)
        self.assertIsInstance(calc_result, str)

    @parametrized.expand(
        [
            ('4',  'directories = {1: [2207 876234, 11-2, 5455 028765], 2: [10006], 3: [], 4: []}'),
            ('5',  'directories = {1: [2207 876234, 11-2, 5455 028765], 2: [10006], 3: [], 5: []}'),
            ('3', "Данная полка уже существует!")

        ]
    )
    def test_name_add_self(self, number_add_self, results):
        calc_result = name_add_self(number_add_self)
        self.assertEqual(calc_result, results)
        self.assertIsInstance(calc_result, str)

    # @parametrized.expand(
    #     [
    #         (1,  2, 2),
    #         (2, 2, 4),
    #         (3, 3, 9)
    #     ]
    # )
    # def test_multiplication_int(self, a, b, results):
    #     # etalon = 'Имя человека, которому принадлежит документ 11-2: Геннадий Покемонов'
    #     # result = name_people('11-2')
    #     # self.assertEqual(result, etalon)
    #     calc_result = multiplication_int(a, b)
    #     self.assertEqual(calc_result, results)
    #     # self.assertIsInstance(result, str)
    #
    # def test_multiplication_int(self):
    #     etalon = 4
    #     result = multiplication_int(1, 4)
    #     self.assertEqual(result, etalon)
    #     # calc_result = multiplication_int(a, b)
    #     # self.assertEqual(calc_result, results)
    #     # self.assertIsInstance(result, str)

