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