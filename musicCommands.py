import discord
from discord.ext import commands
import youtube_dl
from youtube_dl import YoutubeDL
import urllib.request
import re
import random
from musicFunctions import songQueue, previouslyPlayed, currentlyPlaying, moveURL, moveURLback, playQueue, printLists

FFMPEG_OPTIONS = {
    'before_options':
        '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
    'options': '-vn'
}
YDL_OPTIONS = {'format': 'bestaudio', 'ignoreerrors': True}

isLooping = False

class musicCommands(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def getinthevcshinji(self, ctx):
        if ctx.author.voice is None:
            await ctx.send("You are (not) in a voice channel")
        voice_channel = ctx.author.voice.channel
        if ctx.voice_client is None:
            await voice_channel.connect()
        else:
            await ctx.voice_client.move_to(voice_channel)

    @commands.command()
    async def quit(self, ctx):
        await ctx.voice_client.disconnect()

#'-nostdin' <- don't know what this is

    @commands.command()
    async def play(self, ctx, url):
        ctx.voice_client.stop()
        vc = ctx.voice_client
        if (len(currentlyPlaying) >= 1):
            previouslyPlayed.append(currentlyPlaying[0])
            currentlyPlaying.clear()
            currentlyPlaying.append(url)
            printLists()
            with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
                info = ydl.extract_info(currentlyPlaying[0], download=False)
                url2 = info['formats'][0]['url']
                source = await discord.FFmpegOpusAudio.from_probe(
                    url2, **FFMPEG_OPTIONS)
                vc.play(source, after=lambda e: playQueue(ctx))
        else:
            currentlyPlaying.append(url)
            printLists()
            with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
                info = ydl.extract_info(currentlyPlaying[0], download=False)
                url2 = info['formats'][0]['url']
                source = await discord.FFmpegOpusAudio.from_probe(
                    url2, **FFMPEG_OPTIONS)
                vc.play(source, after=lambda e: playQueue(ctx))

    @commands.command()
    async def add(self, ctx, url):
        songQueue.append(url)
        await ctx.send("Song added to queue")
        print("Song Queue: ", songQueue)

    @commands.command()
    async def skip(self, ctx):
        vc = ctx.voice_client
        if not currentlyPlaying:
            playQueue(ctx)
        if songQueue:
            ctx.voice_client.stop()
            #moveURL()
            with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
                info = ydl.extract_info(currentlyPlaying[0], download=False)
                url2 = info['formats'][0]['url']
                source = await discord.FFmpegOpusAudio.from_probe(
                    url2, **FFMPEG_OPTIONS)
                vc.play(source, after=lambda e: playQueue(ctx))
        else:
            await ctx.send("There is nothing right now in the queue")

    @commands.command()
    async def restart(self, ctx):
        ctx.voice_client.stop()
        vc = ctx.voice_client
        moveURLback()
        printLists()
        with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(currentlyPlaying[0], download=False)
            url2 = info['formats'][0]['url']
            source = await discord.FFmpegOpusAudio.from_probe(
                url2, **FFMPEG_OPTIONS)
            vc.play(source, after=lambda e: playQueue(ctx))

    @commands.command()
    async def previous(self, ctx):
        ctx.voice_client.stop()
        vc = ctx.voice_client
        moveURLback()
        moveURLback()
        with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(currentlyPlaying[0], download=False)
            url2 = info['formats'][0]['url']
            source = await discord.FFmpegOpusAudio.from_probe(
                url2, **FFMPEG_OPTIONS)
            vc.play(source, after=lambda e: playQueue(ctx))

    @commands.command()
    async def loop(self, ctx, url):
        ctx.voice_client.stop()
        vc = ctx.voice_client
        isLooping = True
        if currentlyPlaying:
            previouslyPlayed.append(currentlyPlaying[0])
            currentlyPlaying.clear()
        currentlyPlaying.append(url)
        await ctx.send("Started loop")
        while (isLooping == True):
            songQueue.append(url)
            with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
                info = ydl.extract_info(currentlyPlaying[0], download=False)
                url2 = info['formats'][0]['url']
                source = await discord.FFmpegOpusAudio.from_probe(
                    url2, **FFMPEG_OPTIONS)
                vc.play(source, after=lambda e: playQueue(ctx))
            #songQueue.append(url)
            if (isLooping == False):
                if songQueue[0] == url:
                    songQueue.pop(0)
                playQueue()
                break
            continue

    @commands.command()
    async def stoploop(self, ctx):
        isLooping = False
        await ctx.send("Stopped loop")

    @commands.command()
    async def checkifloop(self, ctx):
        if isLooping == True:
            await ctx.send("Yes")
        elif isLooping == False:
            await ctx.send("No")
        else:
            await ctx.send("Error")

    @commands.command()
    async def addnext(self, ctx, url):
        songQueue.insert(0, url)
        printLists()
        await ctx.send("That song will play next")

    @commands.command()
    async def shufflequeue(self, ctx):
        random.shuffle(songQueue)
        print(songQueue)
        await ctx.send("Queue has been shuffled")

    @commands.command()
    async def pause(self, ctx):
        await ctx.voice_client.pause()
        await ctx.send("Paused")

    @commands.command()
    async def resume(self, ctx):
        await ctx.voice_client.resume()
        await ctx.send("Resumed")

    @commands.command()
    async def stop(self, ctx):
        ctx.voice_client.stop()
        previouslyPlayed.append(currentlyPlaying[0])
        currentlyPlaying.clear()
        await ctx.send("Stopped")

    @commands.command()
    async def switch(self, ctx, url):
        vc = ctx.voice_client
        if currentlyPlaying == []:
            await ctx.send("There is nothing playing to switch with!")
        else:
            ctx.voice_client.stop()
            songQueue.insert(0, currentlyPlaying[0])
            currentlyPlaying.clear()
            currentlyPlaying.append(url)
            printLists()
            moveURLback() #not sure why this is needed it moves urls forward by itself after working properly for some reason
            with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
                info = ydl.extract_info(currentlyPlaying[0], download=False)
                url2 = info['formats'][0]['url']
                source = await discord.FFmpegOpusAudio.from_probe(
                    url2, **FFMPEG_OPTIONS)
                vc.play(source, after=lambda e: playQueue(ctx))

    @commands.command()
    async def showqueue(self,ctx):
        print(len(songQueue))
        await ctx.send("There are " + str(len(songQueue)) + " links in the queue")

    @commands.command()
    async def deletenext(self, ctx):
        songQueue.pop(0)
        await ctx.send("Next song has been deleted")

    @commands.command()
    async def deletelast(self, ctx):
        songQueue.pop(-1)
        await ctx.send("Last song on queue has been deleted")

    @commands.command()
    async def clearqueue(self, ctx):
        songQueue.clear()
        print(songQueue)
        await ctx.send("Queue has been cleared.")

    @commands.command()
    async def clearprevious(self, ctx):
        previouslyPlayed.clear()
        print(previouslyPlayed)
        await ctx.send("Previously played list has been cleared")

    @commands.command()
    async def clearcurrent(self, ctx):
        currentlyPlaying.clear()
        print(currentlyPlaying)
        await ctx.send("Currently playing list has been cleared")

    @commands.command()
    async def clearalllists(self, ctx):
        songQueue.clear()
        previouslyPlayed.clear()
        currentlyPlaying.clear()
        printLists()
        await ctx.send("All lists have been cleared")

    @commands.command()
    async def printlists(self, ctx):
        printLists()
        await ctx.send("Lists have been printed in console")

    @commands.command()
    async def search(self, ctx, *args):
        #resultRank = int(args[-1])
        searchTerms = list(args)
        #searchTerms.pop(-1)
        if (searchTerms[-1].isdigit()):
            resultRank = int(searchTerms[-1])
            searchTerms.pop(-1)
        else:
            resultRank = 0
        searchQuery = '+'.join(searchTerms)
        print(searchQuery)
        html = urllib.request.urlopen(
            "https://www.youtube.com/results?search_query=" + searchQuery)
        video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
        #print(video_ids)
        videoURL = "https://www.youtube.com/watch?v=" + video_ids[resultRank]
        await ctx.send(videoURL)
        #await ctx.send("Keep searching?")

        #def check(m):
        ##return m.author == message.author and m.content.isstring()
        #return m.content == "Yes" or "No"
        #try:
        #message = await self.wait_for('message', check = check, timeout = 30.0)

        #except asyncio.TimeoutError:
        #await ctx.send("You took too long to respond")

        #if message == "Yes":
        #await ctx.send("Nice")
        #elif message == "No":
        #await ctx.send("Want to add this to the queue?")
        #else:
        #await ctx.send("I don't understand your response.")

    @commands.command()
    async def playlist(self,ctx,url):
        html = urllib.request.urlopen(url)
        video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
        video_ids = list(dict.fromkeys(video_ids))
        print(video_ids)
        i = 0
        length = len(video_ids)
        while i <= length:
            songQueue.append("https://www.youtube.com/watch?v=" + video_ids[i])
            i += 1
            if (i == length):
                break
        print(songQueue)
        await ctx.send("Playlist added to queue")