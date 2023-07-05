import discord
from discord.ext import commands
from discord.ui import Button, View
import random

class economy(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def econtest(self, ctx):
        await ctx.send("working!")

    @commands.command()
    async def coinflipbet(self, ctx, arg):
        result = random.randint(0, 1)
        headsButton = Button(label = "Heads", style = discord.ButtonStyle.primary)
        tailsButton = Button(label = "Tails", style = discord.ButtonStyle.red)
        view = View()
        view.add_item(headsButton)
        view.add_item(tailsButton)
        initial = arg
        newAmount = (int(arg) * 2)
        print(newAmount)

        async def buttonCallback(interaction):
            userChoice = 0
            if interaction.user == ctx.author:
                view.clear_items()
                await botMessage.edit(view = None)
                if (result == userChoice):
                    await interaction.response.send_message("It landed on heads! So you recieve " + str(newAmount) + " loveca in return!")
                else:
                    await interaction.response.send_message("It landed on tails! Better luck next time.")
            else:
                await interaction.response.send_message("You are not the one playing.")
        async def button2Callback(interaction):
            userChoice = 1
            if interaction.user == ctx.author:
                view.clear_items()
                await botMessage.edit(view = None)
                if (result == userChoice):
                    await interaction.response.send_message("It landed on tails! So you recieve " + str(newAmount) + " loveca in return!")
                else:
                    await interaction.response.send_message("It landed on heads! Better luck next time.")
            else:
                await interaction.response.send_message("You are not the one playing.")
        headsButton.callback = buttonCallback
        tailsButton.callback = button2Callback

        botMessage = await ctx.send("You chose to bet " + str(initial) + " loveca.", view = view)

    @commands.group(invoke_without_command = True)
    async def casino(self, ctx):
        await ctx.send("Available games: Coinflip, Blackjack\nBet loveca for a chance to win double of what you put in.")

    @casino.command()
    async def coinflip(self, ctx):
        await ctx.send("Work in progress")

    @casino.command()
    async def blackjack(self, ctx):
        deck = ["A", "A", "A", "A", "2", "2", "2", "2", "3", "3", "3", "3", "4", "4", "4", "4", "5", "5", "5", "5", "6", "6", "6", "6", "7", "7", "7", "7", "8", "8", "8", "8", "9", "9", "9", "9", "10", "10", "10", "10", "J", "J", "J", "J", "Q", "Q", "Q", "Q", "K", "K", "K", "K"]
        deckDict = {
            "A+" : 11,
            "A-" : 1,
            "2" : 2,
            "3" : 3,
            "4" : 4,
            "5" : 5,
            "6" : 6,
            "7" : 7,
            "8" : 8,
            "9" : 9,
            "10" : 10,
            "J" : 10,
            "Q" : 10,
            "K" : 10
        }
        playerScore = 0
        dealerScore = 0
        playerCards = []
        dealerCards = []

        i = 0
        while i < 2:
            playerPick = random.choice(deck)
            deck.remove(playerPick)
            dealerPick = random.choice(deck)
            deck.remove(dealerPick)
            print(deck)
            playerCards.append(playerPick)
            dealerCards.append(dealerPick)
            i += 1
        await ctx.send("Your cards: " + str(playerCards) + "\nDealer's Cards: " + str(dealerCards[0]) + " + unknown")
        #button = Button(label = "test", style = discord.ButtonStyle.primary)