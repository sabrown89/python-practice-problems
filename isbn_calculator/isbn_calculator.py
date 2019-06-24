class Hiker:

    def __init__(self, isbn, isbn_standard=13):
        self.isbn = self._remove_spaces_and_hyphens(isbn)
        self.isbn_standard = isbn_standard

    def is_isbn(self):
        if not self._valid_isbn_standard():
            return False
        if not self._isbn_is_correct_number_of_digits():
            return False
        isbn_result = self._isbn_calculator()
        if isbn_result == self._check_digit():
            return True
        return False

    def _remove_spaces_and_hyphens(self, isbn):
        isbn = isbn.replace(' ', '').replace('-', '')
        return isbn

    def _valid_isbn_standard(self):
        return self.isbn_standard in [10, 13]

    def _isbn_is_correct_number_of_digits(self):
        return len(self.isbn) == self.isbn_standard and self.isbn.isdigit()

    def _isbn_calculator(self):
        if self.isbn_standard == 13:
            sums = self._calculate_sums_for_isbn_thirteen()
            remainder_of_ten = sums % 10
            subtract_ten_from_sums = sums - 10
            final_remainder_of_ten = subtract_ten_from_sums % 10
            return final_remainder_of_ten
        else:
            sums = self._calculate_sums_for_isbn_ten()
            remainder_of_11 = sums % 11
            if remainder_of_11 == 10:
                return 'X'
            return remainder_of_11

    def _calculate_sums_for_isbn_ten(self):
        result = []
        for i in range(9):
            position = i + 1
            sum_of_digits = position * int(self.isbn[i])
            print(sum_of_digits)
            result.append(sum_of_digits)
        return sum(result)

    def _calculate_sums_for_isbn_thirteen(self):
        result = []
        for i in range(12):
            if i % 2 == 0:
                result.append(int(self.isbn[i]))
            else:
                multiplied_by_three = 3 * int(self.isbn[i])
                result.append(multiplied_by_three)
        return sum(result)

    def _check_digit(self):
        check_digit_index = self.isbn_standard - 1
        return int(self.isbn[check_digit_index])
