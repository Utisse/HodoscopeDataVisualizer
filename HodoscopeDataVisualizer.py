loc = input("Enter file path or press enter to use the file provided with the code\n\nExample file path: D:\\Folder\\filename.csv\n\n")
if loc == "":
	loc = "Example.csv"
file = open(loc,"r", encoding='utf-8-sig')
RowArray = []
col = 0
counter = 1
for i in file:
	row = 0
	list = i.split(",")
	final = ""
	for word in list:
		add = "null"
		if(word == ""):
			add = "0"
		if(word == "1"):
			add = "█"
		if(add != "null"):
			final += add +" "
			row += 1
		if(row == 15):
			RowArray.append(final)
			row = 0
			final = ""
			col += 1
	if(col == 10):
		print(counter)
		counter +=1
		for k in RowArray:
			print(k)
		RowArray = ["\n"]
		col = 0
		input()