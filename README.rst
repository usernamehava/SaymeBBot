===============================================
    SaymeBBot
===============================================

Бот присылает вопрос, на который вамм нужно ответить, выбрав правильный вариант из четырех.

Что тут есть?
================

from random import  shuffle

from telegram import  ParseMode, ReplyKeyboardMarkup

from telegram.ext import Updater, CommandHandler, RegexHandler, MessageHandler, Filters

from telegram.ext import messagequeue as mq


Авторы
=======

* Автор: `G.Khava`_
* Наставник: `E.Isa`_



