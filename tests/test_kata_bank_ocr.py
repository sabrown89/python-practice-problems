from practice_problems import kata_bank_ocr

kbo = kata_bank_ocr.KataBankOcr()

def test_find_number():
    f = open('kata_bank_one.txt', 'r')
    assert kbo.find_number(f.read()) == 1
