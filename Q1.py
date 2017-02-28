# coding=utf-8


def get_hints(originalhints):
    alphabet = {'a': 'c', 'b': 'd', 'c': 'e', 'd': 'f', 'e': 'g', 'f': 'h', 'g': 'i',
                'h': 'j', 'i': 'k', 'j': 'l', 'k': 'm', 'l': 'n', 'm': 'o', 'n': 'p',
                'o': 'q', 'p': 'r', 'q': 's', 'r': 't', 's': 'u', 't': 'v', 'u': 'w',
                'v': 'x', 'w': 'y', 'x': 'z', 'y': 'a', 'z': 'b', ' ': ' ', '.': '.',
                '(': '(', ')': ')', "'": "'"}
    hints_list = []
    for em in original_hints:
        hints_list.append(alphabet[em])
    #print hints_list
    new_hints = ''.join(hints_list)
    return new_hints


if "__main__" == __name__:
    original_hints = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj. "
    # original_hints = 'map'
    # ans is 'ocr'
    hints = get_hints(original_hints)
    print hints
