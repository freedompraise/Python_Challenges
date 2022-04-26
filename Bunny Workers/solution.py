
from itertools import combinations
def solution(l):
	l.sort(reverse = True)
	for i in reversed(range(1, len(l) + 1)):
		for value in combinations(l, i):
			if sum(value) % 3 == 0: return int(''.join(map(str, value)))
	return 0 

print(solution([3,1,4,1]))
