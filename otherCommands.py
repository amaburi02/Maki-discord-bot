import discord
from discord.ext import commands
import random

class otherCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def commandlist(self,ctx):
        await ctx.send("```Music Commands: "
                       "\n !join - makes bot join voice channel or switch voice channels to the one you're using "
                       "\n !quit - makes bot leave voice channel "
                       "\n !play [url] - paste youtube URL after command and it will play the audio from the video "
                       "\n !pause - pauses the music "
                       "\n !resume - resumes the music "
                       "\n !stop - stops the music "
                       "\n !add [url] - adds a song to the queue "
                       "\n !skip - plays next song in the queue "
                       "\n !previous - plays previous song "
                       "\n !restart - restarts the song "
                       "\n !switch [url] - plays your url and and puts what was already playing at the top of the song queue. "
                       "\n !showqueue - tells you how many links are in the queue"
                       "\n !addnext - will put the song in the front of the queue so it plays next "
                       "\n !deletenext - deletes the next song in the queue "
                       "\n !deletelast - deletes the last song in the queue in case you make a typo "
                       "\n !clearqueue - deletes all songs in queue "
                       "\n !shufflequeue - shuffles the queue "
                       "\n !search [searchquery] [int] - searches youtube and returns top video in results. Won't add song to queue, this function is just to save time from searching on youtube yourself. Top result starts at 0. Searching without specifying int will return top result. "
                       "\n !playlist [url] - adds an entire playlist to song queue. If you want to shuffle queue use !shuffle"
                       "\n "
                       "\nExtra Commands: "
                       "\n !fatefranchisewatchorder - pulls up watch "
                       "order for the Fate franchise "
                       "\n !coinflip - flips a coin "
                       "\n !diceroll [int 1 or 2] - rolls "
                       "one dice or 2 "
                       "\n !commandlist - pulls up this list "
                       "\n "
                       "\n "
                       "\n ---------"
                       "\nExamples: "
                       "\n !play "
                       "https://www.youtube.com/watch?v=nU21rCWkuJw (plays audio from link) "
                       "\n !add "
                       "https://www.youtube.com/watch?v=nU21rCWkuJw (adds url to queue, will not play song) "
                       "\n "
                       "!search wowaka (returns top result) "
                       "\n !search wowaka 3 (returns fourth result from youtube) "
                       "\n !diceroll 2 (rolls two dice, meaning it picks a random number from 2 to 12)```")

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