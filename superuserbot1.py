"""import discord


client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)"""

#2018-04-13 11:23:13

from discord.ext.commands import Bot
from discord import Game
from datetime import datetime
import sys
import asyncio

sys.path.append("/home/sudheendra_raghav/Desktop/Discord/SuperUserBot/MemeTaker_Bot/")

from mt_b import mt_b_start as memesteal


BOT_PREFIX = ("?", "!", "++")


client = Bot(command_prefix=BOT_PREFIX)

@client.command(name='sup',
		aliases=['hey','heyoo','hello'],
		pass_context = True)
async def greet(context):
	await client.say("Sup boy kid"+", "+context.message.author.mention)

@client.command(name='time', aliases=['date','weather','day'])
async def timeDisplay():
	await client.say("The date is:\t"+str(datetime.now()))


@client.async_event
async def on_message(message):
	chan = message.channel
	if message.content.startswith('Bot'):
		await client.send_message(message.channel, "hi")
	if message.content.startswith('SendMeme'):
		await client.send_message(message.channel, "Wait for a couple of secondz. Pls.\n\nFetching only the best may-mays from:\nReddit!")
		memesteal()

		numberFile = open("MemeTaker_Bot/Number.txt", "r")
		number = int(numberFile.read())
		numberFile.close()

		with open('MemeTaker_Bot/Memes/Meme'+str(number-1)+'.jpeg', 'rb') as f:
			await client.send_file(message.channel, f)
		await client.send_message(message.channel, "Okay?")
	await client.process_commands(message)

@client.event
async def on_ready():
	await client.change_presence(game=Game(name="with my creator"))
	print ("Logged in as " + client.user.name)




client.run(TOKEN)









