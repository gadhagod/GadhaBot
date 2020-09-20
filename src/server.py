import os
from rockset import Client, Q, F

collectionName = 'GadhaBotServers'
rs = Client(api_key = os.environ.get('ROCKSET_SECRET'), api_server="api.rs2.usw2.rockset.com")
collection = rs.Collection.retrieve(collectionName)

def store(id, name, region, description, member_count):
	docs = {
		'id': str(id),
		'name': name,
		'region': region,
		'description': description,
		'member count': member_count,
	}
	collection.add_docs([docs])
