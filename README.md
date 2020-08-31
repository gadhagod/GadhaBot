<h1 align="center">GadhaBot</h1>
<hr>
<h2>Features</h2>
This list is constantly changing and being added to, because it's still in developement. Here are the features so far:
<ul>
  <li>Can tell you how many COVID-19 deaths and cases there are real-time</li>
  <li>Can tell you the population and capital of any country</li>
  <li>Can tell you the headlines from BBC news</li>
  <li>Automatically sends you an email when someone runs a command</li>
  <li>Many more commands
  <li>Super-fast results</li>
</ul>

<h2>Invite</h2>
<p>You can invite this bot to any server. To invite, you click <a href="https://discord.com/oauth2/authorize?client_id=714911868455747629&permissions=0&scope=bot">here</a> or type !invite in a server that it is already in. </p>

<h2>Environment</h2>
<p>The only thing you need to change after downloading this file onto your computer is the .env file. Environment variables are used for security purposes. You don't want people seeing your email credentials or your bot token. If someone gets your bot token, they have full control over your bot, so change the value of the environment variables to your email credentials and your bot token. Make sure there are no spaces between the '=' sign and the other characters next to it.</p>

<h2>Emails</h2>
<p>Everytime someone runs a command, an email will be sent to you containing what command was run and who ran it. If you don't want to enable emails, don't worry about this section. To enable emails, go to this <a href="https://myaccount.google.com/u/5/lesssecureapps?gar=1">link</a> and enable less secure app access.</p>
<div align="center">
<img src="README images/LessSecureAppAcess.png" style="vertical-align:middle"/>
</div>

<h2>Download & Run</h2>
<p><h4>Packages</h4></p>
<details>
  <summary>Necessary packages</summary>
  <ul>
    <li>flask</li>
    <li>discord</li>
    <li>countryinfo</li>
    <li>bs4</li>
    <li>requests</li>
  </ul>
</details>

<p>You may already have some packages already installed or some default ones may have beem removed on your system.</p>
</p>To install packages:</p>

    pip install {package name}
<p><b>Run</p></b>
<p>Clone this repo</p>

    git clone https://github.com/gadhagod/GadhaBot
<p>Open the repo on your computer</p>

    cd GadhaBot
<p>Edit the .
  file</p>

    nano .env
<p>Put in your email credentials and bot token.</p>
<p>Exit the editor by pressing <kbd>^</kbd> and <kbd>x</kbd> at the same time.</p>
<p>Run main.py</p>

    python3 main.py
