class DegreeOfArray():
    def __init__(self, array):
        self.array = array

    def find_smallest_substring_of_degree(self):
        substrings = [self.find_substrings_for(sub) for sub in self.find_ints_with_degree()]
        return min(len(l) for l in substrings)

    def dict_count_of_list_items(self):
        return dict((k,self.array.count(k)) for k in set(self.array))

    def find_degree(self):
        return max(self.dict_count_of_list_items().values())

    def find_ints_with_degree(self):
        return [k for k,v in self.dict_count_of_list_items().items() if v == self.find_degree()]

    def find_substrings_for(self, item):
        min_index = self.array.index(item)
        max_index = max([i for i, v in enumerate(self.array) if v == item]) + 1
        return self.array[min_index:max_index]
