import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
from musicCommands import musicCommands
from economy import economy
from otherCommands import otherCommands

load_dotenv()

bot = commands.Bot(command_prefix='!', intents = discord.Intents.all())

@bot.event
async def on_ready():
    await bot.add_cog(musicCommands(bot))
    await bot.add_cog(otherCommands(bot))
    await bot.add_cog(economy(bot))
    print('{0.user} launching...'.format(bot))
    return await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="a cassette tape"))

#@bot.command()
#async def hello(ctx):
    #authorID = ctx.message.author.id
    #if authorID == 600444714856218634:
        #await ctx.reply('Hello Sherry!')
    #else:
        #await ctx.reply('Hello!')

#@bot.command()
#async def database(ctx):
    #db = sqlite3.connect('main.sqlite')
    #cursor = db.cursor()
    #cursor.execute(f"SELECT userID FROM economy WHERE # = 1")
    #result = cursor.fetchone()
    #print(result)
    #cursor.close()
    #db.close()

bot.run(os.environ['TOKEN'])