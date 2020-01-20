from telegram.ext import Updater, CommandHandler, RegexHandler, MessageHandler, Filters

from handlers import *

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