# IPND Stage 2 Final Project
import sys
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
 
easy_answer = ['Nile', 'Everest', 'Mediterrannean', 'Caspian']
 
normal_question = '''When we solve a programming question. First we should understand ___1___, like what is ___1___,
and how to represent it. Second, we think about what is ___2___. Third, let's solve the problem. 
We need workout some ___3___ first. So we can see how this program actually work. Forth, comparing
to human, computer like ___4___ simple way. So we should try ___4___ simple solution. Last, we should
develop ___5___ step by step. Which means we need write a bit then test a bit.'''
 
normal_answer = ['inputs','outputs','examples','mechnical','incrementally']

hard_question = '''___1___ ___2___was considered to be the father of computing after his invention of the ___3___ Engine
in 1837.The ___3___ Engine contained an ALU, basic flow control, and integrated memory. However,
the father of Computer is ___4___ ___5____ with his development of Z1, Z2, Z3, and Z4.'''
hard_answer =  ['Charles Babbage', 'Analytical', 'Konrad Zuse']
 
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
# sample = '''A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
# adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
# don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
# tuple, and ___4___ or can be more complicated such as objects and lambda functions.'''
# 
# sample_answer = ['function','parameter','None','list']
# The answer for ___1___ is 'function'. Can you figure out the others?

# We've also given you a file called fill-in-the-blanks.pyc which is a working version of the project.
# A .pyc file is a Python file that has been translated into "byte code".
# This means the code will run the same as the original .py file, but when you open it
# it won't look like Python code! But you can run it just like a regular Python file
# to see how your code should behave.

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
			return 'level_end'

def start_game():
	print "Welcome to Who Wants to Be a Millionaire Please select a game difficulty."
	hard_level = raw_input('You can choose easy, normal, hard, and insane.\n')
	print "You WIN!!!"

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
 	print "You win this level!!! \n"
 	return want_more()



# print find_blank(sample)
def main(questions,answers):
	# 1. Read level strings
	# 2. Pop questions, and determine question type
	# 3. Find blank, read answer
	# 4. Display whole with the words you filled in
	# level;
 # 	find question Display
 # 	fill question
 	level = start_game()
 	while level and level != 'level_end':
 		question = level_choose(level)
 		answer = answers(level)
 		keep_on = engine(question,answer)
 		level = level_change(keep_on,level)
 	end_game()


# Engine test
# engine(easy_question,easy_answer)

print questions['easy']
print questions['normal']
print questions['hard']
print answers['easy']
