# Discord Voicechat Moderator Bot
This is a discord bot made to act as a voice chat moderator by automatically timing out any users who say a banned word or phrase. It uses pycord to get user audio and OpenAI Whisper to provide transcriptions.
# Getting Started
For this project to work, a Discord bot token and OpenAI key is required. Please be aware that **this project requires OpenAI credits.**
### Setting Up The Bot
[Follow this guide](https://discordpy.readthedocs.io/en/stable/discord.html) to setup a Discord bot and generate a bot token, which will be used later.
When adding the bot to a server, ensure it has permissions to **Moderate Members, Send Messages, Use Slash Commands, and Connect.** 
You will need to update the banned_words.txt file and add in any words or phrases that you wish to moderate. Each word or phrase should be on it's own line in the text file.

### Getting Keys
1. [Make an OpenAI developer account](https://platform.openai.com/login) if you have not already done so.
2. [Create an API key](https://platform.openai.com/api-keys) for this project.
3. Edit the .env file and add in the OpenAI key and the bot token aquired during the bot setup.
### Library Installation
For this project to work, the OpenAI and pycord libraries will need to be installed. <br>
<br>
The OpenAI python library can be installed using the following command:
 ```
 pip install openai
```
If you already have the discord library installed you will need to uninstall it first, then install pycord using the following:
 ```
pip uninstall discord.py
pip install "py-cord[voice]"
```
Otherwise, just use this:
 ```
 pip install "py-cord[voice]"
```

# Usage
To start up the bot, simply run the moderator_bot.py file. If it is properly set up and connected to the server, you will see the bot status update from offline to online.

### Commands
Once the bot is active, there are two slash commands that can be used:
<br>
<br>
 ```
/record
```
It is used to connect the bot to a voice channel and start the recording. The user of the command needs to be in a voice channel, which is where the bot will connect.
<br>
<br>
 ```
/stop_recording [stop]
```
Disconnects the bot from the voice channel that it is in. The stop parameter is optional and should not be used for expected functionality.
