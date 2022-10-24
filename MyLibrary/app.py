from flask import Flask, request, jsonify
 
app = Flask(__name__)
 
@app.route('/data/2.5/weather', methods = ['GET'])
def hello_world():
    if(request.method == 'GET'):
        city = request.args.get('q')
        appid = request.args.get('appid')
        data = {
            "City" : city,
            "appid" : appid,
            "response" : "Works Good"
        }
        return jsonify(data)

if __name__ == '__main__':
    app.run()