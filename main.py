import discord
import os
import requests
import json
from dotenv import load_dotenv
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

  if message.content.lower()=="$comandos":
    commandlist = ['te quiero mucho', 'yon', 'leonel', 'sexo','$comandos']
    comandos = ""
    comandos += commandlist
    for a,b,c in zip(commandlist[::2],commandlist[2::3],commandlist[3::4]):
       print ('{:<30}{:<30}{:<}'.format(a,b,c))
    await message.channel.send(comandos)  

  if message.content.lower()=="infravalorada" :
    await message.channel.send(file=discord.File('resources/yichu.jpg'))

  if message.content.lower()=="¿quien soy?":
      await message.channel.send('Vos sos @{}'.format(message.author.name))

  if message.content.startswith('paja'):
        myid = '<@244069957187534848>'
        await message.channel.send(message.channel, ' : %is the best ' % myid)    
  await bot.process_commands(message)

async def status_task():
    while True:
        await bot.change_presence(activity=discord.Game("Turca"), status=discord.Status.online)
        await asyncio.sleep(3) # Changes after x seconds
        await bot.change_presence(activity=discord.Game("Paja"), status=discord.Status.online)
        await asyncio.sleep(3)
        await bot.change_presence(activity=discord.Game("Pornhub"), status=discord.Status.online)
        await asyncio.sleep(3)
    await bot.process_commands()
    
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

	# LOOPS THROUGH THE LIST OF ARGUMENTS THAT THE USER INPUTS.
	for arg in args:
		response = response + " " + arg

	# SENDS A MESSAGE TO THE CHANNEL USING THE CONTEXT OBJECT.
	await ctx.channel.send(response)
  
