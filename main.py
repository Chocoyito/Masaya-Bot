import discord
from dotenv import load_dotenv
import os
import requests
import json
from discord.ext import commands
import asyncio
load_dotenv()
import tracemalloc
import youtube_dl
import pafy

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="$",intents=intents)
tracemalloc.start()

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)


    
@bot.command(
	help="Es para ver si el bot recibe ordenes",
	brief="El bot devuelve Pong! si todo funciona bien."
)
async def ping(ctx):
  await ctx.channel.send('Pong!')

@bot.command(
	# ADDS THIS VALUE TO THE $HELP PRINT MESSAGE.
	help="$say (argumento)",
	# ADDS THIS VALUE TO THE $HELP MESSAGE.
	brief="Repite lo que escribiste"
)
async def say(ctx, *args):
	response = ""

	# Itera el ciclo
	for arg in args:
		response = response + " " + arg

	# manda un mensaje al canal usando el contexto de objeto
	await ctx.channel.send(response)
  
@bot.command(
	help="Documentacion de C modo grafico",
	brief="Lanza documentacion de C grafico"
)
async def docgrafico(ctx):
  await ctx.channel.send('Documentancion de C grafico')
  await ctx.channel.send(file=discord.File('Documentacion/Doc.pdf'))
  await ctx.channel.send(file=discord.File('Documentacion/EJEM1.c'))

youtube_dl.utils.bug_reports_message = lambda: ""


ytdl_format_options = {
    "format": "bestaudio/best",
    "outtmpl": "%(extractor)s-%(id)s-%(title)s.%(ext)s",
    "restrictfilenames": True,
    "noplaylist": True,
    "nocheckcertificate": True,
    "ignoreerrors": False,
    "logtostderr": False,
    "quiet": True,
    "no_warnings": True,
    "default_search": "auto",
    "source_address": "0.0.0.0",  # bind to ipv4 since ipv6 addresses cause issues sometimes
}

ffmpeg_options = {"options": "-vn"}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)


class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)

        self.data = data

        self.title = data.get("title")
        self.url = data.get("url")

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(
            None, lambda: ytdl.extract_info(url, download=not stream)
        )

        if "entries" in data:
            # take first item from a playlist
            data = data["entries"][0]

        filename = data["url"] if stream else ytdl.prepare_filename(data)
        return cls(discord.FFmpegPCMAudio(filename, **ffmpeg_options), data=data)


class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def join(self, ctx, *, channel: discord.VoiceChannel):
        """Joins a voice channel"""

        if ctx.voice_client is not None:
            return await ctx.voice_client.move_to(channel)

        await channel.connect()

    @commands.command()
    async def play(self, ctx, *, query):
        """Plays a file from the local filesystem"""

        source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(query))
        ctx.voice_client.play(
            source, after=lambda e: print(f"Player error: {e}") if e else None
        )

        await ctx.send(f"Now playing: {query}")

    @commands.command()
    async def yt(self, ctx, *, url):
        """Plays from a url (almost anything youtube_dl supports)"""

        async with ctx.typing():
            player = await YTDLSource.from_url(url, loop=self.bot.loop)
            ctx.voice_client.play(
                player, after=lambda e: print(f"Player error: {e}") if e else None
            )

        await ctx.send(f"Now playing: {player.title}")

    @commands.command()
    async def stream(self, ctx, *, url):
        """Streams from a url (same as yt, but doesn't predownload)"""

        async with ctx.typing():
            player = await YTDLSource.from_url(url, loop=self.bot.loop, stream=True)
            ctx.voice_client.play(
                player, after=lambda e: print(f"Player error: {e}") if e else None
            )

        await ctx.send(f"Now playing: {player.title}")

    @commands.command()
    async def volume(self, ctx, volume: int):
        """Changes the player's volume"""

        if ctx.voice_client is None:
            return await ctx.send("Not connected to a voice channel.")

        ctx.voice_client.source.volume = volume / 100
        await ctx.send(f"Changed volume to {volume}%")

    @commands.command()
    async def stop(self, ctx):
        """Stops and disconnects the bot from voice"""

        await ctx.voice_client.disconnect()

    @play.before_invoke
    @yt.before_invoke
    @stream.before_invoke
    async def ensure_voice(self, ctx):
        if ctx.voice_client is None:
            if ctx.author.voice:
                await ctx.author.voice.channel.connect()
            else:
                await ctx.send("You are not connected to a voice channel.")
                raise commands.CommandError("Author not connected to a voice channel.")
        elif ctx.voice_client.is_playing():
            ctx.voice_client.stop()


