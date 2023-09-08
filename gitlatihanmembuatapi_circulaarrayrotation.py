from flask import Flask, request, jsonify
from gitcircular_array_rotation import circularArrayRotation
import base64

app= Flask(__name__)

@app.route('/circular-array-rotation', methods=['GET','POST'])
def searchCircularArrayRotation():
    username = 'pengabdisetan'
    password = 'pengabdisetan666'
    strauth = f'{username}:{password}'
    encryption = strauth.encode('ascii')
    base64_auth_str = f'Basic {str(base64.b64encode(encryption))[2:-1]}'
    header = request.headers.get('Authorization')
    if header!= base64_auth_str :
       return 'ERROR', 401


    data = request.json
    a=data['a'] #[1,2,3]
    k=data['k'] #2
    queries = data['queries'] #[0,1,2]

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
    