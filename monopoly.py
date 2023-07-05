import discord
from discord.ext import commands
import random
import asyncio

def diceroll():
    roll = random.randint(2, 12)

class Property:
    def __init__(self, name, pos, type, price, rent, mortgage_value, color):
        self.name = name
        self.pos = pos
        self.type = type
        self.price = price
        self.rent = rent
        self.mortgage_value = mortgage_value
        self.color = color
        self.owner = None
        self.is_mortgaged = False
        self.num_houses = 0
        self.has_hotel = False

class Player:
    def __init__(self, id, name, pos, bal, properties):
        self.id = id
        self.name = name
        self.pos = pos
        self.bal = bal
        self.properties = []

board = 39
players = []
properties = [Property('Mediterranean Avenue', '1', 'Property', '60', '2', '30', 'brown'),
              Property('Baltic Avenue', '3', 'Property', '60', '4', '30', 'brown'),
              Property('Reading Railroad', '5', 'Railroad', '200', '25', '100', 'null'),
              Property('Oriental Avenue', '6', 'Property', '100', '6', '50', 'light blue'),
              Property('Vermont Avenue', '8', 'Property', '100', '6', '50', 'light blue'),
              Property('Conneticut Avenue', '9', 'Property', '120', '8', '60', 'light blue'),
              Property('St. Charles Place', '11', 'Property', '140', '10', '70', 'magenta'),
              Property('Electric Company', '12', 'Utility', '150', '4', '75', 'null'),
              Property('States Avenue', '13', 'Property', '140', '10', '70', 'magenta'),
              Property('Virginia Avenue', '14', 'Property', '160', '12', '80', 'magenta'),
              Property('Pennsylvania Railroad', '15', 'Railroad', '200', '25', '100', 'null'),
              Property('St. James Place', '16', 'Property', '180', '14', '90', 'orange'),
              Property('Tennessee Avenue', '18', 'Property', '180', '14', '90', 'orange'),
              Property('New York Avenue', '19', 'Property', '200', '16', '100', 'orange'),
              Property('Kentucky Avenue', '21', 'Property', '220', '150', '110', 'red'),
              Property('Indiana Avenue', '23', 'Property', '220', '18', '110', 'red'),
              Property('Illinois Avenue', '24', 'Property', '240', '20', '120', 'red'),
              Property('B&O Railroad', '25', 'Railroad', '200', '25', '100', 'null'),
              Property('Atlantic Avenue', '26', 'Property', '260', '22', '130', 'yellow'),
              Property('Ventnor Avenue', '27', 'Property', '260', '22', '130', 'yellow'),
              Property('Water Works', '28', 'Utility', '150', '4', '75', 'null'),
              Property('Marvin Gardens', '29', 'Property', '280', '24', '140', 'yellow'),
              Property('Pacific Avenue', '31', 'Property', '300', '26', '150', 'green'),
              Property('North Carolina Avenue', '32', 'Property', '300', '26', '150', 'green'),
              Property('Pennsylvania Avenue', '34', 'Property', '320', '28', '160', 'green'),
              Property('Short Line', '35', 'Railroad', '200', '25', '100', 'null'),
              Property('Park Place', '37', 'Property', '350', '35', '175', 'blue'),
              Property('Boardwalk', '39', 'Property', '400', '50', '200', 'blue')]

#go = 0, community chest = 2, 17, 33, income tax = 4, chance = 7, 22, 36, jail = 10, free parking = 20, go to jail = 30, luxury tax = 38

class monopoly(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def monopoly(self, ctx):
        message = await ctx.send("Press the reaction below if you want to play (up to four players):")
        await message.add_reaction('💵')
        def check(reaction, user):
            return str(reaction.emoji) == '💵' and reaction.message.id == message.id
        try:
            while len(players) < 4:
                reaction, user = await self.bot.wait_for('reaction_add', timeout = 30.0, check=check)
                if user not in players:
                    players.append(user.name)
                print(players)
                await ctx.send(str(players[-1]) + " has joined the game!")
        except asyncio.TimeoutError:
            await ctx.send('Countdown for joining players has ended.')
            if len(players) == 1:
                await ctx.send("Only one player has joined, so you will play against the computer")
            else:
                await ctx.send("multiplayer is a work in progress")