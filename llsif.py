import discord
from discord.ext import commands
from discord.ui import Button, View
import random
import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'root',
    database = 'unit01'
)

cursor = mydb.cursor(dictionary = True)

class llsif(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def scout(self, ctx, arg = None):
        if arg == None:
            await ctx.send("Missing argument after command: please choose either honor or regular scouting")
        elif str(arg) == "honor":
            info = "Honor scouting has only rare members and above. Scouting 11 cards costs 50 loveca, and scouting once costs 5 loveca.\nRates: 1% UR, 9% SR, 90% R.\nScouting 11 has a guaranteed SR or higher"
        elif str(arg) == "regular":
            info = "Regular scouting has only normal and rare members.\nRates: 5% R, 95% N"
        else:
            await ctx.send("Invalid argument: please type either honor or regular after command")
        
        button = Button(label = "Scout 11", style = discord.ButtonStyle.primary)
        button2 = Button(label = "Scout 1", style = discord.ButtonStyle.grey)

        view = View()
        view.add_item(button)
        view.add_item(button2)

        async def buttonCallback(interaction):
            if interaction.user == ctx.author:
                view.clear_items()
                await botMessage.edit(view = None)
                if str(arg) == "honor":
                    i = 0
                    result = random.randint(0, 20)
                    if result == (20, 19, 18):
                        cursor.execute(f"select * from Cards where rarity = 'UR' order by rand() limit 1")
                    else:
                        cursor.execute(f"select * from Cards where rarity = 'SR' order by rand() limit 1")
                    rows = cursor.fetchall()
                    for row in rows:
                        await ctx.send(row["img"])
                    while i <= 9:
                        result = random.randint(0, 99)
                        if result == (99):
                            cursor.execute(f"select * from Cards where rarity = 'UR' order by rand() limit 1")
                        elif result == (98, 97, 96, 95, 94, 93, 92, 91, 90):
                            cursor.execute(f"select * from Cards where rarity = 'SR' order by rand() limit 1")
                        else:
                            cursor.execute(f"select * from Cards where rarity = 'R' order by rand() limit 1")
                        rows = cursor.fetchall()
                        for row in rows:
                            await ctx.send(row["img"])
                        i += 1
                elif str(arg) == "regular":
                    i = 0
                    while i <= 10:
                        result = random.randint(0, 99)
                        if result == (99, 98, 97, 96, 95):
                            cursor.execute(f"select * from Cards where rarity = 'R' order by rand() limit 1")
                        else:
                            cursor.execute(f"select * from Cards where rarity = 'N' order by rand() limit 1")
                            rows = cursor.fetchall()
                        for row in rows:
                            await ctx.send(row["img"])
                        i += 1

            else:
                await interaction.response.send_message("You are not the one playing.")
        async def button2Callback(interaction):
            if interaction.user == ctx.author:
                view.clear_items()
                await botMessage.edit(view = None)
                if str(arg) == "honor":
                    result = random.randint(0, 99)
                    if result == (99):
                        cursor.execute(f"select * from Cards where rarity = 'UR' order by rand() limit 1")
                    elif result == (98, 97, 96, 95, 94, 93, 92, 91, 90):
                        cursor.execute(f"select * from Cards where rarity = 'SR' order by rand() limit 1")
                    else:
                        cursor.execute(f"select * from Cards where rarity = 'R' order by rand() limit 1")
                    rows = cursor.fetchall()
                    for row in rows:
                        await ctx.send("Your card: " + row["img"])
                elif str(arg) == "regular":
                    result = random.randint(0, 99)
                    if result == (99, 98, 97, 96, 95):
                        cursor.execute(f"select * from Cards where rarity = 'R' order by rand() limit 1")
                    else:
                        cursor.execute(f"select * from Cards where rarity = 'N' order by rand() limit 1")
                    rows = cursor.fetchall()
                    for row in rows:
                        await ctx.send("Your card: \n" + row["img"])
            else:
                await interaction.response.send_message("You are not the one playing.")
        button.callback = buttonCallback
        button2.callback = button2Callback

        if str(arg) == "honor":
            botMessage = await ctx.send(info, view = view)
        elif str(arg) == "regular":
            botMessage = await ctx.send(info, view = view)