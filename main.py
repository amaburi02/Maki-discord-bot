import discord
from discord.ext import commands
import os
import mysql.connector
from dotenv import load_dotenv
from musicCommands import musicCommands
from economy import economy
from otherCommands import otherCommands

load_dotenv()

bot = commands.Bot(command_prefix='!', intents = discord.Intents.all())
mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'root',
    database = 'unit01'
)

cursor = mydb.cursor(dictionary = True)

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

@bot.command()
async def userinfo(ctx):
    cursor.execute(f"select * from User where userID = {ctx.author.id}")

    rows = cursor.fetchall()
    for row in rows:
        await ctx.send("UserID: " + str(row["userID"]))
        await ctx.send("Loveca: " + str(row["loveca"]))
        await ctx.send("Blue Tickets: " + str(row["bt"]))

@bot.command()
async def register(ctx):
    sql = "insert into User (userID, loveca, bt) values (%s, %s, %s)"
    val = (ctx.author.id, "50", "0")
    cursor.execute(sql, val)
    await ctx.send("You are now registered!")

@bot.command()
async def bal(ctx):
    cursor.execute(f"select loveca from User where userID = {ctx.author.id}")

    rows = cursor.fetchall()
    for row in rows:
        await ctx.send("Loveca: " + str(row["loveca"]))

@bot.command()
async def cardimgtest(ctx):
    cursor.execute(f"select img from Cards where cardID = 1")

    rows = cursor.fetchall()
    for row in rows:
        await ctx.send(row["img"])


bot.run(os.environ['TOKEN'])