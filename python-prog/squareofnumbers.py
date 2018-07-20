
def main():
	nums = [10,20,[4,5],{6,7},3]
	newnums = [square(n) for n in nums]
	
	print(nums)
	print(newnums)


def square(n):
	if type(n) in (int,float): return n*n
	if type(n) == list: return [square(x) for x in n]
	if type(n) == set: return {square(x) for x in n}
	if type(n) == tuple: return tuple([square(x) for x in n])
	return None


if __name__ == '__main__':
	main()



