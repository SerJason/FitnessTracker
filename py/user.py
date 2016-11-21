def isNameOkay(name):
	if (len(name) == 0):
		isNameOkayName = False
	else:
		isNameOkayName = True
	return isNameOkayName

def isUserNameOkay(userName):
	if (len(userName) == 0):
		isUserNameOkayUserName = False
	else:
		isUserNameOkayUserName = True
	return isUserNameOkayUserName

def saveName(name):
	file = open('name.txt','w')
	file.write(name)
	file.close()
	return True

def getName():
	file = open('name.txt','r')
	name = file.readline()
	file.close()
	return name

def saveUserName(userName):
	file = open('userName.txt','w')
	file.write(userName)
	file.close()
	return True

def getUserName():
	file = open('userName.txt','r')
	userName = file.readline()
	file.close()
	return userName
