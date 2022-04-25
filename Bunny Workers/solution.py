def check(n):
    return True if n%3==0 else False

def solution(L):
    L.sort(reverse=True)
    number=''
    for i in L:
        number+=str(i)
    number=int(number)
    if check(number)==True:
        return number
    while number>0:
        number-=1
        if check(number)==True:
            break
    return number

print(solution([3,1,4,1]))
