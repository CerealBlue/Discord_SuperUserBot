import praw
from sys import exit
from time import sleep
from random import randrange
from subprocess import run
from os import remove

flag = 0

def stealData(post):
	try:
		data = (post.preview['images'])
	except:
		print("Restart")
		mt_b_start()
	
	try:
		urlSteal = data[0]['source']['url']
	except:
		print("Restart")
		mt_b_start()

	print ("Stealing of data hath Begun")

	fileObj = open("MemeTaker_Bot/Number.txt",'r')
	number = int(fileObj.read())
	fileObj.close()
	remove("MemeTaker_Bot/Number.txt")

	run(['wget', '-O', 'Meme'+str(number)+'.jpeg', str(urlSteal)])
	run(['mv', 'Meme'+str(number)+'.jpeg', 'MemeTaker_Bot/Memes'])
	number += 1

	fileObj2 = open("MemeTaker_Bot/Number.txt", 'w')
	fileObj2.write(str(number))
	fileObj2.close()

	return



def mt_b_start():
	print ("MT_B Start")

	"""bot ={}{}{}{}"""

	lineBuffer = []
	ids = []

	with open("MemeTaker_Bot/ListOfIds.txt", "r") as fileObj:
		for line in fileObj:
			for i in range(0,len(line),1):
				if (line[i:i+2] == '\n'):
					break
				lineBuffer.append(line[i])
			lineBuffer = ''.join(lineBuffer)
			ids.append(lineBuffer)
			lineBuffer = []
	fileObj.close()

	subRs = ['BikiniBottomTwitter','dank_meme','indianpeoplefacebook','memes']				



	deltacon4 = randrange(4)

	overallcount = 0
	count = 0
	for post in bot.subreddit(subRs[deltacon4]).hot():
		count += 1
		sleep(1)

		if (count == 20):
			count = 0
			if (overallcount == 1):
				sys.exit()

			overallcount += 1

			if (deltacon4 == 0):
				deltacon4 += 1
			else:
				deltacon4 -= 1

		if (post.id in ids):
			continue
		else:
			fileObj2 = open("MemeTaker_Bot/ListOfIds.txt", "a")
			fileObj2.write(str(post.id)+"\n")
			fileObj2.close()
			stealData(post)
			return

