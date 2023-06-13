import datetime
import os

import telebot
from Cardapio import Cardapio

BOT_TOKEN = os.environ.get('')

bot = telebot.TeleBot("")

cardapio = Cardapio()

@bot.message_handler(commands=['start'])
def send_menu(message):
    menu = "Selecione uma opção:\n\n" \
           "/cardapio"

    bot.send_message(message.chat.id, menu)

@bot.message_handler(commands=['ola'])
def send_welcome(message):
    bot.reply_to(message, "Olá, eu sou o bot do Restaurante Acadêmico. Como posso ajudar?")

@bot.message_handler(commands=['cardapio'])
def send_welcome(message):
    cardapio.consultar_banco()
    string = cardapio.ExibirCardapioDiario(datetime.date.today())
    bot.reply_to(message, string, parse_mode='Markdown')# esse parse mode serve para exibir em negrito
    bot.send_message(message.chat.id, "Deseja exibir o cardapio semanal?")#esta função permite enviar uma mensagem, diferente da anterior que é uma resposta
    string = cardapio.ExibirCardapioSemanal()
    bot.send_message(message.chat.id, string, parse_mode='Markdown')


@bot.message_handler(commands=['saldo'])
def send_welcome(message):
    bot.reply_to(message, "Informe o seu número de matrícula: ")

@bot.message_handler(commands=['informe'])
def send_welcome(message):
    bot.reply_to(message, "Informes são mensagens que devem ser enviadas no início da conversa quando são registrados. Não há informes!")

@bot.message_handler(commands=['faq'])
def send_welcome(message):
    bot.reply_to(message, "O Restaurante Acadêmico é um projeto de assistência a alunos que é responsável por garantir almoço e lanches a estudantes e servidores do IFCE campus Maracanaú. Deseja ver todas as perguntas ou tem algo específico?")

@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message, message.text)


bot.infinity_polling()
