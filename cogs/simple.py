import discord
from discord.ext import commands



"""Ejemplo de cogs que estoy siguiendo 14/11/2021"""

class SimpleCog(commands.Cog):
    """SimpleCog"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='add', aliases=['plus'])
    @commands.guild_only()
    async def do_addition(self, ctx, first: int, second: int):
        """Comando Simple para sumar (Prueba de Cogs."""

        total = first + second
        await ctx.send(f'The sum of **{first}** and **{second}**  is  **{total}**')

    @commands.command(name='me')
    @commands.is_owner()
    async def only_me(self, ctx):
        """Comando simple que solo le responde al dueño."""

        await ctx.send(f'Hello {ctx.author.mention}. This command can only be used by you!!')

    @commands.command(name='embeds')
    @commands.guild_only()
    async def example_embed(self, ctx):
        """Comando de ejemplo para los embeds, con esto se realizo el comando $reactrole.
        xD."""

        embed = discord.Embed(title='Example Embed',
                              description='Ejemplo de uso de embeds.',
                              colour=0x98FB98)
        embed.set_author(name='MysterialPy',
                         url='https://gist.github.com/MysterialPy/public',
                         icon_url='http://i.imgur.com/ko5A30P.png')
        embed.set_image(url='https://cdn.discordapp.com/attachments/84319995256905728/252292324967710721/embed.png')

        embed.add_field(name='Embed Visualizer', value='[Click Here!](https://leovoel.github.io/embed-visualizer/)')
        embed.add_field(name='Command Invoker', value=ctx.author.mention)
        embed.set_footer(text='Made in Python with discord.py@rewrite', icon_url='http://i.imgur.com/5BFecvA.png')

        await ctx.send(content='**A simple Embed for discord.py@rewrite in cogs.**', embed=embed)
    
    @commands.Cog.listener()
    async def on_member_ban(self, guild, user):
      

        print(f'{user.name}-{user.id} was banned from {guild.name}-{guild.id}')


def setup(bot):
    bot.add_cog(SimpleCog(bot))
