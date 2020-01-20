from random import choice

from telegram import ReplyKeyboardMarkup

import config

def get_keyboard():
  my_keyboard = ReplyKeyboardMarkup([['Прислать вопрос!']],resize_keyboard=True)
  return my_keyboard

def get_question():
  question = choice(list(config.questions))
  return question