# from main import division
# import unittest
#
# class NameTestCase(unittest.TestCase):
#
#    def test_division(self):
#         sum_division = division(4, 2)
#         self.assertEqual(sum_division, 2.0)
#
#
#    def test_first(self):
#        sum_division = division(4, 2, 1)
#        self.assertEqual(division(4, 2, 1))
#
#
# unittest.main()
#
# from main import division
#
# print("Для выхода теста ввидете символ 'P'")
# while True:
#     num1 = (input('\nВведите число: '))
#     if num1 == 'P':
#         break
#     num2 = (input('\nВведите число: '))
#     if num2 == 'P':
#         break
#     sum_division = division(num1, num2)
#     print('\t Деление = ' +  sum_division)

# from main import division
# import unittest
# class DivisionTest(unittest.TestCase):
#   def test_division(self):
#      self.assertEqual(division(4, 2), 2)
#      self.assertEqual(division(6, 2),3)
#      self.assertEqual(division(2, 2), 1)
#      self.assertEqual(division(10, 0),'Division by Zero')
#      self.assertEqual(division(0, 10), 0)
#
#   def division_values(self):
#       self.assertEqual(division('a', 4), 'Type Error')
#       self.assertEqual(division(6, [2]), 'Type Error')
#       self.assertEqual(division(10, '2'), 'Type Error')
#
# if __name__ == '__main__':
#     print('Ok')


# from main import string
# import unittest
# class string1(unittest.TestCase):
#     def test_string(self):
#         test_1 = string('- Did Joffrey agree?\n- He did. He also said "I love using \\n".')
#         self.assertEqual(test_1, ('- Did Joffrey agree?\n- He did. He also said "I love using \\n".'))
#
#
#
# unittest.main()


# from main import s_1
# import unittest
#
# class Test (unittest.TestCase):
#     def test_s_1(self):
#         s_2 = s_1('LOwer')
#         self.assertEqual(s_2, 'lower')
#
#
#
# unittest.main()


# from main import division
# def division_test():
#     assert division(4, 2) == 2
