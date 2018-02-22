def ransom_note(magazine, ransom):
    mag = {m: magazine.count(m) for m in magazine}
    ran = {r: ransom.count(r) for r in ransom}
    value = False
    for word, count in ran.items():
        try:
            if mag[word] == count:
                value = True
            else:
                value = False
                break
        except KeyError:
            value = False
            break
    return value

m, n = map(int, input().strip().split(' '))
magazine = input().strip().split(' ')
ransom = input().strip().split(' ')
answer = ransom_note(magazine, ransom)
if(answer):
    print("Yes")
else:
    print("No")
