import discord
import shutil
import os

import wikipedia
from discord.ext import commands

class Wikipedia(commands.Cog):
    """Busca la mayoria de cosas en wikipedia"""
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["wiki", "w"],
    brief="Busca lo que sea en wikipedia, tienes que ser especifico.")
    async def wikipedia(self, ctx, *query):
        thequery = " ".join(query)
        link = wikipedia.page(thequery)
        await ctx.send(link.url)


def setup(bot):
    bot.add_cog(Wikipedia(bot))