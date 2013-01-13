import time

def readHits(fileName):
	with open(fileName) as inFile:
		hitsList = map(lambda x:x.replace('\n',''), inFile.readlines())
	return hitsList

def updateHits(fileName):
	
	hitsList = readHits(fileName)
	date = time.strftime("%d,%m,%Y")

	if hitsList == []:
		hitsList.append(date+":1")
	elif date == hitsList[-1].split(":")[0]:
		hitsList[-1] = date + ":" + str(int(hitsList[-1].split(":")[1])+1)
	else:
		hitsList.append(date+":1")
	
	with open(fileName, 'w') as outFile:
		for hit in hitsList:
			outFile.write(hit+"\n")
