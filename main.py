import discord
import os
import requests
import json
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio

PREFIX = ("$")
bot = discord.ext.commands.Bot(command_prefix = "!");
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
    await message.channel.send('lo unico que no vas a heredar de tus padres')

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
      await message.channel.send('vos sos @{}'.format(message.author.name))

  if message.content.startswith('paja'):
        myid = '<@244069957187534848>'
        await message.channel.send(message.channel, ' : %s is the best ' % myid)

async def status_task():
    while True:
        await bot.change_presence(activity=discord.Game("turca"), status=discord.Status.online)
        await asyncio.sleep(3) # Changes after x seconds
        await bot.change_presence(activity=discord.Game("paja"), status=discord.Status.online)
        await asyncio.sleep(3)
        await bot.change_presence(activity=discord.Game("pornhub"), status=discord.Status.online)
        await asyncio.sleep(3)

print(os.getenv("TOKEN"))
bot.run(os.getenv('TOKEN'))
