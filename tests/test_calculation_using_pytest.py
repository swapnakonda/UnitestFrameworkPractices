import pytest

from src.calculation import add_two_numbers


@pytest.mark.parametrize('first_number, second_number, result', [(1, 2, 3), (3, 4, 7)])
def test_add_two_numbers_return_result(first_number, second_number, result):
    output = add_two_numbers(first_number, second_number)
    assert result == output


def test_add_two_numbers_return_exception():
    with pytest.raises(ValueError) as ex:
        add_two_numbers(None, None)
    assert str(ex.value) == 'inputs are wrong'




'''
demonstrated pytest fixtures .
 a. pytest fixtures are functions attached to the tests which run before the test function is executed

'''
@pytest.fixture
def fixture_func():
    a= 10
    b = 20
    return a, b


def test_fixture(fixture_func):
    print (f'a value is  {fixture_func[0]}')
    print(f'b value is  {fixture_func[1]}')
    assert fixture_func[0] == 10
    assert fixture_func[1] == 20
