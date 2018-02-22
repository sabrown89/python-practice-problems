class CavityMap():
    def __init__(self, list_matrix):
        self.list_matrix = list_matrix

    def cavity_map(self):
        result = []
        for elem in self.non_border_locations():
            if self.is_cavity(elem[0],elem[1]):
                result.append(elem)
        for cavity in result:
            self.list_matrix[cavity[0]][cavity[1]] = 'X'
        return self.list_matrix

    def is_cavity(self, row, col):
        top_middle = self.list_matrix[row - 1][col]
        left = self.list_matrix[row][col - 1]
        right = self.list_matrix[row][col + 1]
        bottom_middle = self.list_matrix[row + 1][col]
        value = self.list_matrix[row][col]
        if value > top_middle\
            and value > left\
            and value > right\
            and value > bottom_middle:
                return True
        else:
             return False

    def non_border_locations(self):
        max_index = len(self.list_matrix) - 1
        non_borders = []
        for row in range(0, len(self.list_matrix)):
                for col in range(0, len(self.list_matrix)):
                    if row == 0 or col == 0 or row == max_index or col == max_index:
                        pass
                    else:
                        non_borders.append([row,col])
        return non_borders
