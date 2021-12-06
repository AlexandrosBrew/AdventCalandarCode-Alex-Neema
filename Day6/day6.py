def day6():
	lanternlife = [3,4,3,1,2]

	for x in range(80):
		for l in range(len(lanternlife)):
			x = lanternlife[l]
			if x == 0:
				lanternlife.pop(l)
				lanternlife.insert(l, 6)
				lanternlife.append(8)
			else:
				lanternlife.pop(l)
				lanternlife.insert(l, x-1)

	return len(lanternlife)

print(day6())