class Player(commands.Cog):
    def __init__(self, bot):
        self.bot = bot 
        self.song_queue = {}

        self.setup()

    def setup(self):
        for guild in self.bot.guilds:
            self.song_queue[guild.id] = []

    async def check_queue(self, ctx):
        if len(self.song_queue[ctx.guild.id]) > 0:
            ctx.voice_client.stop()
            await self.play_song(ctx, self.song_queue[ctx.guild.id][0])
            self.song_queue[ctx.guild.id].pop(0)

    async def search_song(self, amount, song, get_url=False):
        info = await self.bot.loop.run_in_executor(None, lambda: youtube_dl.YoutubeDL({"format" : "bestaudio", "quiet" : True}).extract_info(f"ytsearch{amount}:{song}", download=False, ie_key="YoutubeSearch"))
        if len(info["entries"]) == 0: return None

        return [entry["webpage_url"] for entry in info["entries"]] if get_url else info

    async def play_song(self, ctx, song):
        url = pafy.new(song).getbestaudio().url
        ctx.voice_client.play(discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(url)), after=lambda error: self.bot.loop.create_task(self.check_queue(ctx)))
        ctx.voice_client.source.volume = 0.5

    @commands.command()
    async def join(self, ctx):
        if ctx.author.voice is None:
            return await ctx.send("Por favor metete en un canal de voz para que yo pueda meterme, me da miedo :c.")

        if ctx.voice_client is not None:
            await ctx.voice_client.disconnect()

        await ctx.author.voice.channel.connect()

    @commands.command()
    async def leave(self, ctx):
        if ctx.voice_client is not None:
            return await ctx.voice_client.disconnect()

        await ctx.send("No estoy conectada en un canal de voz.")

    @commands.command()
    async def play(self, ctx, *, song=None):
        if song is None:
            return await ctx.send("Inclui una canción paja.")

        if ctx.voice_client is None:
            return await ctx.send("Tengo que estar metida en un canal de voz.")

        # handle song where song isn't url
        if not ("youtube.com/watch?" in song or "https://youtu.be/" in song):
            await ctx.send("Buscando tu mierda, dame chance.")

            result = await self.search_song(1, song, get_url=True)

            if result is None:
                return await ctx.send("Loco vos hablas miskito o que onda?, escribi bien esa paja.")

            song = result[0]

        if ctx.voice_client.source is not None:
            queue_len = len(self.song_queue[ctx.guild.id])

            if queue_len < 10:
                self.song_queue[ctx.guild.id].append(song)
                return await ctx.send(f"I am currently playing a song, this song has been added to the queue at position: {queue_len+1}.")

            else:
                return await ctx.send("Sorry, I can only queue up to 10 songs, please wait for the current song to finish.")

        await self.play_song(ctx, song)
        await ctx.send(f"Reproduciendo: {song}")

    @commands.command()
    async def search(self, ctx, *, song=None):
        if song is None: return await ctx.send("Te falto poner un nombre de una cancion on un link valido.")

        await ctx.send("Buscando esa mierda...")

        info = await self.search_song(5, song)

        embed = discord.Embed(title=f"Los resultados de '{song}':", description="*You can use these URL's to play an exact song if the one you want isn't the first result.*\n", colour=discord.Colour.red())
        
        amount = 0
        for entry in info["entries"]:
            embed.description += f"[{entry['title']}]({entry['webpage_url']})\n"
            amount += 1

        embed.set_footer(text=f"Displaying the first {amount} results.")
        await ctx.send(embed=embed)

    @commands.command()
    async def queue(self, ctx): # display the current guilds queue
        if len(self.song_queue[ctx.guild.id]) == 0:
            return await ctx.send("No hay canciones en cola actualmente.")

        embed = discord.Embed(title="Cola de canciones", description="", colour=discord.Colour.dark_gold())
        i = 1
        for url in self.song_queue[ctx.guild.id]:
            embed.description += f"{i}) {url}\n"

            i += 1

        embed.set_footer(text="Gracias por usarme!")
        await ctx.send(embed=embed)

    @commands.command()
    async def skip(self, ctx):
        if ctx.voice_client is None:
            return await ctx.send("No estoy reproduciendo ninguna canción.")

        if ctx.author.voice is None:
            return await ctx.send("No estas conectado en ningun canal de voz.")

        if ctx.author.voice.channel.id != ctx.voice_client.channel.id:
            return await ctx.send("No te estoy reproduciendo ninguna canción a tí.")

        poll = discord.Embed(title=f"Votacion para quitar por - {ctx.author.name}#{ctx.author.discriminator}", description="**80% del canal de voz tiene que estar de acuerdo para quitarla.**", colour=discord.Colour.blue())
        poll.add_field(name="Skip", value=":white_check_mark:")
        poll.add_field(name="Stay", value=":no_entry_sign:")
        poll.set_footer(text="Voting ends in 15 seconds.")

        poll_msg = await ctx.send(embed=poll) # only returns temporary message, we need to get the cached message to get the reactions
        poll_id = poll_msg.id

        await poll_msg.add_reaction(u"\u2705") # yes
        await poll_msg.add_reaction(u"\U0001F6AB") # no
        
        await asyncio.sleep(15) # 15 seconds to vote

        poll_msg = await ctx.channel.fetch_message(poll_id)
        
        votes = {u"\u2705": 0, u"\U0001F6AB": 0}
        reacted = []

        for reaction in poll_msg.reactions:
            if reaction.emoji in [u"\u2705", u"\U0001F6AB"]:
                async for user in reaction.users():
                    if user.voice.channel.id == ctx.voice_client.channel.id and user.id not in reacted and not user.bot:
                        votes[reaction.emoji] += 1

                        reacted.append(user.id)

        skip = False

        if votes[u"\u2705"] > 0:
            if votes[u"\U0001F6AB"] == 0 or votes[u"\u2705"] / (votes[u"\u2705"] + votes[u"\U0001F6AB"]) > 0.79: # 80% or higher
                skip = True
                embed = discord.Embed(title="La cancion se ha quitado correctamente", description="***La votacion para quitarla ganó, quitando ahora.***", colour=discord.Colour.green())

        if not skip:
            embed = discord.Embed(title="Falló", description="*La votacion para quitar la cancion actual ha fallado .*\n\n**Votación fallida, requiere al menos una aprobacion del 80% de los usuarios.**", colour=discord.Colour.red())

        embed.set_footer(text="Votación finalizada.")

        await poll_msg.clear_reactions()
        await poll_msg.edit(embed=embed)

        if skip:
            ctx.voice_client.stop()
            await self.check_queue(ctx)


    @commands.command()
    async def pause(self, ctx):
        if ctx.voice_client.is_paused():
            return await ctx.send("Ya fui pausada.")

        ctx.voice_client.pause()
        await ctx.send("La canción fue pausada.")

    @commands.command()
    async def resume(self, ctx):
        if ctx.voice_client is None:
            return await ctx.send("No estoy conectada a ningun canal de voz.")

        if not ctx.voice_client.is_paused():
            return await ctx.send("Ya estoy reproduciendo una musica.")
        
        ctx.voice_client.resume()
        await ctx.send("La musica actual fue reanudada.")

async def setup():
    await bot.wait_until_ready()
    bot.add_cog(Player(bot))

bot.loop.create_task(setup())


bot.run(os.getenv('TOKEN'))
