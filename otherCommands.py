import discord
from discord.ext import commands
import random

class otherCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def commandlist(self,ctx):
        await ctx.send("```Music Commands: \n !getinthevcshinji - makes bot join voice channel or switch voice "
                       "channels to the one you're using \n !quit - makes bot leave voice channel \n !play [url] - "
                       "paste youtube URL after command and it will play the audio from the video \n !pause - pauses "
                       "the music \n !resume - resumes the music \n !stop - stops the music \n !add [url] - adds a "
                       "song to the queue \n !skip - plays next song in the queue \n !previous - plays previous song "
                       "\n !restart - restarts the song \n !switch [url] - plays your url and and puts what was already playing at the top of the song queue. \n !addnext - will put the song in the front of the queue so "
                       "it plays next \n !deletenext - deletes the next song in the queue \n !deletelast - deletes "
                       "the last song in the queue in case you make a typo \n !clearqueue - deletes all songs in "
                       "queue \n !shufflequeue - shuffles the queue \n !search [searchquery] [int] - searches youtube "
                       "and returns top video in results. Won't add song to queue, this function is just to save time "
                       "from searching on youtube yourself. Top result starts at 0. Searching without specifying int "
                       "will return top result. \n \nExtra Commands: \n !fatefranchisewatchorder - pulls up watch "
                       "order for the Fate franchise \n !coinflip - flips a coin \n !diceroll [int 1 or 2] - rolls "
                       "one dice or 2 \n !commandlist - pulls up this list \n !problemshelp - stuff to read if "
                       "something isn't working \n \n \n ---------\nExamples: \n !play "
                       "https://www.youtube.com/watch?v=nU21rCWkuJw (plays audio from link) \n !add "
                       "https://www.youtube.com/watch?v=nU21rCWkuJw (adds url to queue, will not play song) \n "
                       "!search wowaka (returns top result) \n !search wowaka 3 (returns fourth result from youtube) "
                       "\n !diceroll 2 (rolls two dice, meaning it picks a random number from 2 to 12)```")
        await ctx.send("New feature 4/5/2022: !switch function added, which will play the url you put into it then whatever was currently playing goes to the top of the song queue")

    @commands.command()
    async def problemshelp(self, ctx):
        await ctx.send(
            "```Help: \n 'My song isn't playing!' \n -Wait at least a minute \n -Make sure you typed the command correctly \n -The bot can't play age restricted videos, so double check this \n -Google/YouTube could be denying the bot access (http error 403) so try again, it'll work eventually \n 'Audio sounds distorted or randomly speeds up' \n -Yeah that's not my fault, that's discord or your internet connection \n '!repeat or !previous doesn't work as it's supposed to' \n -Something is wrong with the lists storing the urls probably. Just try again. \n 'My question isn't answered here!' \n -Good luck```")

    @commands.command()
    async def codegeasswatchorder(self, ctx):
        await ctx.send("```Main Canon: Season 1 -> R2 \nAlternate Canon: Koudou -> Handou -> Oudou -> Fukkatsu```")

    @commands.command()
    async def fatefranchisewatchorder(self, ctx):
        await ctx.send(file=discord.File('fatewatchorder.jpg'))
        await ctx.send("<" + "https://www.youtube.com/watch?v=wnVwcUhxt1k" + ">")

    @commands.command()
    async def coinflip(self, ctx):
        result = random.randint(0, 1)
        if (result == 0):
            await ctx.send('Heads')
        elif (result == 1):
            await ctx.send('Tails')
        else:
            await ctx.send('Error')

    @commands.command()
    async def diceroll(self, ctx, arg):
        numOfDice = int(arg)
        if numOfDice == 1:
            roll = random.randint(1, 6)
        elif numOfDice == 2:
            roll = random.randint(2, 12)
        else:
            await ctx.send("You can only roll two dice")
        result = "You rolled a " + str(roll)
        await ctx.send(result)

    @commands.command()
    async def checkmate(self, ctx):
        await ctx.send(file=discord.File("tl.jpg"))

    @commands.command()
    async def repeatword(self, ctx, string):
        await ctx.send(string)