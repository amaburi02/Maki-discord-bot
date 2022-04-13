import discord
from discord.ext import commands
from musicCommands import musicCommands
from otherCommands import otherCommands
import sqlite3
import os
from dotenv import load_dotenv
load_dotenv()

bot = commands.Bot(command_prefix='!', intents = discord.Intents.all())

bot.add_cog(musicCommands(bot))
bot.add_cog(otherCommands(bot))

@bot.event
async def on_ready():
    #db = sqlite3.connect('main.sqlite')
    #cursor = db.cursor()
    #cursor.execute('''
    #CREATE TABLE IF NOT EXISTS main(
    #Name TEXT,
    #Amount TEXT,
    #)
    #''')
    print('{0.user} launching...'.format(bot))
    return await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="a cassette tape"))

@bot.command()
async def hello(ctx):
    authorID = ctx.message.author.id
    if authorID == 600444714856218634:
        await ctx.reply('Hello Sherry!')
    else:
        await ctx.reply('Hello!')

bot.run(os.environ['TOKEN'])