import time
from datetime import datetime

responses = {
    'hi': 'Hello! How can I help you today?',
    'hello': 'Hi there!',
    'how are you': "I'm a program, but I'm working fine!",
    'name': 'I am TejaBot, your sample chatbot.',
    'bye': 'Goodbye! Have a nice day.'
}

def get_response(text):
    t = text.lower()
    for k in responses:
        if k in t:
            return responses[k]
    if 'time' in t:
        return 'Current time: ' + datetime.now().strftime('%H:%M:%S')
    return "Sorry, I don't understand. Try 'hi' or ask the time."

def main():
    print('Simple Chatbot (type "exit" to quit)')
    while True:
        txt = input('You: ').strip()
        if txt.lower() in ('exit','quit','bye'):
            print('Bot:', get_response('bye'))
            break
        print('Bot:', get_response(txt))

if __name__ == '__main__':
    main()
