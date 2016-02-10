'''
input = None
while input != "yes":
	input = raw_input("Please type 'yes': ")
print "YOU said 'yes'!"
'''


# Code Your Own Quiz 

# array for blanks in question
answer_blanks = ["___1___", "___2___", "___3___", "___4___"]

# three questions based on level of difficulty
easy_question = '''A ___1___ is a name given to a value. The name goes on the left, an equals sign in the middle, and the ___2___ on the right. While a ___1___ can only hold a single value, ___3___ can hold many items. These items could be strings, numbers, Boolean values, or even other ___3___. You reference values in ___3___ by referring to their ___4___.'''
medium_question = '''You can use an ___1___ statement to check whether a condition is true. When you follow the ___1___ statement up with an ___2___ statement, the ___2___ statement's code will run if the ___1___ statement is not true. When you need to test whether multiple conditions are true, you can use ___3___ along with ___1___ and ___2___. These types of statements are named ___4___ statements.'''
hard_question = '''Variables can have either a ___1___  or ___2___  scope. When a variable has a ___1___  scope, it can be accessed throughout the program. When a variable has a ___1___  scope, it can't be accessed outside the ___3___ or block where it's declared. When the value of a ___2___ variable needs accessed outside of a ___3___, you can ___4___  its value at the end of the ___3___ . '''

# answers for the three questions
easy_answers = ["variable", "value", "arrays", "index"]
medium_answers = ["if", "else", "elif", "conditional"]
hard_answers = ["global", "local", "function", "return"]

# Takes the level chosen as input and returns the prompt for the level the user chooses
def level_chooser(level):
	level = raw_input("Choose a level: easy, medium, or hard: ")
	if level == "easy":
		return easy_question
	elif level == "medium":
		return medium_question
	else:
		return hard_question

# Takes the question for the level as input and outputs the answers to use
def get_answers(question):
	if question == easy_question:
		return easy_answers
	elif question == medium_question:
		return medium_answers
	else:
		return hard_answers

# Takes in the user's answer, the answers to the chosen question, and the index of the answers the user is on. Determines if the user's answer matches the value in the index of the answers for that question
def answer_check(user_answer, answers, answers_index):
	if user_answer == answers[answers_index]:
		return "Correct"
	return "Incorrect"

def ask_question(question, answers, answer_blanks, blanks_index, answers_index):
	# Loops through all the blanks and answers. Grabs the user's answer for the current blank and uses the answer as input for answer_check. If the user doesn't guess correctly, then they will be prompted until they do.
	while blanks_index < len(answer_blanks):
		while answers_index < len(answer_blanks):
			user_answer = raw_input("What word goes in " + answer_blanks[blanks_index] + "? ")
			while answer_check(user_answer, answers, answers_index) != "Correct":
				user_answer = raw_input("Sorry, that is not correct. What word goes in " + answer_blanks[blanks_index] + "? ")
			if answer_check(user_answer, answers, answers_index) == "Correct":
				print "Congrats! " + user_answer + " is correct!"
				# when the user guesses correctly, the blanks in the question are replaced with the user's answer
				question = question.replace(answer_blanks[blanks_index], user_answer)
				# increments both indicies by 1 to go to the next blank number
				blanks_index += 1
				answers_index += 1
				print question

# Main function for game play
def play_game():
	# grabs user input for level and grabs prompt from the level_chooser function	
	level = raw_input("Choose a level: easy, medium, or hard: ")
	while level != "easy":
		print "You didn't choose easy!"
		level = raw_input("Choose a level: easy, medium, or hard: ")


	question = level_chooser(level)

	print question

	# stores returned answers from get_answers
	answers = get_answers(question)

	# sets the blanks_index and answers_index both to 0
	blanks_index = 0
	answers_index = 0

	# Asks the user the question until all blanks are filled. It takes the question, answers, the answer blanks, and both indices as input 
	ask_question(question, answers, answer_blanks, blanks_index, answers_index)

	print "You have got all the answers correct!"

# starts the game upon running this Python file
play_game()




