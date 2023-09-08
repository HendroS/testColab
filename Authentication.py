import base64


username = 'guest'
password = 'guest123'
credentials = f'{username}:{password}'.encode('utf-8')
auth_string = str(base64.b64encode(credentials))
auth_key = f'Basic ' + auth_string[2:-1]

# print(auth_string)    
print(auth_key)
    
