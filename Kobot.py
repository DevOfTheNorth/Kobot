import os
import asyncpraw
import discord

client=discord.Client()
reddit = asyncpraw.Reddit(
    client_id="8mPH8_jF_NtZ3eXUqh7ghA",
    client_secret="oaacevipHemiUz5cTh7ixczqAk702w",
    password="Cookies123",
    user_agent="KoboldbotPycharm",
    username="Koboldbot")

@client.event
async def on_ready():
    print("we have logged in as{0.user}".format(client))



@client.event
async def on_message(message):
    if message.author==client.user:
        return
    if(message.content.startswith("kobot kobold")):
        Subreddit = reddit.subreddit("KoboldsFuckingKobolds")
        submission = Subreddit.random()
        await message.channel.send(submission.url)

    if(message.content.startswith("kobot gay")):
        Subreddit = reddit.subreddit("gayfurryporn")
        submission = Subreddit.random()
        await message.channel.send(submission.url)

client.run('ODk3NDcyNDA2MDc0MDMyMTg5.YWWKTw.Mk0F2NVXxnQwSJCYoeLNbDjUabw')


