#2018-04-13 11:23:13

from discord.ext.commands import Bot
from discord import Game
import datetime
import sys
import asyncio
import random

#sys.path.append("/home/CerealBlue/Desktop/Discord/SuperUserBot/MemeTaker_Bot/")

#from mt_b import mt_b_start as memesteal

TOKEN = "NDM0MDI3NzE2Nzk1NDMyOTYx.DcTOsQ.yxwiSAePR3u_wlXgh_pt9SuW6_o"

BOT_PREFIX = ("?", "!", "++")

client = Bot(command_prefix=BOT_PREFIX)

@client.command(name='greetings',
                description="This command makes SuperUserBot greet you.",
                brief="Bot Greets",
		aliases=['hey','hi','hello', 'sup', 'wassup'],
		pass_context = True)
async def greet(context):
    greeters = [
        "Wassup,",
        "Salutations",
        "Hello from the Cloud!",
        "Hello! I stay in a Raspberry Pi! It's doesn't taste like a Pie though :( ...",
        "My Creator (The great BlueCereal) has taught me to greet people (I'm anti-social, btw). Here goes... ~~Gretings~~ ~~Greatthings~~ \n\nGreetings,"]
    await client.say(random.choice(greeters) + " " + context.message.author.mention + ".")

@client.command(name='time',
                description=
                "This command displays the date and time in:"
                "\n\t>YYYY-MM-DD HH:MM:SS:MS"
                "\n\t>Current Year"
                "\n\t>Current Month"
                "\n\t>WeekNumber"
                "\n\t>WeekdayNumber"
                "\n\t>Day of the Year"
                "\n\t>Day of the Month"
                "\n\t>Day of the Week"
                "\n\nAlso, why are you this lazy to not look at your phone's time?",
                brief="Time Displayer",
                aliases=['date', 'day'])
async def timeDisplay():
	await client.say("Time:\n"
                    "```"+str(datetime.datetime.now())+"```\n"
                    "Current year: \t`" +     str(datetime.date.today().strftime("%Y")) + "`\n"
                    "Current Month: \t`" +    str(datetime.date.today().strftime("%B")) + "`\n"
                    "WeekNumber \t`" +        str(datetime.date.today().strftime("%W")) + "`\n"
                    "WeekdayNumber: \t`" +    str(datetime.date.today().strftime("%w")) + "`\n"
                    "Day of the Year: \t`" +  str(datetime.date.today().strftime("%j")) + "`\n"
                    "Day of the Month: \t`" + str(datetime.date.today().strftime("%d")) + "`\n"
                    "Day of the Week: \t`" +  str(datetime.date.today().strftime("%A")) + "`\n"
                    )

@client.async_event
async def on_message(message):
	chan = message.channel
	if message.content.startswith('Bot'):
		await client.send_message(message.channel, "hi")
	"""if message.content.startswith('SendMeme'):
		await client.send_message(message.channel, "Wait for a couple of secondz. Pls.\n\nFetching only the best may-mays from:\nReddit!")
		memesteal()

		numberFile = open("MemeTaker_Bot/Number.txt", "r")
		number = int(numberFile.read())
		numberFile.close()

		with open('MemeTaker_Bot/Memes/Meme'+str(number-1)+'.jpeg', 'rb') as f:
			await client.send_file(message.channel, f)
		await client.send_message(message.channel, "Okay?")"""
	await client.process_commands(message)

@client.event
async def on_ready():
	await client.change_presence(game=Game(name="with my creator"))
	print ("Logged in as " + client.user.name)




client.run(TOKEN)
