<h1 align="center">GadhaBot</h1>
<p align="center">
  <b><a href="https://discord.com/oauth2/authorize?client_id=714911868455747629&permissions=0&scope=bot">Invite</a> | 
    <a href="https://github.com/gadhagod/GadhaBot/blob/master/commands.txt">Commands</a> |
    <a href="https://github.com/gadhagod/GadhaBot">Code</a>
  </b>
</p>

<hr>
<h2>Features</h2>
This list is constantly changing and being added to, because it's still in developement. Here are the features so far:
<ul>
  <li>Can tell you how many COVID-19 deaths and cases there are real-time</li>
  <li>Can tell you the population and capital of any country</li>
  <li>Can tell you the headlines from BBC news</li>
  <li>Can give you google search results</li>
  <li>Automatically sends you an email when someone runs a command</li>
  <li>Many more commands
  <li>Super-fast results</li>
</ul>

<h2>Creating the Bot</h2>
<p>First, you have to create your bot. To do this, go to the <a href="https://discord.com/developers/applications">Discord Developer Portal</a> and click <kbd>New Application</kbd> on the top right of the page. Now name your application and hit <kbd>Create</kbd>.</p>
<div align="center">
<img src="README images/CreateApplication.png" style="vertical-align:middle"/>
</div> <p> Go to the <kbd>bot</kbd> tab and click <kbd>Add Bot</kbd>.</p>
<div align="center"><img src="README images/AddBot.png" style="vertical-align:middle"/></div>
<p>Name your bot and chose an icon. To copy your bot token, click <kbd>copy</kbd>. You will need your bot token to control your bot from python.</p>
<div align="center">
<img src="README images/BotToken.png" style="vertical-align:middle"/>
</div>

<h2>Cloning</h2>
<p>Clone this repo</p>

    git clone https://github.com/gadhagod/GadhaBot

<h2>Emails</h2>
<p>Everytime someone runs a command, an email will be sent to you containing what command was run and who ran it. If you don't want to enable emails, don't worry about this section. To enable emails, go to this <a href="https://myaccount.google.com/u/5/lesssecureapps?gar=1">link</a> and enable less secure app access.</p>
<div align="center">
<img src="README images/LessSecureAppAcess.png" style="vertical-align:middle"/>
</div>

<h2>Environment Variables</h2>
<p>Environment variables are used for security purposes. You don't want people seeing your email credentials or your bot token. If someone gets your bot token, they have full control over your bot.</p>
  <p><b>Windows</b><br>
Change the value of the environment variables to your email credentials and your bot token. Make sure there are no spaces between <kbd>=</kbd> and the other characters next to it. </p>

```
DISCORD_BOT_SECRET={bot token}
EMAIL={your email}
PASSWORD={your email's password}
RECIEVER={your email}
```
<p><b>Mac</b></p>
<p>For mac, you have to use the <code>export</code> command. To make environment variables permanent, make .bashrc.</p>

    nano ~/.bashrc
<p>Put in your credentials and bot token.</p>

    export DISCORD_BOT_SECRET={bot token}
    export EMAIL={your email}
    export RECIEVER={your email's password}
    export PASSWORD={your email}
<p>When you want to run main.py, make sure you are in the bash shell. To enter the bash shell, run <code>bash</code> in your terminal.</p>

<h2>Download & Run</h2>
<p><h4>Packages</h4></p>
<details>
  <summary>Necessary packages</summary>
  <ul>
    <li>flask</li>
    <li>discord</li>
    <li>countryinfo</li>
    <li>beautifulsoup4</li>
    <li>feedparser</li>
    <li>requests</li>
    <li>google</li>
  </ul>
</details>

<p>You may already have some packages already installed or some default ones may have beem removed on your system.</p>
</p>To install packages:</p>

    pip install {package name}
<p>or</p>

    pip3 install {package name}
<p><b>Run</p></b>
<p>Open the repo on your computer.</p>

    cd GadhaBot
<p>If you are on mac, ignore the rest of these steps. </p>
<p>Edit the .env file</p>

    nano .env
<p>Put in your email credentials and bot token.<br>
Exit the editor by pressing <kbd>^</kbd> and <kbd>x</kbd> at the same time.<br>
Run main.py</p>

    python3 main.py
