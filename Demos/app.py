from flask import Flask
from flask_pymongo import PyMongo
from bson.json_util import dumps
from bson.objectid import ObjectId
from flask import jsonify,request


app=Flask(__name__)
app.secret_key="secretkey"
app.config['MONGO_URI'] = "mongodb://localhost:27017/Users"
mongo = PyMongo(app)



@app.route('/addItems',methods=['POST'])
def add_Items():
	_json=request.json
	_itemName=_json['name']
	_itemQuantity=_json['quantity']
	_price=_json['price']


	if _itemName and _itemQuantity and _price and request.method == 'POST' :
		
		id = mongo.db.cartItems.insert({'name':'_itemName','quantity':'_itemQuantity','price':'_price'})
		resp = jsonify("Item added successfully")
		resp.status_code=200
		return resp
	else:
		return not_found()


@app.route('/getItems')
def getItems():
	allitems=mongo.db.cartItems.find()
	resp=dumps(allitems)
	return resp


@app.route('/removeItems/<id>', methods=['DELETE'])
def remove_item(id):
	mongo.db.cartItems.delete_one({'id': ObjectId(id)})
	resp=jsonify("Items Removed successfully")
	resp.status_code=200
	return resp

@app.route('/updateItem<'id'>', methods=['PUT'])
def update_Item(id):
	_id=id
	_json=request.json
	_itemName=_json['name']
	_itemQuantity=_json['quantity']
	_price=_json['price']


	if _itemName and _itemQuantity and _price and request.method == 'POST' :
		mongo.db.cartItems.update_one({'_id':ObjectId(_id['oid']) if '$oid' in _id in _id else ObjectId(_id)}, {'$set':{'({'name':'_itemName','quantity':'_itemQuantity','price':'_price'}})
		resp=jsonify("Item Updated successfully")
		resp.status_code=200
		return resp
	else:
		return not_found()


@app.errorhandler(404)
def not_found(error=None):
	message ={
	'status': 404,
	'message':'Not Found' +request.url
	}
	resp=jsonify(message)
	resp.status_code=404
	return resp




if __name__=="__main__":
	app.run(debug=True)



