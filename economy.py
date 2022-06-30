import discord
from discord.ext import commands
import random
import sqlite3

class economy(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def econtest(self, ctx):
        await ctx.send("working!")

    @commands.command()
    async def register(self,ctx):
        db = sqlite3.connect('main.sqlite')
        cursor = db.cursor()
        cursor.execute("INSERT INTO economy VALUES (1, 600444714856218634, 0, 0, 0)")
        result = cursor.fetchall()
        print(result)
        cursor.close()
        db.close()

    @commands.group(invoke_without_command = True)
    async def casino(self, ctx):
        await ctx.send("Available games: Blackjack, Coinflip\nBet loveca for a chance to win double of what you put in.")

    @casino.command()
    async def blackjack(self, ctx):
        await ctx.send("Work in progress")

    @casino.command()
    async def coinflip(self, ctx):
        await ctx.send("Work in progress2")