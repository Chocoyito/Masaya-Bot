
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


intents = discord.Intents.all()
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
    "0.0.0.0",  # bind to ipv4 since ipv6 addresses cause issues sometimes
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

        await ctx.send(f"🎶 Reproduciendo: {player.title} 🎶")

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

        await ctx.send(f"🎶 Reproduciendo:  {player.title}  🎶")

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



@bot.event
async def status_task():
    while True:
        await bot.change_presence(activity=discord.Game("Lovo lindo"),
                                  status=discord.Status.idle)
        await asyncio.sleep(3)  # cambia luego de x segundos
        await bot.change_presence(activity=discord.Game("Paja"),
                                  status=discord.Status.idle)
        await asyncio.sleep(3)
        await bot.change_presence(activity=discord.Game("Pornhub"),
                                  status=discord.Status.idle)
        await asyncio.sleep(3)
        await bot.change_presence(
            activity=discord.Streaming(name='TurboC es completamente basura',
                                       url='https://www.twitch.tv/tugfammg'))
        await asyncio.sleep(3)
        await bot.change_presence(activity=discord.Streaming(
            name='Roberto lindo', url='https://www.twitch.tv/tugfammg'))
    await bot.process_commands(status_task)

@bot.event
async def on_raw_reaction_add(payload):
    if payload.member.bot:
      pass
    else:

      with open('reactrole.json') as react_file:
        data = json.load(react_file)
        for x in data:
          if x['emoji'] == payload.emoji.name and x['message_id'] == payload.message_id:
            role = discord.utils.get(bot.get_guild(payload.guild_id).roles, id=x['role_id'])  
            await payload.member.add_roles(role)

@bot.event
async def on_raw_reaction_remove(payload):

    with open('reactrole.json') as react_file:
        data = json.load(react_file)
        guild = bot.get_guild(payload.guild_id)
     
        member = guild.get_member(payload.user_id)
        for x in data:
            if x['emoji'] == payload.emoji.name:
                role = discord.utils.get(bot.get_guild(
                    payload.guild_id).roles, id=x['role_id'])

        
                await member.remove_roles(role)


@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    bot.loop.create_task(status_task())  # Create loop/task

  

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.lower() == "frase":
        quote = get_quote()
        await message.channel.send(quote)

    if message.content.lower() == "yon":
        await message.channel.send('Mi hombre')
        await message.channel.send(file=discord.File('resources/YON.jpg'))
    
    if message.content.lower() == "elmago":
        await message.channel.send(file=discord.File('resources/Mago.jpg'))

    if message.content.lower() == "digod":
        await message.channel.send(file=discord.File('resources/Digod.jpg'))

    if message.content.lower() == "sexo":
        await message.channel.send(
            'Lo unico que no vas a heredar de tus padres.')

    if message.content.lower() == "rodrigo":
        await message.channel.send(
            'Anda busca como estudiar tilin.')
        await message.channel.send(file=discord.File('resources/loli.jpg'))

    if message.content.lower() == "leonel":
        await message.channel.send(file=discord.File('resources/esposa.jpg'))

    if message.content.lower() == "te quiero mucho":
        await message.channel.send(file=discord.File('resources/mp4.gif'))
        await message.add_reaction("🥰")
    if message.content.lower() == "passchipeada":
        await message.channel.send(file=discord.File('resources/leonel.c'))

    if message.content.lower() == "infravalorada":
        await message.channel.send(file=discord.File('resources/yichu.jpg'))

    if message.content.lower() == "¿quien soy?":
        await message.channel.send('Vos sos @{}'.format(message.author.name))

    if message.content.lower() == "elpepe":
        await message.channel.send(file=discord.File('resources/elpepe.mp4'))

    if message.content.startswith("!hello"):
            await message.reply("Hello!", mention_author=True)

    if message.content.lower() == "grevinpaja":
        await message.channel.send(file=discord.File('TAREAS/Munecos.C'))
        await message.channel.send(file=discord.File('TAREAS/tupapa.h'))
        await message.channel.send(file=discord.File('TAREAS/MARIOBROS.h'))

    if message.content.lower() == "lovo":
        await message.channel.send(file=discord.File('resources/lovo.mp4'))

    if message.content.lower() == "*dormir*":
        await message.reply('¿Vamos a dormir (。U⁄ ⁄ω⁄ ⁄ U。)??', mention_author=True)
        await message.add_reaction("😳")
        await message.channel.send(file=discord.File('waifu/dormir.png'))

    if message.content.lower() == "*me siento triste*":
        await message.channel.send('¿Que tenés bb? contame u.u')
        await message.channel.send(file=discord.File('waifu/triste.gif'))

    if message.content.lower() == "*te cuento*":
        await message.channel.send('contame')
        await message.channel.send(file=discord.File('waifu/contame.gif'))

    if message.content.lower().startswith("lo que pasa es que"):
        await message.channel.send('¿Y como te hace sentir eso?')
        await message.channel.send(file=discord.File('waifu/feeling.gif'))

    if message.content.lower() == "logouni3d":
        await message.channel.send(file=discord.File('resources/cuento.c'))

    if message.content.lower().startswith("$repeat"):
      await message.channel.send("(!) Comando deshabilitado temporalmente. (!)")
    await bot.process_commands(message)


