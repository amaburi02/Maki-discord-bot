import discord
from discord.ext import commands
from discord.ui import Button, View
from musicFunctions import songQueue, previouslyPlayed, currentlyPlaying, printLists, moveURL, moveURLback, playQueue
import youtube_dl
import urllib.request
import re
import random

FFMPEG_OPTIONS = {
    'before_options':
        '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
    'options': '-vn'
}
YDL_OPTIONS = {'format': 'bestaudio', 'ignoreerrors': True}

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
        savedQueue = []
        end = 99
        i = 0

        if songQueue:
            savedQueue = songQueue.copy()
            songQueue.clear()
        if currentlyPlaying:
            previouslyPlayed.append(currentlyPlaying)
            currentlyPlaying.clear()

        songQueue.insert(0, url)
        playQueue(ctx)
        while i <= end:
            songQueue.append(url)
            i += 1

        button = Button(label="Stop", style=discord.ButtonStyle.primary)
        view = View()
        view.add_item(button)

        async def buttonCallback(interaction):
            ctx.voice_client.stop()
            for x in songQueue:
                if (x == url):
                    songQueue.remove(url)
                elif (x != url):
                    break
                else:
                    await ctx.send("Error")

        button.callback = buttonCallback

        await ctx.send("Press the button below to stop loop", view=view)
    
    @commands.command()
    async def viewqueue(self, ctx):
        i = 0
        await ctx.send("Queue:")
        for x in songQueue:
            await ctx.send("<" + songQueue[i] + ">")
            i += 1

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

        if not currentlyPlaying:
            button = Button(label = "Play now", style = discord.ButtonStyle.primary)
            view = View()
            view.add_item(button)

            async def buttonCallback(interaction):
                print(ctx.author.id)
                if interaction.user == ctx.author:
                    songQueue.insert(0, videoURL)
                    playQueue(ctx)
                    await interaction.response.send_message("Now playing")
                else:
                    await interaction.response.send_message("You were not the one that searched this.")

            button.callback = buttonCallback

            await ctx.send("It looks like you're not playing anything currently, want to play this?", view = view)
        else:
            button = Button(label = "Add to queue", style = discord.ButtonStyle.primary)
            view = View()
            view.add_item(button)

            async def buttonCallback(interaction):
                songQueue.append(videoURL)
                await interaction.response.send_message("Song added to queue")

            button.callback = buttonCallback

            await ctx.send("Want to add this to the queue?", view = view)

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