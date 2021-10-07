
import discord
from dotenv import load_dotenv
import os
import requests
import json
from discord.ext import commands
import asyncio
#:p
load_dotenv()
import tracemalloc
import youtube_dl

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="$", intents=intents)
tracemalloc.start()


def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return (quote)

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
    "source_address":
    "0.0.0.0", 
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
            None, lambda: ytdl.extract_info(url, download=not stream))

        if "entries" in data:
            # take first item from a playlist
            data = data["entries"][0]

        filename = data["url"] if stream else ytdl.prepare_filename(data)
        return cls(discord.FFmpegPCMAudio(filename, **ffmpeg_options),
                   data=data)


class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def join(self, ctx, *, channel: discord.VoiceChannel):
        """Entra a un canal de voz"""

        if ctx.voice_client is not None:
            return await ctx.voice_client.move_to(channel)

        await channel.connect()

    @commands.command()
    async def play(self, ctx, *, query):
        """Reproduce una cancion almacenada en el bot"""
        
        source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(query))
        ctx.voice_client.play(source,
                              after=lambda e: print(f"Player error: {e}")
                              if e else None)

        await ctx.send(f"Reproduciendo: {query}")

    @commands.command()
    async def yt(self, ctx, *, url):
        """Reproduce desde un url (todo lo que pueda soportar youtube_dl)"""

        async with ctx.typing():
            player = await YTDLSource.from_url(url, loop=self.bot.loop)
            ctx.voice_client.play(player,
                                  after=lambda e: print(f"Player error: {e}")
                                  if e else None)

        await ctx.send(f"Reproduciendo: {player.title}")

    @commands.command()
    async def stream(self, ctx, *, url):
        """Streamea desde un url (lo mismo que yt, pero no lo descarga)"""

        async with ctx.typing():
            player = await YTDLSource.from_url(url,
                                               loop=self.bot.loop,
                                               stream=True)
            ctx.voice_client.play(player,
                                  after=lambda e: print(f"Player error: {e}")
                                  if e else None)

        await ctx.send(f"Reproduciendo: {player.title}")

    @commands.command()
    async def volume(self, ctx, volume: int):
        """Cambia el volumen del bot"""

        if ctx.voice_client is None:
            return await ctx.send("No estoy conectada a un canal de voz.")

        ctx.voice_client.source.volume = volume / 100
        await ctx.send(f"Cambia el volumen a{volume}%")

    @commands.command()
    async def stop(self, ctx):
        """Para y desconecta al bot del canal"""

        await ctx.voice_client.disconnect()

    @play.before_invoke
    @yt.before_invoke
    @stream.before_invoke
    async def ensure_voice(self, ctx):
        if ctx.voice_client is None:
            if ctx.author.voice:
                await ctx.author.voice.channel.connect()
            else:
                await ctx.send("No estas conectado a un canal de voz UwU.")
                raise commands.CommandError(
                    "Author not connected to a voice channel.")
        elif ctx.voice_client.is_playing():
            ctx.voice_client.stop()


bot = commands.Bot(
    command_prefix=commands.when_mentioned_or("$"),
    description="Sangre Nueva pa",
)


@bot.event
async def status_task():
    while True:
        await bot.change_presence(activity=discord.Game("Hola"),
                                  status=discord.Status.idle)
        await asyncio.sleep(3)  # cambia luego de x segundos
        await bot.change_presence(activity=discord.Game("Paja"),
                                  status=discord.Status.idle)
        await asyncio.sleep(3)
        await bot.change_presence(activity=discord.Game("Yuca"),
                                  status=discord.Status.idle)
        await asyncio.sleep(3)
        await bot.change_presence(
            activity=discord.Streaming(name='TurboC es completamente bueno',
                                       url='https://www.twitch.tv/tugfammg'))
        await asyncio.sleep(3)
        await bot.change_presence(activity=discord.Streaming(
            name='Lindos', url='https://www.twitch.tv/tugfammg'))
    await bot.process_commands(status_task)


