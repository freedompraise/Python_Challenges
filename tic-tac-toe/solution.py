def get_row_col(input):
    r,c=list(input)
    c=int(c)
    c=3-c
    if r=="A":
        r=2
    if r=='B':
        r=1
    if r=='C':
        r=0

    return r,c
