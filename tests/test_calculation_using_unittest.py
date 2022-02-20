from unittest import TestCase, mock
from src.calculation import add_two_numbers, add_two_numbers_by_operation


class Calculation(TestCase):

    def setUp(self):
        '''
            This method gets called at the start of every individual test.
        '''
        print('in setup')

    def tearDown(self):
        '''
        This method gets called at the end of every individual test
        '''
        print('in tearDown')

    def test_given_two_numbers_should_return_sum(self):
        sum = add_two_numbers(10, 20)
        print(f'sum of two numbers  {sum}')
        self.assertEqual(sum, 30)

    def test_given_two_numbers_failed_case(self):
        sum = add_two_numbers(1,3)
        print(f'sum failed case  {sum}')
        self.assertNotEqual(sum,19)

    def test_given_two_empty_numbers_raises_value_error(self):
        with self.assertRaises(ValueError) as e:
            add_two_numbers(None,None)
        print(e)
        self.assertEqual(1, e.exception.args.__len__())

    @mock.patch("src.calculation.get_operation")
    def test_two_numbers_by_operation_mock_patch(self, mock_get_operation):
        mock_get_operation.return_value = 'op_add'
        expected_outcome = add_two_numbers_by_operation()
        print('expected_results  - ', expected_outcome)
        self.assertIn('op_add', expected_outcome)

    def test_two_numbers_by_operation_without_mock_patch(self):
        expected_outcome = add_two_numbers_by_operation()
        print('expected_results  - ', expected_outcome)
        self.assertIn('add', expected_outcome)