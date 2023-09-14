from flask import Flask, request, jsonify
from gitcircular_array_rotation import circularArrayRotation
import base64

app= Flask(__name__)

#error handler
@app.errorhandler(400)
def badRequest():
    return {'ERROR 400 - Bad Request' : 'The request was malformed or invalid'},400

@app.errorhandler(401)
def unauthorized():
    return {'ERROR 401 - Unauthorized' : 'You are not authorized to access this resource'},401

@app.route('/circular-array-rotation', methods=['GET','POST'])
def searchCircularArrayRotation():
    #authentification
    username = 'pengabdisetan'
    password = 'pengabdisetan666'
    strauth = f'{username}:{password}'
    encryption = strauth.encode('ascii')
    base64_auth_str = f'Basic {str(base64.b64encode(encryption))[2:-1]}'
    header = request.headers.get('Authorization')
    #data validation error 401
    if header!= base64_auth_str :
       return unauthorized(),401

    #body parameter
    data = request.json
    a=data['a'] #[1,2,3]
    k=data['k'] #2
    queries = data['queries'] #[0,1,2]
    
    #data validation error 404
    if len(a)==0 or k==0 or len(queries)==0:
        return badRequest(),400
    # required_data = ['a', 'k', 'queries']
    # for data_key in required_data :
    #     data_keyfound=False
    #     for key in data.keys() :
    #         if data_key == key:
    #             data_keyfound=True
    #             break
    #         else :
    #             return badRequest(),400

    result = circularArrayRotation(a,k,queries)
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)

# {"a": [1,2,3],
# "k": 2 ,
# "queries": [0,1,2]
# }

#belum bisa jalan kalau pake head parameter, nilainya string ke list blm bs

# @app.route('/circular-array-rotation', methods=['GET','POST'])
# def searchCircularArrayRotation():
#     a1=request.headers.get('Array') #1,2,3
#     a=a1.split(',')
#     for i in a :
#         i=int(i)
#     k=int(request.headers.get('Ktimes'))
#     queries1=request.headers.get('Queries') #0,1,2
#     queries = queries1.split(',')
#     for i in queries:
#         i=int(i)