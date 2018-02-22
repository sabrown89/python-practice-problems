from example import example_pytest
def test_add():
    ad = example_pytest.Addition()
    assert ad.add(1, 2) == 3

