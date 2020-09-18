<h1>Rockset</h1>
<a href="rockset.com">Rockset</a> is a database that we will use to store user's info. In the database, we store contents for user's experinces to be personalized. One of the things we store is user's cites, so they can run !weather without typing their city. (More personaliztion features are in development).<br>
Start by creating an account at <a href="rockset.com">Rockset</a> on the free tier and head to your <a href="http://console.rockset.com/">Rockset console</a>. Create a new collection.
<img src="README images/CreateCollection.png">
Under "Custom Integration", choose "Write API".
<img src="README images/WriteAPI.png">
Name the collection "GadhaBotUsers".<br>
Create the following field mapping.
<img src="README images/FieldMapping.png">
Hit <kbd>Create</kbd>. Now our database is setup and ready for use.
