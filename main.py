import discord
import os
import requests
import json
from dotenv import load_dotenv
from discord.ext import commands
import asyncio
load_dotenv()
import tracemalloc

tracemalloc.start()


bot = commands.Bot(command_prefix="$")
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
  


bot.run(os.getenv('TOKEN'))
