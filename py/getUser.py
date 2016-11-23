# import cgi
import json
import user

# form = cgi.FieldStorage()
# TODO: get anything needed like: info = form.getvalue('info')

name = user.getName()
username = user.getUsername()
data = {'name': name, 'username': username}

print('Content-Type: text/json')
print('')
print(json.dumps(data))
