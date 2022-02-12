import os
import logging
import asyncio

import discord
from discord.ext import commands

# import pafy
# from replit import db
# from youtubesearchpython import VideosSearch
# from pydub import AudioSegment

# import random_song

#from keep_alive import keep_alive

from dotenv import load_dotenv
load_dotenv()

############# RECOMMENDED ##############
logging.basicConfig(level=logging.INFO)
########################################

#YT_API = os.getenv('YT_TOKEN')
TOKEN = os.getenv('TOKEN')

bot = commands.Bot(['m ', 'maria ', 'M ', 'Maria ',
                   '!m ', '!M '], case_insensetive=True)


@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(name="m help"))
    print(f"Logged in as {bot.user}")


@bot.command()
async def ping(ctx):
    msg = discord.Embed(title="Pong :ping_pong:",
                        description=f"{round(bot.latency*1000)} _ms_!", color=0xCB1956)
    await ctx.send(embed=msg)


# @bot.command(name= 'join', aliases= ['connect'])
# async def join(ctx):
#     vc = ctx.author.voice
#     voice = ctx.voice_client
#     if voice:
#         if voice.is_playing():
#             await ctx.send(f"Bot is already connected to {voice.channel.mention} and playing music.")
#         else:
#             await ctx.send(f"Bot is already connected to {voice.channel.mention}")
#     elif not vc:
#         await ctx.send("You aren't connected to any voice channel!")
#     elif vc:
#         await vc.channel.connect()
#         await ctx.send(f"Bot connected to {vc.channel.mention}")
#     else:
#         if voice.channel != vc.channel:
#             await voice.move_to(vc.channel)
#             await ctx.send(f"Bot moved to {vc.channel.mention}")
#         else:
#             await vc.channel.connect()
#             await ctx.send(f"Bot connected to {vc.channel.mention}")

# @bot.command(name='leave', aliases=['disconnect', 'dc'])
# async def leave(ctx):
#     voice = ctx.voice_client
#     if not voice:
#         await ctx.send('Bot isn\'t connected to any voice channel!!')
#     else:
#         await voice.disconnect()
#         await ctx.send(f'Bot disconnected from {voice.channel.mention}!!')


# @bot.command(name= "add")
# async def add(ctx, key, val):
#     db[key] = val
#     await ctx.send("Added")

# @bot.command(name="show")
# async def show(ctx, val):
#     await ctx.send(f"{db[val]}")


# '''
# {
# 1233: {songs: [], no: 2, auto: False, auto_songs: [], auto_no: 0}
# }
# '''
# fast_f = False
# time = 0
# song_loop = "off"
# @bot.command(name='play', aliases=['p'])
# async def play(ctx, *, url=None):

# #    guild = db.get(ctx.guild.id)
# #    if guild:
# #        auto = guild.get("auto")
# #        if auto:
# #            songs =
#     if fast_f:
#         filename = "song2.mp3"
#         source = discord.FFmpegPCMAudio(filename)
#         ctx.voice_client.stop()
#         ctx.voice_client.plsy(source)
#     else:
#         songs = db["songs"]
#         n = int(db["n"])
#         limit = len(songs)

#         if not ctx.voice_client:
#             await ctx.invoke(join)
#         if not url:
#             is_autoplay = True
#             db["auto"] = is_autoplay
#             if n == limit:
#                 songs = []
#                 n = 0
#                 limit = 1
#             if not songs:
#                 songs = random_song.get_song()
#                 db["songs"] = songs
#                 db["limit"] = len(songs)
#             url = songs[n]
#         if not (url.startswith("https://www") or url.startswith("http://")):
#             video_search = VideosSearch(url, limit = 1)
#             url = video_search.result()["result"][0]["id"]


#         video = pafy.new(url)
#         audio = video.audiostreams[0]
#         filename = "song.mp3"
#         if os.path.exists(filename):
#             os.remove(filename)
#         audio.download(filename)
#         #stream_url = audio.url_https
#         source = discord.FFmpegPCMAudio(filename)
#         await ctx.send(f"Now Playing: **{video.title}**")
#         embed = discord.Embed(title = f"{video.title}", description = f"Duration: {video.length}\nPublished At: ", url = f"https://youtu.be/{video.videoid}", color = 0xcb1956)
#         embed.set_thumbnail(url = f"{video.thumb}")
#         embed.set_footer(text = f"\N{eye} {video.viewcount} || \N{Thumbs Up Sign} {video.likes} | \N{Thumbs Down Sign} {video.dislikes}")
#         await ctx.send(embed = embed)
#         ctx.voice_client.play(source)
#         #await ctx.send(data)


# @bot.command(name = "skip", aliases = ["next"])
# async def skip(ctx):
#     ctx.voice_client.stop()
#     db["n"] = int(db["n"])+1

#     await ctx.invoke(play)

# @bot.command(name='pause')
# async def pause(ctx):
#     ctx.voice_client.pause()
#     await ctx.send('Song Paused!!')

# @bot.command(name= "repeat", aliases= ["loop", "l"])
# async def repeat(ctx, loop_of = "single"):
#     pass


# @bot.command(name='stop')
# async def stop(ctx):
#     ctx.voice_client.stop()
#     await ctx.send('Stopped the song!!')


# @bot.command(name='resume')
# async def resume(ctx):
#     ctx.voice_client.resume()
#     await ctx.send('Resuming the song!!')

# #@bot.comman

# @bot.command()
# async def fast(ctx, time):
#     time = time*1000
#     song = AudioSegment.from_file('song.mp3', 'mp3')
#     fast_for = song[:time]
#     fast_for.export("song2.mp3", format="mp3", bitrate="192k")
#     fast_f = True

for files in os.listdir("./cogs"):
    if files.endswith(".py"):
        bot.load_extension(f"cogs.{files[:-3]}")


# keep_alive()
bot.run(TOKEN)
