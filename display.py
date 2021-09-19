def display(a,b):
    unknown_word = "-"*(len(b))
    for i in a:
        position = 0
        for k in b:
            if i == k.lower():
                unknown_word = unknown_word[:position] + k + unknown_word[(position + 1):]
            position += 1
    return unknown_word.upper()
