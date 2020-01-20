from random import  shuffle

from telegram import  ParseMode

from telegram.ext import messagequeue as mq

from utils import * 

@mq.queuedmessage
def get_answers(bot,update, user_data):
  question = get_question()
  global answers 
  answers = config.questions[question]
  rnd = answers.copy()
  shuffle(rnd)
  reply_keyboard = [['{}'.format(rnd[0])],['{}'.format(rnd[1])],['{}'.format(rnd[2])],['{}'.format(rnd[3])]]
  update.message.reply_text(question,reply_markup=ReplyKeyboardMarkup(reply_keyboard,one_time_keyboard=True))
  
  
def get_rating(bot, update,user_data):
  if answers[0] == update.message.text:
    user_text = """
    <b>Верно!</b>"""
    update.message.reply_text(user_text,reply_markup=get_keyboard(),parse_mode=ParseMode.HTML)                             
  else:
    user_text = f"""
  <b>Неверно!
  
Правильный ответ:</b> {answers[0]}"""
    update.message.reply_text(user_text,reply_markup=get_keyboard(),parse_mode=ParseMode.HTML)


def start(bot, update): 
  msg = '<b>{}</b>, вы запустили данного бота. Я (то есть бот) буду присылать вам вопросы, а вы должны постараться правильно на них ответить. Удачи!'.format(update.message.chat.first_name)  
  update.message.reply_text(msg,reply_markup=get_keyboard(), parse_mode=ParseMode.HTML)

def dont_know(bot, update):
  user_text = f'{update.message.chat.first_name}, не присылайте мне видео, стикеры, документы, фото и лишние текстовые сообщения,<b> пожалуйста</b>.'
  update.message.reply_text(user_text, reply_markup=get_keyboard(), parse_mode=ParseMode.HTML)
