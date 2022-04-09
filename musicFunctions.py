import discord
import youtube_dl

FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
YDL_OPTIONS = {'format': 'bestaudio', 'ignoreerrors': True}

songQueue = []
previouslyPlayed = []
currentlyPlaying = []


def printLists():
    print("Previously Played: ", previouslyPlayed)
    print("Currently Playing: ", currentlyPlaying)
    print("Song Queue: ", songQueue)


def moveURL():
    if currentlyPlaying:
        previouslyPlayed.append(currentlyPlaying[0])
        currentlyPlaying.clear()
    if songQueue:
        currentlyPlaying.append(songQueue[0])
        songQueue.pop(0)
    printLists()


def moveURLback():
    if currentlyPlaying:
        songQueue.insert(0, currentlyPlaying[0])
        currentlyPlaying.clear()
    if previouslyPlayed:
        currentlyPlaying.append(previouslyPlayed[-1])
        previouslyPlayed.pop(-1)
    printLists()


def playQueue(ctx):
    vc = ctx.voice_client
    ctx.voice_client.stop()
    with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
        moveURL()
        info = ydl.extract_info(currentlyPlaying[0], download=False)
        url2 = info['formats'][0]['url']
        source = discord.FFmpegOpusAudio(url2, **FFMPEG_OPTIONS)
        vc.play(source, after=lambda e: playQueue(ctx))