import os
import telebot

API_KEY = os.getenv('API_KEY')
bot = telebot.TeleBot(API_KEY)

@bot.message_handler(command=['help'])
def help(message)
    bot.repy_to(message, "Hello World! This bot is currently a WIP.")

bot.polling()
