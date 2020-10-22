

def words_separator(words) -> list:
    separated = []
    for el in words:
        separated_els = el.split()
        separated += separated_els
    return separated

print(words_separator(["apple banana", "orange", "banana", "kiwi strawberry blueberry"]))

