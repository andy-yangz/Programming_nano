# 1. At first get all the list
# 2. Then pass all the list to identify which one is triple
# 3. Because there is one, so if we find we can break

def num_list():
	num_list = [];
	#Cause a + b + c = 1000, and a<b<c
	# then at list a < 1000/3 ~ 333
	for a in range(1,333):
		for b in range(a,int((1000-a)/2)):
			num_list.append([a,b,1000-a-b])
	return num_list

def is_triple(num_list):
	for i in num_list:
		if i[0]**2 + i[1]**2 == i[2]**2:
			return i

num_list = num_list()
triple = is_triple(num_list)

print triple