async def setup():
    await bot.wait_until_ready()


async def on_message_delete(self, message):
    msg = f"{message.author} has deleted the message: {message.content}"
    await message.channel.send(msg)



'''
@bot.command()
async def repeat(ctx, times: int, content="repeating..."):
    """Repeats a message multiple times."""
    for i in range(10):
        await ctx.send(content)
'''

@bot.command()

async def joined(ctx, member: discord.Member):
      """Says when a member joined."""
      await ctx.send(f"{member.name} Entro una puta en {member.joined_at}")

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

@bot.command(help="Lista de servidores",
  brief="Displayea una lista de servidores donde se encuentra el bot")
async def servidores(ctx):
    await ctx.channel.send("Estoy en " + str(len(bot.guilds)) + " servidores!")

@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
      username_1 = ctx.message.author.name
      avatar_1 = ctx.message.author.avatar_url
      avatar_2 = member.avatar_url
      await member.kick(reason=reason)
      embed=discord.Embed(title=f'El usuario {member} ha sido brutalmente turqueado', icon_url=avatar_2)
      embed.set_author(name=f"Realizado por {username_1}", icon_url=avatar_1)
      await ctx.send(embed=embed)

format = "%a, %d %b %Y | %H:%M:%S %ZGMT"

@bot.command()
async def serverinfo(ctx):
      if isinstance(ctx.channel, discord.channel.DMChannel):
          emb = discord.Embed(title="Comando Invalido",description=f":warning:```Este comando solo puede ser utilizado en un servidor.```")
          emb.set_thumbnail(url = bot.user.avatar_url)
          emb.set_footer(text="\n\nMuchas Gracias por utilizarme. 🥰", icon_url="")
          await ctx.send(embed=emb)
      else:
        embed = discord.Embed(
        )
        text_channels = len(ctx.guild.text_channels)
        voice_channels = len(ctx.guild.voice_channels)
        categories = len(ctx.guild.categories)
        channels = text_channels + voice_channels
        embed.set_thumbnail(url = str(ctx.guild.icon_url))
        embed.add_field(name = f"Information About **{ctx.guild.name}**: ", value = f":white_small_square: ID: **{ctx.guild.id}** \n:white_small_square: Owner: **{ctx.guild.owner}** \n:white_small_square: Location: **{ctx.guild.region}** \n:white_small_square: Creation: **{ctx.guild.created_at.strftime(format)}** \n:white_small_square: Members: **{ctx.guild.member_count}** \n:white_small_square: Channels: **{channels}** Channels; **{text_channels}** Text, **{voice_channels}** Voice, **{categories}** Categories \n:white_small_square: Verification: **{str(ctx.guild.verification_level).upper()}** \n:white_small_square: Features: {', '.join(f'**{x}**' for x in ctx.guild.features)} \n:white_small_square: Splash: {ctx.guild.splash}")
        await ctx.send(embed=embed)

@bot.command()
async def avatar(ctx, *,  avamember : discord.Member=None):
      userAvatarUrl = avamember.avatar_url
      await ctx.send(userAvatarUrl)

@bot.command()
@commands.has_permissions(administrator=True, manage_roles=True)
async def reactrole(ctx,emoji,role: discord.Role,titulo,*,message):

    emb = discord.Embed(title=titulo,description=message)
    emb.set_thumbnail(url = bot.user.avatar_url)
    emb.set_footer(icon_url = ctx.author.avatar_url,text=f"Creado por {ctx.author.name}")
    msg = await ctx.channel.send(embed=emb)
    await msg.add_reaction(emoji)
    
    with open('reactrole.json') as json_file:
      data = json.load(json_file)

      new_react_role = {
        'role_name':role.name,
        'role_id':role.id,
        'emoji': emoji,
        'message_id': msg.id
      }
      data.append(new_react_role)
      
    with open('reactrole.json','w') as j:
      json.dump(data,j,indent=4)


bot.add_cog(Music(bot))
bot.loop.create_task(setup())
bot.load_extension("cogs.simple")
# bot.load_extension("cogs.comandos")
bot.load_extension("cogs.music")
bot.run(os.getenv('TOKEN'))