from flask import Flask, jsonify
from flask_cors import CORS
import pymongo


connection_url = 'mongodb+srv://sailakshmi:ALifFxlhlVU7GbID@cluster0.651b1ys.mongodb.net/?retryWrites=true&w=majority'

app = Flask(__name__)
client = pymongo.MongoClient(connection_url)


Database = client.get_database('test')

SampleTable = Database.todos



@app.route('/insert-one/<name>/<id>/', methods=['PUT'])
def insertOne(name, id):
    queryObject = {
        'Name': name,
        'ID': id
    }
    query = SampleTable.insert_one(queryObject)
    return "Query inserted...!!!"


@app.route('/find-one/<argument>/<value>/', methods=['GET'])
def findOne(argument, value):
    queryObject = {argument: value}
    query = SampleTable.find_one(queryObject)
    query.pop('_id', None)
    return jsonify(query)




@app.route('/delete-one/<argument>/<value>', methods=['DELETE'])
def deleteOne(argument, value):
    queryObject = {argument: value}
    query = SampleTable.delete_one(queryObject)
    output = "Sucessfully Deleted"
    return output

@app.route('/find/', methods=['GET'])
def findAll():
    query = SampleTable.find()
    output = {}
    i = 0
    for x in query:
        output[i] = x
        output[i].pop('_id')
        i += 1
    return jsonify(output)



@app.route('/update/<key>/<value>/<element>/<updateValue>/', methods=['POST'])
def update(key, value, element, updateValue):
    queryObject = {key: value}
    updateObject = {element: updateValue}
    query = SampleTable.update_one(queryObject, {'$set': updateObject})
    if query.acknowledged:
        return "Update Successful"
    else:
        return "Update Unsuccessful"



if __name__ == '__main__':
    app.run(debug=True)