@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    bot.loop.create_task(status_task()) #crea el loop para los change_presence


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.lower() == "frase":
        quote = get_quote()
        await message.channel.send(quote)

    
    if message.content.lower() == "elmago":
        await message.channel.send(file=discord.File('resources/Mago.jpg'))

    if message.content.lower() == "digod":
        await message.channel.send(file=discord.File('resources/Digod.jpg'))


    if message.content.lower() == "te quiero mucho":
        await message.channel.send(file=discord.File('resources/mp4.gif'))

        await message.add_reaction("🥰")
    if message.content.lower() == "passchipeada":
        await message.channel.send(file=discord.File('resources/leonel.c'))


    if message.content.lower() == "¿quien soy?":
        await message.channel.send('Vos sos @{}'.format(message.author.name))

    if message.content.lower() == "elpepe":
        await message.channel.send(file=discord.File('resources/elpepe.mp4'))

    if message.content.lower() == "crudninja":
        await message.channel.send(file=discord.File('TAREAS/pipe.c'))
        await message.channel.send(file=discord.File('TAREAS/tupapa.h'))
        await message.channel.send(file=discord.File('TAREAS/CRUD.rar'))

    if message.content.startswith("!hello"):
            await message.reply("Hello!", mention_author=True)

    if message.content.lower() == "TC20":
        await message.channel.send(file=discord.File('TAREAS/Munecos.C'))
        await message.channel.send(file=discord.File('TAREAS/tupapa.h'))
        await message.channel.send(file=discord.File('TAREAS/MARIOBROS.h'))

    if message.content.lower() == "GOD":
        await message.channel.send(file=discord.File('resources/lovo.mp4'))


    if message.content.lower() == "logouni3d":
        await message.channel.send(file=discord.File('resources/cuento.c'))
    if message.content.lower() == "chepito":
        await message.channel.send(file=discord.File('video.mp4'))

    await bot.process_commands(message)


async def setup():
    await bot.wait_until_ready()



@bot.command()
async def repeat(ctx, times: int, content="repeating..."):
    """Repite un mensaje muchas veces."""
    for i in range(times):
        await ctx.send(content)


@bot.command()
async def joined(ctx, member: discord.Member):
    """Te dice cuando entro un miembro."""
    await ctx.send(f"{member.name} Entro en{member.joined_at}")

@bot.command(
    # ADDS THIS VALUE TO THE $HELP PRINT MESSAGE.
    help="$say (argumento)",
    # ADDS THIS VALUE TO THE $HELP MESSAGE.
    brief="Repite lo que escribiste")
    
async def say(ctx, *args):
    response = ""
  # Itera el ciclo
    for arg in args:
        response = response + " " + arg

    # manda un mensaje al canal usando el contexto de objeto
    await ctx.channel.send(response)

@bot.command(help="Es para ver si el bot recibe ordenes",
             brief="El bot devuelve Pong! si todo funciona bien.")
async def ping(ctx):
    await ctx.channel.send('Pong!')


@bot.command(help="Documentacion de C modo grafico",
             brief="Lanza documentacion de C grafico")
async def docgrafico(ctx):
    await ctx.channel.send('Documentancion de C grafico')
    await ctx.channel.send(file=discord.File('Documentacion/Doc.pdf'))
    await ctx.channel.send(file=discord.File('Documentacion/EJEM1.c'))

@bot.command(help="Complejidad de algoritmos",
brief="Resumen para medir la complejidad de una estructura de datos en un ejecucion de tiempo real en un algoritmo con soluciones de fuerza bruta")
async def algorspeed(ctx):
  await ctx.channel.send('Complejidad de algoritmo')
  await ctx.channel.send(file=discord.File('resources/complejidad.txt'))
  
bot.add_cog(Music(bot))
bot.loop.create_task(setup())

bot.run(os.getenv('TOKEN'))