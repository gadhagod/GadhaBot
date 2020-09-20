import os
from rockset import Client, Q, F

collectionName = 'GadhaBotUsers'
rs = Client(api_key = os.environ.get('ROCKSET_SECRET'), api_server="api.rs2.usw2.rockset.com")
collection = rs.Collection.retrieve(collectionName)
                        
def store(userid, city):
	print('City store query')	
	docs = {
		'id': userid, 
		'city': city
	}
	collection.add_docs([docs])
	return('City stored. Type !weather to see weather in your city.')
	
def get(userid):
	struserid = str(userid)
	res = rs.sql(Q(collectionName).where(F['_id'] == struserid).select(F['city']))
	cityobj = res[0]
	city = cityobj['city']
	return city
