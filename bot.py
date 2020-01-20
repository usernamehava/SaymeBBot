from random import choice, shuffle

from telegram import ReplyKeyboardMarkup, ParseMode, ReplyKeyboardRemove

from telegram.ext import messagequeue as mq
from telegram.ext import Updater, CommandHandler, RegexHandler, MessageHandler, Filters
import config



def get_question():
  question = choice(list(config.questions))
  return question

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


def get_keyboard():
  my_keyboard = ReplyKeyboardMarkup([['Прислать вопрос!']],resize_keyboard=True)
  return my_keyboard

def dont_know(bot, update):
  user_text = f'{update.message.chat.first_name}, не присылайте мне видео, стикеры, документы, фото и лишние текстовые сообщения,<b> пожалуйста</b>.'
  update.message.reply_text(user_text, reply_markup=get_keyboard(), parse_mode=ParseMode.HTML)

def main():
  bot = Updater(config.TOKEN, request_kwargs=config.PROXY)
  dp = bot.dispatcher 
  dp.add_handler(CommandHandler("start", start))
  dp.add_handler(RegexHandler('^(Прислать вопрос!)$', get_answers,pass_user_data=True))
  dp.add_handler(MessageHandler(Filters.text,get_rating,pass_user_data=True))
  dp.add_handler(MessageHandler(Filters.video | Filters.photo | Filters.document | Filters.sticker, dont_know))
  bot.bot._msg_queue = mq.MessageQueue()
  bot.bot._is_messages_queued_default = True
  bot.start_polling()
  bot.idle()

if __name__=='__main__':
  main()