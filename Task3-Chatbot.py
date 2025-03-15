import random
greetings = ['hello', 'hi', 'hey']
greeting_responses = ['Hello!', 'Hi there!', 'Hey!']
questions = ['how are you?', 'how is your day?', 'what are you doing?']
question_responses = ['I am doing well!', 'My day is going great!', 'I am just chatting with you.']
goodbyes = ['bye', 'goodbye', 'see you later']
goodbye_responses = ['Goodbye!', 'See you later!', 'Take care!']
def chatbot(input_string):
    for word in input_string.split():
        if word.lower() in greetings:
            return random.choice(greeting_responses)
    for word in input_string.split():
        if word.lower() in questions:
            return random.choice(question_responses)
    for word in input_string.split():
        if word.lower() in goodbyes:
            return random.choice(goodbye_responses)
    return "I'm sorry, I don't understand. Can you please rephrase that?"
while True:
    user_input = input("You: ")
    response = chatbot(user_input)
    print("Chatbot:", response)