bot = commands.Bot(
    command_prefix=commands.when_mentioned_or("$"),
    description="Relatively simple music bot example",
)

@bot.event
async def on_ready():
  print('We have logged in as {0.user}'
  .format(bot))
  bot.loop.create_task(status_task()) # Create loop/task

@bot.event
async def on_message(message):
   
  if message.author == bot.user:
    return

  if message.content.lower()=="frase":
    quote=get_quote() 
    await message.channel.send(quote)

  if message.content.lower()=="yon":
    await message.channel.send('Mi hombre')
    await message.channel.send(file=discord.File('resources/YON.jpg'))

  if message.content.lower()=="sexo":
    await message.channel.send('Lo unico que no vas a heredar de tus padres.')

  if message.content.lower()=="leonel":
    await message.channel.send(file=discord.File('resources/esposa.jpg'))

  if message.content.lower() == "te quiero mucho":
    await message.channel.send(file=discord.File('resources/mp4.gif'))

  if message.content.lower() == "passchipeada":
    await message.channel.send(file=discord.File('resources/leonel.c'))

  if message.content.lower()=="infravalorada" :
    await message.channel.send(file=discord.File('resources/yichu.jpg'))

  if message.content.lower()=="¿quien soy?":
      await message.channel.send('Vos sos @{}'.format(message.author.name))

  if message.content.lower()=="elpepe":
    await message.channel.send(file=discord.File('resources/elpepe.mp4'))

  if message.content.lower()=="crudninja":
    await message.channel.send(file=discord.File('TAREAS/pipe.c'))
    await message.channel.send(file=discord.File('TAREAS/tupapa.h'))
    await message.channel.send(file=discord.File('TAREAS/CRUD.rar'))

  if message.content.lower()=="grevinpaja":
    await message.channel.send(file=discord.File('TAREAS/Munecos.C'))
    await message.channel.send(file=discord.File('TAREAS/tupapa.h'))
    await message.channel.send(file=discord.File('TAREAS/MARIOBROS.h'))

  if message.content.lower()=="lovo":
    await message.channel.send(file=discord.File('resources/lovo.mp4'))

  if message.content.lower()=="*dormir*":
    await message.channel.send('¿Vamos a dormir U//U?')
    await message.channel.send(file=discord.File('waifu/dormir.png'))
  
  if message.content.lower()=="*me siento triste*":
    await message.channel.send('¿Que tenés bb? contame u.u')
    await message.channel.send(file=discord.File('waifu/triste.gif'))

  if message.content.lower()=="*te cuento*":
    await message.channel.send('contame')
    await message.channel.send(file=discord.File('waifu/contame.gif'))

  if message.content.lower().startswith("lo que pasa es que"):
    await message.channel.send('¿Y como te hace sentir eso?')
    await message.channel.send(file=discord.File('waifu/feeling.gif'))

  if message.content.lower()=="logouni3d":
    await message.channel.send(file=discord.File('resources/cuento.c'))

  await bot.process_commands(message)

@bot.event
async def status_task():
    while True:
        await bot.change_presence(activity=discord.Game("Lovo lindo"), status=discord.Status.idle)
        await asyncio.sleep(3) # cambia luego de x segundos
        await bot.change_presence(activity=discord.Game("Paja"), status=discord.Status.idle)
        await asyncio.sleep(3)
        await bot.change_presence(activity=discord.Game("Pornhub"), status=discord.Status.idle)
        await asyncio.sleep(3)
        await bot.change_presence(activity=discord.Streaming(name='TurboC es completamente basura', url='https://www.twitch.tv/tugfammg'))
        await asyncio.sleep(15)
        await bot.change_presence(activity=discord.Streaming (name='Roberto lindo', url='https://www.twitch.tv/tugfammg'))
    await bot.process_commands(status_task)







bot.add_cog(Music(bot))
bot.loop.create_task(status_task())


bot.run(os.getenv('TOKEN'))