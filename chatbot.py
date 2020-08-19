import random

greetings = ['hello', 'hola', 'hi', 'Hi', 'hey!','hey']
random_greeting = random.choice(greetings)

question = ['How are you?','How are you doing?']
responses = ['Okay',"I'm fine"]
random_response = random.choice(responses)

question = ['good Morning','good night']
responses = ['You 2.',"Thank's. You 2"]
random_response = random.choice(responses)

question = ['bored','tired']
responses = ['You will be Okay',"You'll be fine"]
random_response = random.choice(responses)

question = ['quotes','quote']
responses = ['Change your thoughts and you change your world. Norman Vincent Peale',"Keep your eyes on the stars and your feet on the ground. Theodore Roosevelt", 'Keep looking up… that’s the secret of life. Snoopy',"Non-ownership is not about having nothing, It means you don't have anything unnecessary. bubjung", "Live brightly, confidently, and actively. Jihwan Ahn(developer of this program XD)" ]
random_response = random.choice(responses)


while True:
	userInput = input("SaJa@ ")
	if userInput in greetings:
		print(random_greeting)
	elif userInput in question:
		print(random_response)
	else:
		print("I need a code surgery. Please fix me by editing my python code.")