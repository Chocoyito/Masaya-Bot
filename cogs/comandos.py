import discord
import json
from discord.ext import commands


class Comandos(commands.Cog):
  def __init__(self, bot):
      self.bot = bot

  @commands.command()
  async def joined(ctx, member: discord.Member):
      """Says when a member joined."""
      await ctx.send(f"{member.name} Entro una puta en {member.joined_at}")

  @commands.command(
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

  @commands.command(help="Es para ver si el bot recibe ordenes",
              brief="El bot devuelve Pong! si todo funciona bien.")
  async def ping(ctx):
      await ctx.channel.send('Pong!')


 @commands.command(help="Documentacion de C modo grafico",
              brief="Lanza documentacion de C grafico")
  async def docgrafico(ctx):
      await ctx.channel.send('Documentancion de C grafico')
      await ctx.channel.send(file=discord.File('Documentacion/Doc.pdf'))
      await ctx.channel.send(file=discord.File('Documentacion/EJEM1.c'))

 @commands.command(help="Complejidad de algoritmos",
  brief="Resumen para medir la complejidad de una estructura de datos en un ejecucion de tiempo real en un algoritmo con soluciones de fuerza bruta")
  async def algorspeed(ctx):
    await ctx.channel.send('Complejidad de algoritmo')
    await ctx.channel.send(file=discord.File('resources/complejidad.txt'))

 @commands.command(help="Lista de servidores",
  brief="Displayea una lista de servidores donde se encuentra el bot")
  async def servidores(ctx):
    await ctx.channel.send("Estoy en " + str(len(bot.guilds)) + " servidores!")

 @commands.command()
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

 @commands.command()
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

 @commands.command()
  async def avatar(ctx, *,  avamember : discord.Member=None):
      userAvatarUrl = avamember.avatar_url
      await ctx.send(userAvatarUrl)

 @commands.command()
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

def setup(bot):
    bot.add_cog(Comandos(bot))