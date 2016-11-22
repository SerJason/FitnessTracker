import cgi
import user

form = cgi.FieldStorage()

name = form.getvalue('name')
username = form.getvalue('username')

isError = False
if user.isNameOkay(name) == False:
    isError = True
if user.isUsernameOkay(username) == False:
    isError = True

print ('Content-Type: text/html')
if isError == False:
    user.saveName(name)
    user.saveUsername(username)
    print("Location: ../html/usersaved.html")
    print ('')
else:# isError == True:
    print ('')
    print("The name or username is not valid.")
