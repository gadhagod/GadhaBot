<h1>Rockset</h1>
<a href="rockset.com">Rockset</a> is a database that we will use to store user's and server's info. In the database, we store contents for user's experinces to be personalized.<br>
Start by creating an account at <a href="rockset.com">Rockset</a> on the free tier and head to your <a href="http://console.rockset.com/">Rockset console</a>. Create a new collection.
<img src="images/CreateCollection.png">
Under "Custom Integration", choose "Write API".
<img src="images/WriteAPI.png">
Name the collection "GadhaBotUsers".<br>
Create the following field mapping.
<img src="images/FieldMapping.png">
Hit <kbd>Create</kbd>.<br>
Create another collection called "GadhaBotServers" with the same field mapping.
We have to create an API key to access our database. Click <kbd><a href="https://console.rockset.com/apikeys">API Keys</a> on the left sidebar.</kbd>
<img src="images/RocksetAPIKeys.png">
After creating your API key, copy it. You will need it later.
