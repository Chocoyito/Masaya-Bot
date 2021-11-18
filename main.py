
import discord
from dotenv import load_dotenv
import os
import requests
import json
from discord.ext import commands
import asyncio
load_dotenv()
import tracemalloc


intents = discord.Intents.all()
intents.members = True

bot = commands.Bot(command_prefix="$", intents=intents)
tracemalloc.start()


def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return (quote)

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

    if message.content.lower() == "*yon*":
        await message.channel.send('Mi hombre')
        await message.channel.send(file=discord.File('resources/YON.jpg'))

    if message.content.lower() == "*sexo*":
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

    if message.content.lower().startswith("*lo que pasa es que*"):
        await message.channel.send('¿Y como te hace sentir eso?')
        await message.channel.send(file=discord.File('waifu/feeling.gif'))

    if message.content.lower() == "logouni3d":
        await message.channel.send(file=discord.File('resources/cuento.c'))

    await bot.process_commands(message)


async def setup():
    await bot.wait_until_ready()


async def on_message_delete(self, message):
    msg = f"{message.author} has deleted the message: {message.content}"
    await message.channel.send(msg)


@bot.command()

async def joined(ctx, member: discord.Member):
      """Dice la fecha exacta cuando entro un miembro."""
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

@bot.command(brief="Expulsa un miembro del servidor (El bot tiene que tener mayor rango que el miembro a expulsar).")
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


bot.loop.create_task(setup())
bot.load_extension("cogs.simple")
# bot.load_extension("cogs.comandos")
bot.load_extension("cogs.music")
bot.load_extension("cogs.wiki")
bot.run(os.getenv('TOKEN'))