def mid(string):
    length=len(string)
    if length%2==0:
        return ''
    else:
        return string[int(length/2)]
