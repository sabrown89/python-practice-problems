from app import cavity_map

list_matrix = [[1,1,1,2],[1,9,1,2],[1,8,9,2],[1,2,3,4]]
cm = cavity_map.CavityMap(list_matrix)

def test_border_elements():
    assert cm.non_border_locations() == [[1,1],[1,2],[2,1],[2,2]]

def test_is_cavity():
    row = 1
    col = 1
    assert cm.is_cavity(row, col) == True
    row = 1
    col = 2
    assert cm.is_cavity(row, col) == False
    row = 2
    col = 2
    assert cm.is_cavity(row, col) == True

def test_cavity_map():
    assert cm.cavity_map() == [[1,1,1,2],[1,'X',1,2],[1,8,'X',2],[1,2,3,4]]
