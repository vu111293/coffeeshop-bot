from flask import Flask
from flask_assistant import Assistant, ask, tell, event
import os
import logging

os.environ['DEV_ACCESS_TOKEN'] = 'd0d6b88518c640f6916a9eafe90598c8'
os.environ['CLIENT_ACCESS_TOKEN'] = 'a2fdbd74d6324856a27811608993a3ee'

# export DEV_ACCESS_TOKEN='d0d6b88518c640f6916a9eafe90598c8'
# export CLIENT_ACCESS_TOKEN='a2fdbd74d6324856a27811608993a3ee'

app = Flask(__name__)
assist = Assistant(app, route='/')
logging.getLogger('flask_assistant').setLevel(logging.DEBUG)

app.config['ASSIST_ACTIONS_ON_GOOGLE'] = True


@assist.action('greeting')
def greet_and_start():
    speech = "Hey! Are you male or female?"
    return ask(speech)


@assist.action("give-gender")
def ask_for_color(gender):
    if gender == 'male':
        gender_msg = 'Sup bro!'
    else:
        gender_msg = 'Haay gurl!'

    speech = gender_msg + ' What is your favorite color?'
    return ask(speech)


@assist.action('give-color', mapping={'color': 'sys.color'})
def ask_for_season(color):
    speech = 'Ok, {} is an okay color I guess'.format(color)
    return ask(speech)


@assist.action('purchase')
def purchase_action(payment, a, b):
    # return ask('Nice to meet u ' + str(a) + str(b))
    return event('boom_event')


@assist.action('boom')
def boom_action():
    return ask('Boom is called')


@assist.action('ShowCard')
def show_card():
    resp = ask("Here's an example of a card")
    resp.card(text='The text to display',
              title='Card Title',
              img_url='http://example.com/image.png'
              )

    return resp


@assist.action('ask_name')
def ask_name_action(name):
    return ask('Hi ' + str(name) + '. Nice to meet you!')


@assist.action('Default Welcome Intent')
def welcome():
    return event('ask_name')


if __name__ == '__main__':
    app.run(debug=True)
