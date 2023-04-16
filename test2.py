from flask import Flask,request,jsonify

app = Flask(__name__)
task = [
    {
    "id":1,
    "title":'shopping list',
    "description":['cheese','milk','apple','grape'],
    "done":False

    },
    {
    "id":2,
    "title":'luxuary car brands',
    "description":['lambo','ferrari','bugati'],
    "done":False
    }
]
@app.route("/get-data")
def gettask():
    return jsonify({
        "data":task
    }) 

if (__name__ =="__main__"):
    app.run(debug=True)
