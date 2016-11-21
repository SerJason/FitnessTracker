print ('Content-Type: text/plain')
print ('')

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
	return name

def saveUserName(userName):
	file = open('userName.txt','w')
	file.write(userName)
	file.close()
	return True

def getUserName():
	file = open('userName.txt','r')
	userName = file.readline()
	return userName

print(isUserNameOkay(""))
print(isUserNameOkay("Larry"))

print(saveName("Jason"))
print(getName())

print(saveUserName("SerJason"))
print(getUserName())