class BubbleSort():
    def __init__(self, unsorted_list):
        self.unsorted_list = unsorted_list

    def sort_list(self):
        sorted_yet = False
        list_size = len(self.unsorted_list)
        list_size = list_size - 1
        while not sorted_yet:
            sorted_yet = True
            for element in range(0, list_size):
                if self.unsorted_list[element] > self.unsorted_list[element + 1]:
                    sorted_yet = False
                    higher_value = self.unsorted_list[element]
                    self.unsorted_list[element] = self.unsorted_list[element + 1]
                    self.unsorted_list[element + 1] = higher_value
