# IPND Stage 2 Final Project
import sys
import time
# You've built a Mad-Libs game with some help from Sean.
# Now you'll work on your own game to practice your skills and demonstrate what you've learned.

# For this project, you'll be building a Fill-in-the-Blanks quiz.
# Your quiz will prompt a user with a paragraph containing several blanks.
# The user should then be asked to fill in each blank appropriately to complete the paragraph.
# This can be used as a study tool to help you remember important vocabulary!

# Note: Your game will have to accept user input so, like the Mad Libs generator,
# you won't be able to run it using Sublime's `Build` feature.
# Instead you'll need to run the program in Terminal or IDLE.
# Refer to Work Session 5 if you need a refresher on how to do this.

# To help you get started, we've provided a sample paragraph that you can use when testing your code.
# Your game should consist of 3 or more levels, so you should add your own paragraphs as well!

easy_question = '''River ___1___ is the longest river in the world. Mount ___2___ is the highest mountain,
which 29035 feet above the sea level. And largest sea is ___3___ Sea, largest lake is ___4___ Sea.'''
 
easy_answer = ['Nile', 'Everest', 'Mediterranean', 'Caspian']
 
normal_question = '''When we solve a programming question. First we should understand ___1___, like what is ___1___,
and how to represent it. Second, we think about what is ___2___. Third, let's solve the problem. 
We need workout some ___3___ first. So we can see how this program actually work. Forth, comparing
to human, computer like ___4___ simple way. So we should try ___4___ simple solution. Last, we should
develop ___5___ step by step. Which means we need write a bit then test a bit.'''
 
normal_answer = ['inputs','outputs','examples','mechnical','incrementally']

hard_question = '''___1___ ___2___ was considered to be the father of computing after his invention of the ___3___ Engine
in 1837.The ___3___ Engine contained an ALU, basic flow control, and integrated memory. However,
the father of Computer is ___4___ ___5____ with his development of Z1, Z2, Z3, and Z4.'''
hard_answer =  ['Charles', 'Babbage', 'Analytical', 'Konrad', 'Zuse']
 
insane_question = "wa'-wa' equal ___1___"
insane_answer =["cha'"]

questions = {
	'easy': easy_question,
	'normal': normal_question,
	'hard': hard_question,
	'insane': insane_question
}

answers = {
	'easy': easy_answer,
	'normal': normal_answer,
	'hard': hard_answer,
	'insane': insane_answer
}

rewards = {
	'easy': 1000,
	'normal': 2000,
	'hard': 5000,
	'insane': 10000
}

# Hint: It might help to think about how this project relates to the Mad Libs generator you built with Sean.
# In the Mad Libs generator, you take a paragraph and replace all instances of NOUN and VERB.
# How can you adapt that design to work with numbered blanks?

# If you need help, you can sign up for a 1 on 1 coaching appointment: https://calendly.com/ipnd-1-1/20min/


def find_blank(question):
	"""Input a string of question, find blank in it. Out put blank string."""
	max_blank_number = 6
	for i in range(1,max_blank_number):
		blank = '___'+str(i)+'___'
		if question.find(blank) > -1:
			return blank
	return None

def want_more():
	while True:
		keep_on = raw_input('Do you want try more level ? y/n: ')
 		if keep_on.lower() in ['yes','y']:
 			return 1
 		elif keep_on.lower() in ['no','n']:
 			return 0
 		else:
 			print "Can't read! Please input yes or no.\n" 


def level_change(keep_on,level):
	if keep_on == 0:
		return None
	else:
		if level == 'easy':
			return 'normal'
		elif level == 'normal':
			return 'hard'
		elif level == 'hard':
			return 'insane'
		else:
			print "You already come to highest level."
			print "So there is no more question for you."
			time.sleep(5)
			return 'level_end'

def start_game():
	print "\nWelcome to Who Wants to Be a Pythonaire !!!\nYou can try to answer all the question or just from one hard level."
	print "You will get correspond rewards after this game, according to your result."
	print "But if you are fail between this game you can get nothing.\n"
	print "Please select a game difficulty."
	level = raw_input('You can choose easy, normal, hard, or insane.\n')
	while True:
		if level.lower() in ['easy','normal','hard','insane']:
			return level.lower()
		else:
			print "\n%s is not an option!"%(level)
			level = raw_input("Please type a game difficulty among easy, normal, hard, and insane.\n")


def end_game(reward):
	print "\n\nYou WIN!!!"
	print "Let's the first beauty in Python Kingdom give you reward and her lovely kiss!!!"
	time.sleep(5)
	print "Muahhhhhhhhhhhh!"
	time.sleep(5)
	print "and this is your reward"
	time.sleep(3)
	print "-------------------------------"
	print "|     pythin kindom bank       |"
	print "|     	%d dollors          |"%(reward)
	print "--------------------------------"

def reward_calculate(question_number,reward):
	return question_number*reward


def engine(question,answer):
	replacement = find_blank(question)
	chance = 3
	while replacement:
		print '\n'+question + '\n'
		for i in range(1,chance+1):
			user_input = raw_input('What should be blank '+replacement + '? ')
			if answer[int(replacement[3])-1].lower() == user_input.lower():
 				question = question.replace(replacement,answer[int(replacement[3])-1])
 				print "Great! Correct!"
 				break
 			else:
 				if i < chance:
 					print user_input + " is not right answer. Please try again."
 					print "You still have " + str(chance-i) +" chance.\n"
 				else:
 					print "You fail. Gave Over!"
 					sys.exit(0)

 		replacement = find_blank(question)
 	print "\nYou win this level!!! \n"
 	return want_more()



# print find_blank(sample)
def main(questions,answers,rewards):
	# 1. Read level strings
	# 2. Pop questions, and determine question type
	# 3. Find blank, read answer
	# 4. Display whole with the words you filled in
	# level;
 # 	find question Display
 # 	fill question
 	total_reward = 0;
 	level = start_game()
 	while level and level != 'level_end':
 		question = questions[level]
 		answer = answers[level]
 		reward = rewards[level]
 		print "This %s level."%level
 		print "\nFor %s level, you get %d dollors from each question.\nIf you don't fail in the level."%(level,reward)

 		keep_on = engine(question,answer)
 		total_reward += reward_calculate(len(answer),reward)
 		level = level_change(keep_on,level)
 	end_game(reward)

