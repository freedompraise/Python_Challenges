def format_number(num):
    if len(str(num))<4:
        return num
    else:
        num=str(num)
        num=num[::-1]
        string=''
        other_string=num[0]
        for i in range(len(num)):
            if i%3==0 and i!=0:
                string+=','
            string+=num[i]
    return string[::-1]
