import discord
import os
import discord.ext
from keep_alive import keep_alive
from discord.ext import commands
client = discord.Client()

client = commands.Bot(command_prefix = '%')
async def on_ready():
    print("bot online") #will print bot online when booted up
    
@client.command()
async def ping(co):
    await co.send("pong")

bad_words = []#insert words and phrases word by word with maximum detectable phrase size of 3 adjacent words in this list e.g ["this", "is", "a", "phrase"]

good_words = []#insert words and phrases word by word with maximum detectable phrase size of 3 adjacent words in this list


@client.event
async def on_message(message):
  msgcontent = message.content.lower()
  msgcontentSet = set(msgcontent.split())
  msgcontentList = list(msgcontent.split())
  good = set(good_words)
  goodList = list(good)
  bad = set(bad_words)
  badList = list(bad)
  badFlag = False #flag to prioritise bad over good
  if message.author.id == client.user.id:
    return

#bad words
  if len(msgcontentSet.intersection(bad)) > 1:
      #if iterator not at end of the list (no i+1)
      for i in range(len(msgcontentList)-1):
        if i < len(msgcontentList):
          nB = badList.index(msgcontentList[i]) +1
          compareB = badList.index(msgcontentList[i+1]) +1
          if (compareB - nB) < 3:
            #consider them as one phrase
            await message.channel.send(file=discord.File(''))#optionally send an image
            await message.send("") #enter a message to be displayed when bad words/phrases are said
            badFlag = True
             #randomise
  if len(msgcontentSet.intersection(bad)) == 1:
    await message.channel.send(file=discord.File('mqdefault.jpg'))
    badFlag = True

#good words
  if len(msgcontentSet.intersection(good)) > 1:
    for i in range(len(msgcontentList)-1):
      if i < len(msgcontentList):
        nG = goodList.index(msgcontentList[i]) +1
        compareG = goodList.index(msgcontentList[i+1]) +1
        if (compareG - nG) < 3:
          if badFlag is False:
            await message.channel.send(file=discord.File(''))#optionally send an image
            await message.send("") #enter a message to be displayed when bad words/phrases are said
  if len(msgcontentSet.intersection(good)) == 1:
    if badFlag is False:
      await message.channel.send(file=discord.File('cover10.jpg'))

keep_alive()

client.run(os.getenv("TOKEN"))
my_secret = os.environ['TOKEN']
