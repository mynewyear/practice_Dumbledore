import string

def encrypting(text):
    words = []
    alphabet = '{}a'.format(string.ascii_lowercase)
    next_el = 0
    for el in text:
        if el.isalpha() and el.islower():
            next_el = alphabet.index(el) + 1
            words.append(alphabet[next_el].capitalize())
        elif el.isalpha() and el.isupper():
            next_el = alphabet.index(el.lower()) + 1
            words.append(alphabet[next_el].lower())
        else:
            words.append(el)
    return ''.join(words)


def dencrypting(text):
    words = []
    alphabet = '{}a'.format(string.ascii_lowercase)
    previous_el = 0

    for el in text:
        if el.isalpha() and el.islower():
            previous_el = alphabet.index(el) - 1
            words.append(alphabet[previous_el].capitalize())
        elif el.isalpha() and el.isupper():
            previous_el = alphabet.index(el.lower()) - 1
            words.append(alphabet[previous_el].lower())
        else:
            words.append(el)
    return ''.join(words)


print(encrypting(
    "You don't need to hardcode the letters and their positions in the alphabet - you can use the string.ascii_lowercase."))

print(dencrypting(
    "zPV EPO'U OFFE UP IBSEDPEF UIF MFUUFST BOE UIFJS QPTJUJPOT JO UIF BMQIBCFU - ZPV DBO VTF UIF TUSJOH.BTDJJ_MPXFSDBTF."))
