#!/usr/bin/env python
# -*- coding: utf-8 -*-

from telegram.ext import CommandHandler, Filters, MessageHandler, Updater
from emoji import emojize
from conf.settings import TELEGRAM_TOKEN, HTTP_CATS_URL
import random


def start(bot, update):
    response_message = "Obrigado por me adicionar como amigo!"
    bot.send_message(
        chat_id=update.message.chat_id,
        text=response_message
    )
    response_message = "Serei seu parceiro nessa caminhada, sempre lhe incentivando mostrando hacks e sacadas de emprendendorismo! "

    bot.send_message(
        chat_id=update.message.chat_id,
        text=response_message
    )
    response_message = "Tamo junto e é só o começo!"
    bot.send_message(
        chat_id=update.message.chat_id,
        text=response_message
    )



def random(bot, update):
    import random
    file = open("datacoach.txt", "r")
    a = file.read()
    b = a.split("//")
    print len(b)
    t= len(b) -1
    print t
    print "parada"
    i = random.randint(0,t)

    print i
    response_message = b[i]
    print response_message
    bot.send_message(
        chat_id=update.message.chat_id,
        text=response_message
    )


def unknown(bot, update):
    response_message = "Have you changed your mindset today? ? =^._.^="
    bot.send_message(
        chat_id=update.message.chat_id,
        text=response_message
    )


def main():
    updater = Updater(token=TELEGRAM_TOKEN)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(
        CommandHandler('start', start)
    )
    dispatcher.add_handler(
        CommandHandler('random', random)
    )
    # dispatcher.add_handler(
    #     CommandHandler('http', http_cats, pass_args=True)
    # )
    dispatcher.add_handler(
        MessageHandler(Filters.command, unknown)
    )

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    print("press CTRL + C to cancel.")
    main()
