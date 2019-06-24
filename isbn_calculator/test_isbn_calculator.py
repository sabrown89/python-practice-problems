import hiker

def test_remove_hyphens_and_spaces():
    douglas = hiker.Hiker('978-0-13-  149505- 0')
    assert douglas.isbn == '9780131495050'

def test_isbn_is_thirteen_digits():
    douglas = hiker.Hiker('978-0-13-  149505- 0')
    assert douglas._isbn_is_correct_number_of_digits() is True

def test_isbn_is_correct_number_digits_is_false_if_not_all_digits():
    douglas = hiker.Hiker('978-0-1A-  149505- 0')
    assert douglas._isbn_is_correct_number_of_digits() is False

def test_isbn_is_correct_number_of_digits_is_false_if_not_length_thirteen():
    douglas = hiker.Hiker('97-  149505- 0')
    assert douglas._isbn_is_correct_number_of_digits() is False

def test_is_isbn_thirteen_returns_false():
    douglas = hiker.Hiker('97-  149505- 0')
    assert douglas.is_isbn() is False

def test_calculate_sums():
    douglas = hiker.Hiker('978-0-13-  149505- 4')
    assert douglas._calculate_sums_for_isbn_thirteen() == 100

def test_check_digit():
    douglas = hiker.Hiker('978-0-13-  149505- 4')
    assert douglas._check_digit() == 4

def test_is_isbn_thirteen_true():
    douglas = hiker.Hiker('978-0-13-  149505- 0')
    assert douglas.is_isbn() is True

def test_is_isbn_thirteen_true_another_number():
    douglas = hiker.Hiker('978-0596809485')
    assert douglas.is_isbn() is True

def test_isbn_calculator():
    douglas = hiker.Hiker('978-0596809485')
    assert douglas._isbn_calculator() == 5

def test_isbn_calculator_another():
    douglas = hiker.Hiker('978-0-13-  149505- 0')
    assert douglas._isbn_calculator() == 0

def test_isbn_ten_is_valid():
    douglas = hiker.Hiker('0471958697', 10)
    assert douglas.is_isbn() is True

def test_valid_isbn_standard_invalid():
    douglas = hiker.Hiker('0471958697', 5)
    assert douglas._valid_isbn_standard() is False

def test_valid_isbn_standard_valid_10():
    douglas = hiker.Hiker('047195869')
    assert douglas._valid_isbn_standard() is True

def test_valid_isbn_standard_valid_13():
    douglas = hiker.Hiker('0471958697', 13)
    assert douglas._valid_isbn_standard() is True

