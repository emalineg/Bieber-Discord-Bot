import asyncio
import os
import discord
from dotenv import load_dotenv

# below imports for audio function not yet finished
# import ffmpeg
# import nacl
# from discord import guild, voice_client, FFmpegAudio
# from discord.ext import commands, tasks
# from discord.ext.commands import bot
# from discord import FFmpegAudio, FFmpegPCMAudio, PCMVolumeTransformer
# from discord.types import voice
# from discord import FFmpegPCMAudio
# from discord.utils import get

load_dotenv()

dsecret = os.getenv('DISCORD_SECRET')

# 'message_content' intent
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}


# bot online
@client.event
async def on_ready():
    print('hey its me')


# dictionary with client messages bieberBot will respond to (and what it will say)
@client.event
async def on_message(message):
    cmds = {
        'hello': "hey, it's jb",
        'is justin bieber here?': 'yeah, im here. whats up bbqurl?',
        'jb ily!': 'i have a wife',
        ': (': 'dont b sad',
        "hope your feelings aren't hurt": 'do I LOOK caSe SenSITIVE to U?! buy my album'
    }

    # wont respond to its own messages
    if message.author == client.user:
        return

    # how it'll actually happen
    # lowercases client message, so it doesn't have to be case-sensitive
    # then if it matches item in dictionary ...
    # adds 'is typing'
    # for 3 seconds
    # sends response
    for cmd, resp in cmds.items():
        if message.content.lower().startswith(cmd):
            async with message.channel.typing():
                await asyncio.sleep(3)
                await message.channel.send(resp)


# BELOW DOESN'T WORK YET --
# WON'T THROW ERROR UNLESS IT'S ACTIVE WHILE JOINING A VC CHANNEL

# @client.event
# notices when someone joins vc
# async def on_voice_state_update(member, before, after):
# selects channel someone joined
# if after.channel:
# joins & play song (needs ffmpeg)
# await member.voice.channel.connect().create_ffmpeg_player('loveme.mp3', after=lambda: print('done'))
# waits 3 seconds
# leaves
# some sort of assurance this has to be completed before it will respond
# to another call


client.run(dsecret)
