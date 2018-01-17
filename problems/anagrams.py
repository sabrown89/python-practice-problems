def number_of_swaps(a, b):
    dict_a = {letter: a.count(letter) for letter in a}
    dict_b = {letter: b.count(letter) for letter in b}
    result = []
    for k,v in dict_a.items():
        try:
            if dict_b[k] == v:
                pass
            else:
                diff = dict_b[k] - v
                result.append(abs(diff))
        except KeyError:
            result.append(v)
    for k,v in dict_b.items():
        try:
            if dict_a[k] == v:
                pass
        except KeyError:
            result.append(v)
    return sum(result)
