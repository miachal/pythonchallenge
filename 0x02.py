txt = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj. "


def rot(string):
    before = "abcdefghijklmnopqrstuvwxyz"
    after = before[2:] + before[:2]
    diff = {x: y for x, y in zip(before, after)}

    return ''.join(map(lambda x: diff.get(x, x), string))


print(rot(txt))

print('http://pythonchallenge.com/pc/def/{}.html'.format(rot('map')))
