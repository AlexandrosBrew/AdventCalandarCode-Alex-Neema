text = open("depth.txt", "r")
depth = text.readlines()
dlist = []
counter = 0
for x in depth:
	dlist.append(int(x))
text.close()

for y in range(len(dlist)):
	try:
		if dlist[y] < dlist[y+1]:
			counter+=1
	except:
		pass

print(counter)
