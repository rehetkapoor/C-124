from flask import Flask, jsonify, request

app=Flask(__name__)

tasks=[
{
    'id': 1,
    'title': u"Buy groceries",
    'description':u'Milk, Cheese, Pizza, Fruit, Tylenol',
    'done':False
},

{
    'id': 2,
    'title': u"Learn Python",
    'description':u'Need to find a good tutorial',
    'done':False
},
  
]


@app.route("/")
def hello_world():
    return "Hello World"

@app.route("/add-data",methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"Please provide the data!"
        },400)
    
    task={
        'id': task[-1]['id']+1,
        'title':request.json['title'] ,
        'description':request.json.get['description',""],
        'done':False

    }

    tasks.appened(task)
    return jsonify(
        {
            "status": "success",
            "message": "Task completed successfully"
        }
    )

@app.route("/get-data")   
def get_task():
    return jsonify({
        "data":tasks
    })





if(__name__=='__main__'):
    app.run(debug=True)