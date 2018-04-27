#2018-04-13 11:23:13

from discord.ext.commands import Bot
from discord import Game
import datetime
import sys
import asyncio
import random
import praw

#sys.path.append("/home/CerealBlue/Desktop/Discord/SuperUserBot/MemeTaker_Bot/")

#from mt_b import mt_b_start as memesteal



BOT_PREFIX = ("?", "!", "++")

client = Bot(command_prefix=BOT_PREFIX)

class Lists:
	def __init__(self):
		self.idList = []
	
	def addId(self, Id):
		self.idList.append(Id)
	
	def IdList(self, Id):
		if Id in idList:
			return 1
		return 0

class serversData:
	def __init__(self):
		self.servo = {	'Num' : ["CSE", 0],
				'Num' : ["MeMyself&I", 0]
				}
		self.me = 'Num'

	def myId(self):
		return self.me

	def isMe(self, testId):
		if (self.me == testId):
			return True
		return False

	def addCall(self, serverId):
		self.servo[serverId][1] += 1

	def thisCall(self, serverId):
		return self.servo[serverId][1]

	def returnServerInfo(self):
		lis = []
		lis.append( str( "```Bot Calls From Servers```" ) )
		for i in self.servo:
			lis.append( str( "`  "+str(self.servo[i][0])+"  `:\t" ) )
			lis.append( str( "`  "+str(self.servo[i][1])+"  `" ) )
			lis.append("\n")
		lis = ''.join(lis)
		return (lis)




suBot = serversData()


@client.command(name='greetings',
                description="This command makes SuperUserBot greet you.",
                brief="Bot Greets",
		aliases=['hey','hi','hello', 'sup', 'wassup'],
		pass_context = True)
async def greet(context):
	suBot.addCall(context.message.server.id)	
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
                aliases=['date', 'day'],
		pass_context=True)
async def timeDisplay():
	suBot.addCall(context.message.server.id)
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

@client.command(name='joke',
                description="Do you want a joke? Well get ready for these jokes!\n\nType Specifiers: <none> <dark>\n\nExample:\n!joke\t!joke dark",
                brief="Joke Sender",
		pass_context = True)
async def joke(context):
	suBot.addCall(context.message.server.id)
	msg = context.message.content
	subR = "jokes"
	if "dark" in msg:
		await client.say("Dark joke, huh? Let's do it") 
		subR = "darkjokes"
	else:
		await client.say("Wait for one sec")


@client.command(name='callsMade',
		description='Bot Creator Only',
		brief='Bot Creator Only',
		pass_context=True)
async def callsMade(context):
	suBot.addCall(context.message.server.id)
	
	if (suBot.isMe(context.message.author.id)):
		pingedServ = client.get_server(context.message.server.id)
		me = pingedServ.get_member(suBot.myId())
		senderMsg = suBot.returnServerInfo()
		await client.send_message(me, senderMsg)
		
		
	else: 
		print ("no")



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
