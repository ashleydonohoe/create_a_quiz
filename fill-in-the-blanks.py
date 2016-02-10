# Code Your Own Quiz

# array for blanks in question
answer_blanks = ["___1___", "___2___", "___3___", "___4___"]

# three questions based on level of difficulty
easy_question = '''A ___1___ is a name given to a value. The name goes on the left, an equals
sign in the middle, and the ___2___ on the right. While a ___1___ can only hold
a single value, ___3___ can hold many items. These items could be strings,
numbers, Boolean values, or even other ___3___. You reference values in
___3___ by referring to their ___4___.'''
medium_question = '''You can use an ___1___ statement to check whether a condition is
true. When you follow the ___1___ statement up with an ___2___ statement,
the ___2___ statement's code will run if the ___1___ statement is not true.
When you need to test whether multiple conditions are true, you can use ___3___
along with ___1___ and ___2___. These types of statements are named ___4___
statements.'''
hard_question = '''Variables can have either a ___1___  or ___2___  scope. When
a variable has a ___1___  scope, it can be accessed throughout the program.
When a variable has a ___1___  scope, it can't be accessed outside the ___3___
or block where it's declared. When the value of a ___2___
variable needs accessed outside of a ___3___, you can ___4___
its value at the end of the ___3___ . '''

# answers for the three questions
easy_answers = ["variable", "value", "arrays", "index"]
medium_answers = ["if", "else", "elif", "conditional"]
hard_answers = ["global", "local", "function", "return"]

def level_chooser(level):
	'''
	This function takes the level the user types as input.
	It compares the user input to the available levels (defaults
	to else for "hard").
    It returns the question and answers for that level as output.
	'''
	if level == "easy":
		return easy_question, easy_answers
	elif level == "medium":
		return medium_question, medium_answers
	else:
		return hard_question, hard_answers

def answer_check(user_answer, answers, answers_index):
	'''
	This function takes the user's answer, the answers for the
	chosen question, and the current index of answers as input.

	If the user's answer is the same as the one in the current 
	index in the answers array, then "Correct" is output. 
	Otherwise, "Incorrect" is output.
	'''
	if user_answer == answers[answers_index]:
		return "Correct"
	return "Incorrect"

def ask_question(question, answers, answer_blanks, blanks_index, answers_index):
	'''
	This function takes the chosen question, its answers, the answer_blanks 
	array, the current index of the answer_blanks array, and the current
	answers_index of the answers array for the chosen question as input.

	For as long as there are blanks remaining and answers remaining, 
	the user is asked what should go in the blank. The user's input is
	saved as user_answer and then the answer_check function compares
	what the user typed to the correct answer. If the answer is correct,
	the user moves on to the next question. Otherwise, the user has to
	keep trying until answer_check returns "Correct". After each correct
	guess, the question's current blank is replaced with the user's answer
	and then the blanks_index and answers_index are incremented by 1.
	Finally, the updated question with filled in correct answers appears.
	'''
	while blanks_index < len(answer_blanks):
		while answers_index < len(answer_blanks):
			user_answer = raw_input("What word goes in " + answer_blanks[blanks_index] + 
                "? ")
			while answer_check(user_answer, answers, answers_index) != "Correct":
				user_answer = raw_input("Sorry, that is not correct. What word goes in " 
                + answer_blanks[blanks_index] + "? ")
			if answer_check(user_answer, answers, answers_index) == "Correct":
				print "Congrats! " + user_answer + " is correct!"
				# when the user guesses correctly, the blanks in the question are replaced with the user's answer
				question = question.replace(answer_blanks[blanks_index], user_answer)
				# increments both indicies by 1 to go to the next blank number
				blanks_index += 1
				answers_index += 1
				print question

def play_game():
	'''
	This is the main function for game play, and it takes no inputs.

	It asks the user to type a level and checks whether the level is valid. If not,
	then the user has to try again. Once a correct level is chosen, the level is used
	as input to the level_chooser function, which outputs the question and answers 
	to use. These are saved as variables here for use.

	Then, the question is printed, the blanks_index and answers_index are initialized at 0,
	and the ask_question function is called to begin with asking the questions (the 
	answer_check function is called in ask_question for answer checking).
	
	When all blanks are filled, this function prints out a message showing
	game completion.
	'''
	level = raw_input("Choose a level: easy, medium, or hard: ")
	while level not in ["easy", "medium", "hard"]:
		level = raw_input("Sorry, that was not valid. Choose a level: easy, medium, or hard: ")
	question, answers = level_chooser(level)

	print question

	# sets the blanks_index and answers_index both to 0
	blanks_index = 0
	answers_index = 0

	ask_question(question, answers, answer_blanks, blanks_index, answers_index)

	print "You have got all the answers correct!"

# starts the game upon running this Python file
play_game()