def isNameOkay(name):
	if ((name == None) or (len(name) == 0)):
		isNameOkayName = False
	else:
		isNameOkayName = True
	return isNameOkayName

def isUsernameOkay(username):
	if ((username == None) or (len(username) == 0)):
		isUsernameOkayUsername = False
	else:
		isUsernameOkayUsername = True
	return isUsernameOkayUsername

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

def saveUsername(username):
	file = open('username.txt','w')
	file.write(username)
	file.close()
	return True

def getUsername():
	file = open('username.txt','r')
	username = file.readline()
	file.close()
	return username
