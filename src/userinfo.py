import os
from rockset import Client, Q, F

collectionName = 'GadhaBotUsers'
rs = Client(api_key = os.environ.get('ROCKSET_SECRET'), api_server="api.rs2.usw2.rockset.com")
collection = rs.Collection.retrieve(collectionName)

def store(username, userid):
	docs = {
		'id': userid,
		'username': username
	}
	collection.add_docs([docs])
