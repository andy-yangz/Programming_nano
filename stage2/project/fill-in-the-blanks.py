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
	"""Input a question string, find blank in it. Out put this blank string."""
	max_blank_number = 6
	for current_attempt in range(1,max_blank_number):
		blank = '___'+str(current_attempt)+'___'
		if question.find(blank) > -1:
			return blank
	return None

def want_more():
	'''Prompt player whether want to try higher level. Return keep_on flag 0 or 1.'''
	while True:
		keep_on = raw_input('Do you want try more level ? y/n: ')
 		if keep_on.lower() in ['yes','y']:
 			return 1
 		elif keep_on.lower() in ['no','n']:
 			return 0
 		else:
 			print "Can't read! Please input yes or no.\n" 


def level_change(keep_on,level):
	'''Input keep_on flag and current level. If player want keep on, 
	then output string of higher level. But if player already in highest 
	level, then return string of level_end'''
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
	'''Start of game. Prompt player choose hard level. Then output 
	correspond string of level.'''
	print ("\nWelcome to Who Wants to Be a Pythonaire !!!\n"
			"You can try to answer all the question or just from one hard level.")
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

def chance_decide():
	print ("\nBefore start you game\n"
			"you can decide how many times you can guess for each question.")
	while True:
		try:
			chance = int(raw_input('How many chance do you want: '))
			return chance
		except ValueError:
			print "\nInvalid input! \nPlease enter integer number."

def end_game(reward):
	'''End of game. Input rewards at end of game. Then print out ending words.'''
	print "\n\nYou WIN!!!"
	print "Let's the first beauty in Python Kingdom give you reward and her lovely kiss!!!"
	time.sleep(5)
	print "Muahhhhhhhhhhhh!"
	time.sleep(3)
	print "and this is your reward"
	time.sleep(3)
	print "-------------------------------"
	print "|     python kindom bank       |"
	print "|     	%d dollors          |"%(reward)
	print "--------------------------------"

def reward_calculate(question_number,reward):
	'''Input question number and reward level for each question for current level.
	   Output whole reward for this level.'''
	return question_number*reward


def engine(question,answer, chance):
	'''The engine of this game. Input current level question and answer. 
		Prompt question and then check answer. If fail chance times to answer
		correct answer, then exit program. If get correct all answer, it will
		prompt player whether go to higher level or not. Then return keep_on flag'''
	replacement = find_blank(question)
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
 					print "\nYou fail. Gave Over!\nPlease challenge again."
 					sys.exit(0)

 		replacement = find_blank(question)
 	print "\nYou win this level!!! \n"
 	return want_more()



def main(questions,answers,rewards):
	'''Main structure of this game. Inputs information of questions, answers,
	and rewards information for all level. Then start game, calculate rewards, 
	go through questions, and at last call end_game to print end scence.'''
 	total_reward = 0;
 	level = start_game()
 	chance = chance_decide()
 	while level and level != 'level_end':
 		question = questions[level]
 		answer = answers[level]
 		reward = rewards[level]
 		print "\nThis %s level."%level
 		print "\nFor %s level, you get %d dollors from each question."%(level,reward)
 		print "If you don't fail in the level."

 		keep_on = engine(question,answer,chance)
 		total_reward += reward_calculate(len(answer),reward)
 		level = level_change(keep_on,level)
 	end_game(total_reward)

main(questions,answers,rewards)
