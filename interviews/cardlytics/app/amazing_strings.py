class AmazingStrings():
    def __init__(self, unamazing_list):
        self.unamazing_list = unamazing_list

    def amazing_string_count(self):
        replacement_list = []
        for string in self.unamazing_list:
            replacement_list.append(self.count_replacements_needed(string))
        return replacement_list

    def count_replacements_needed(self, string):
        result = []
        if len(self.count_of_repeating_letters(string)) == 0:
            result.append(0)
        else:
            for count in self.count_of_repeating_letters(string):
                if count == 1:
                    result.append(1)
                elif count % 2 == 0:
                   result.append(count / 2)
                else:
                   result.append(round(count / 2))
        return sum(result)

    def count_of_repeating_letters(self, string):
        length = len(string) - 1
        count = 0
        repeating_list = []
        for num in range(0,length):
            if num + 1 == length and string[num] == string[num + 1]:
                count += 1
                repeating_list.append(count)
            elif string[num] == string[num + 1]:
                count += 1
            else:
                if count > 0:
                    repeating_list.append(count)
                count = 0
        return repeating_list
