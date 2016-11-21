import cgi

form = cgi.FieldStorage()

name = form['name']
userName = form['userName']

isError = False

if isNameOkay(name) == False:
    isError = True

if isUserNameOkay(userName) == False:
    isError = True

print ('Content-Type: text/plain')
print ('')

print(isUserNameOkay(""))
print(isUserNameOkay("Larry"))

print(saveName("Jason"))
print(getName())

print(saveUserName("SerJason"))
print(getUserName())
