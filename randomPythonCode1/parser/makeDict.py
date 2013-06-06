def fillDict(j,dictionary):
		dictionary[j] = dictionary[j]+1 if j in dictionary else 1


def makeDict(individualList):
	dictionary={}
	[  fillDict(j.strip(),dictionary) for i in individualList for j in i[2] ]
	return dictionary
