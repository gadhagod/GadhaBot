<h1><center>GadhaBot</center></h1>
The source code of GadhaBot, a discord bot with many miscellaneous functions.
<h2>Features</h2>
This list is constantly changing and being added to, because it's still in developement. Here are the features so far:
<ul>
  <li>Automatically send an email to you when someone runs a command with what they did and who did it</li>
  <li>Can tell you how many COVID-19 deaths and cases there are real-time</li>
  <li>Can tell you the population and capital of any country</li>
  <li>Can tell you the headlines from BBC news</li>
  <li>Many more commands
  <li>Super-fast results</li>
</ul>
<h2>Invite</h2>
<p>You can invite this bot to any server. To invite, you can click this bot <a href="https://discord.com/oauth2/authorize?client_id=714911868455747629&permissions=0&scope=bot">here</a> or type !invite in your server. </p>
<h2>Permissions</h2>
<p>This bot doesn't require many permissions. It just need to be able to read messages and send messages. Make sure it has these permissions on whichever channels you wish use this bot with.</p>
<h2>Enviroment</h2>
<p>The only thing you need to change after downloading this file onto your computer is the .env file. Enviroment variables are used for security purposes. You don't want people seeing your email credentials or your bot token. If someone gets your bot token, they have full control over your bot, so change the value of the enviroment variables to your email credentials and your bot token. Make sure there are no spaces between the '=' sign and the other characters next to it.</p>
<h2>Download</h2>
<p><b>Packages</b></p>
Install the following packages: 
<ul>
  <li>flask</li>
  <li>discord</li>
  <li>countryinfo</li>
  <li>bs4</li>
  <li>requests</li>
</ul>
<p>You may already have some packages already installed or some default ones may have beem removed on your system.</p>
</p>To install packages:</p>

    pip install {package name}
<p><b>Run</p></b>
<p>Clone this repo</p>

    git clone https://github.com/gadhagod/GadhaBot
<p>Open the repo on your computer</p>

    cd gadhabot
<p>Edit the .env</p>

    nano .env
<p>Put in your email credentials and bot token.</p>
<p>Exit the editor by pressing "control" and "x" at the same time.</p>
<p>Run main.py</p>

    python3 main.py
