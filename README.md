# Discord Voicechat Moderator Bot
This is a discord bot made to act as a voice chat moderator by automatically timing out any users who say a banned word or phrase. It uses pycord to get user audio and OpenAI Whisper to provide transcriptions.
# Getting Started
For this project to work, a Discord bot token and OpenAI key is required. Additionally, the python libraries for pycord and openai must be installed. Please be aware that **this project requires OpenAI credits.**
### Setting Up The Bot
[Follow this guide](https://discordpy.readthedocs.io/en/stable/discord.html) to setup a Discord bot and generate a bot token, which will be used later.
When adding the bot to a server, ensure it has permissions to **Moderate Members, Use Slash Commands, and Connect.**

### Getting Keys
1. [Make an OpenAI developer account](https://platform.openai.com/login) if you have not already done so.
2. [Create an API key](https://platform.openai.com/api-keys) for this project.
3. Edit the .env file and add in the OpenAI key and the bot token aquired during the bot setup.
### Library Installation
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
