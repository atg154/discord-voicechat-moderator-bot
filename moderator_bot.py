import asyncio
import datetime
import dotenv
import discord
from discord.ext import commands
import os
from openai import OpenAI

dotenv.load_dotenv()
client = OpenAI()
TOKEN = os.getenv('BOT_TOKEN')
TIMEOUT_DURATION = 5 # Timeout duration in seconds
BANNED_WORDS = ['example','test'] # Put any banned words here
connections = {}
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.command()
async def record(ctx):
    """Bot command to connect to begin recording."""
    voice = ctx.author.voice

    if not voice:
        await ctx.send("You aren't in a voice channel!")
    else:
        # Connect to the voice channel the author is in
        if len(bot.voice_clients) == 0: 
            vc = await voice.channel.connect()
        else:
            vc = bot.voice_clients[0]
        
        #Starts the recording
        vc.start_recording(
            discord.sinks.WaveSink(),
            once_done,
            ctx.channel,
            ctx.channel.guild,
            ctx
        )

        # Stops the recording 5 seconds later to process the audio.
        await asyncio.sleep(5)
        asyncio.create_task(stop_recording(ctx, stop=False))

async def once_done(sink: discord.sinks, channel: discord.TextChannel, guild, ctx, *args):  # Automatically passed by voice client
    """Times out any user who says a banned word."""
    # Checks if bot has disconnected before continuing.
    if guild.voice_client in bot.voice_clients:
        # The audio is saved as a file first to simplify the transcription process.
        for user_id, audio in sink.audio_data.items():
            audio_io = audio.file.read()
            with open(f'{user_id}.wav', "wb") as f:
                f.write(audio_io)
                
            with open(f'{user_id}.wav', "rb") as f:
                transcript = client.audio.transcriptions.create(model="whisper-1", file=f, response_format="text")
                print(transcript)
            text = transcript.lower()

            if any(word in text for word in BANNED_WORDS):
                user = await guild.fetch_member(user_id)
                try:
                    # Timeout takes a utc datetime, so we just create an offset using a timedelta.
                    timeout = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(seconds=TIMEOUT_DURATION)
                    await user.timeout(timeout)
                    await channel.send(f'Riposte detected: Timing out user {user.display_name} for {TIMEOUT_DURATION} seconds.', tts=True)
                except discord.Forbidden:
                    await channel.send(f'Error: User {user.display_name} has higher permissions than bot.', tts=True)
        
        asyncio.create_task(record(ctx))
    else:
        await ctx.send("bot disconnected!")


@bot.command()
async def stop_recording(ctx, stop=True):
    """Stops the recording process.

    If this is called by a user, it will disconnect and stop. 
    Otherwise it will simply stop the recording, which gets restarted after the once_done.
    """
    # Since the bot can't be connected to multiple voice chats at once, there will only ever be 0 or 1 connections.
    if len(bot.voice_clients) != 0:
        vc = bot.voice_clients[0]
        if stop:
            await vc.disconnect()
        else:
            vc.stop_recording() # Stops recording, and call the callback (once_done).

bot.run(TOKEN)