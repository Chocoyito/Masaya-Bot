import discord
import os
import requests
import json

client = discord.Client()

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

@client.event
async def on_ready():
  print('We have logged in as {0.user}'
  .format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('$frase'):
    quote=get_quote() 
    await message.channel.send(quote)

  if message.content.startswith('yon'):
    await message.channel.send('Mi hombre')
    await message.channel.send(file=discord.File('resources/YON.jpg'))

  if message.content.startswith('sexo'):
    await message.channel.send('lo unico que no vas a heredar de tus padres')

  if message.content.startswith('leonel'):
    await message.channel.send(file=discord.File('resources/esposa.jpg'))

  if message.content.startswith('te quiero mucho'):
    await message.channel.send(file=discord.File('resources/mp4.gif'))

  if message.content.startswith('$comandos'):
    commandlist = ['te quiero mucho', 'yon', 'leonel', 'sexo','$comandos']
    comandos = commandlist
    for a,b,c in zip(commandlist[::2],commandlist[2::3],commandlist[3::4]):
        print ('{:<30}{:<30}{:<}'.format(a,b,c))
    await message.channel.send(comandos)        
    

print(os.getenv("TOKEN"))
client.run(os.getenv('TOKEN'))

