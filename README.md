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

<h2>Cloning</h2>
<p>Clone this repo and cd to it</p>

    git clone https://github.com/gadhagod/GadhaBot
    cd GadhaBot

<h2>APIs & Tokens</h2>
To create a discord bot and find your bot token, click <a href="DiscordBotCreate.md">here</a>.<br> To create a GitHub API token, click <a href="GitHubAPI.md">here</a>.<br>To get a, OpenWeather token, click <a href="OpenWeatherAPI.md">here</a>.</p>

<h2>Environment Variables</h2>
<p>Environment variables are used for security purposes. You don't want people seeing your email credentials or API tokens. </p><br>
<p><b>Windows</b>
Change the values of the environment variables in file .env to your email credentials and tokens. Make sure there are no spaces between <kbd>=</kbd> and the other characters next to it. 
  
    nano .env
 <br>
 
    DISCORD_BOT_SECRET={bot token}
    WEATHER_SECRET={openweathermap token}
    GITHUB_SECRET={github token}
    EMAIL={your email}
    PASSWORD={your email's password}
    RECIEVER={your email}

<p><b>Mac/Linux</b></p>
<p>For mac or linux, you have to use the <code>export</code> command. To make environment variables permanent, create/edit file .bashrc.</p>

    nano ~/.bashrc
<p>Export your credentials and tokens.</p>

    export DISCORD_BOT_SECRET={bot token}
    export WEATHER_SECRET={openweathermap token}
    export GITHUB_SECRET={github token}
    export EMAIL={your email}
    export RECIEVER={your email's password}
    export PASSWORD={your email}
<p>When you want to run code, make sure you are in the bash shell. To enter the bash shell, run <code>bash</code> in your terminal.</p>

<h2>Emails</h2>
<p>Everytime someone runs a command, an email will be sent to you containing what command was run and who ran it. If you don't want to enable emails, don't worry about this section. To enable emails, go to this <a href="https://myaccount.google.com/u/5/lesssecureapps?gar=1">link</a> and enable less secure app access.</p>
<div align="center">
<img src="README images/LessSecureAppAcess.png" style="vertical-align:middle"/>
</div>

<h2>Website</h2>
<p>On GadhaBot's website, you can view features, versions, and more.<br>
<a href="https://gadhabot.gadhagod.repl.co/">GadhaBot's website</a><br>
<a href="https://github.com/gadhagod/GadhaBot/tree/master/WebsiteSubPages">GadhaBot's website source code</a>

<h2>Run the Bot</h2>
<p><h4>Packages</h4></p>
<details>
  <summary>Necessary packages</summary>
  <ul>
    <li>discord</li>
    <li>countryinfo</li>
    <li>beautifulsoup4</li>
    <li>feedparser</li>
    <li>requests</li>
    <li>google</li>
    <li>pygithub</li>
  </ul>
</details>

<p>You may already have some packages already installed or some default ones may have beem removed on your system.</p>
</p>To install packages:</p>

    pip install {package name}
<p>or</p>

    pip3 install {package name}

<h4>AWS</h4>
If your run discordmain.py normally, your bot will go offline when you close the terminal or your computer goes to sleep. To solve this, we use an AWS machine.<br> Create an AWS account. We will only use the free tier on AWS, so you won't be charged for anything. This <a href="https://docs.aws.amazon.com/efs/latest/ug/gs-step-one-create-ec2-resources.html">tutorial</a> tells you how to launch an E2C instance on AWS. Select an Ubuntu machine. <br>
<div align="center">
<img src="README images/UbuntuAWS.png" style="vertical-align:middle"/>
</div>
<br>After launching, ssh to your new machine using the .pem file you downloaded

    ssh -i "something.pem" ubuntu@ipaddress
<h4>Run</h4>
Run this command to run your ssh terminal.

    nohup python3 discordmain.py &
Now you can close your terminal and the bot will remain running. If you want to stop running, run these commands:

    ps -ef | grep discordmain.py
This should return something similar to this (maybe along with other processes):

    ubuntu   25678 25026  3 19:23 pts/1    00:00:00 python3 discordmain.py
The second column's value is the process id. To kill the process, run <code>kill {process id}</code>. Now the bot is offline. You can do this if you need to make changes to the bot.
<br><p align="center">
  <a href="http://gadhagod.repl.co/"><img src="Logos/logo.png" legnth=40% width=40%></a>
</p>
