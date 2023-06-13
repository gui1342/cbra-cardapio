import datetime
import os
import telebot

from Cardapio import Cardapio
from Informe import Informe
from Faq import Faq

BOT_TOKEN=''
#BOT_TOKEN = os.environ.get('BOT_TOKEN')

bot = telebot.TeleBot(BOT_TOKEN)
cardapio = Cardapio()
informe = Informe()


#Incorporar commands na classe message_handler como uma lista não funciona, por algum motivo a função send_welcome só recebe o primeiro index da lista.

@bot.message_handler(commands=['start'])
def send_menu(message):
    menu = "Selecione uma opção:\n\n" \
           "/Cardapio_diario\n" \
            "/Cardapio_semanal\n" \
            "/Saldo\n" \
            "/Faq"
    bot.send_message(message.chat.id, menu)

@bot.message_handler(commands=['ola'])
def send_welcome(message):
    bot.reply_to(message, "Olá, eu sou o bot do Restaurante Acadêmico. Como posso ajudar?")
    
@bot.message_handler(commands=['Cardapio_diario'])
def send_welcome(message):
    cardapio.consultar_banco()
    string = cardapio.ExibirCardapioDiario(datetime.date.today())
    bot.reply_to(message, string, parse_mode='Markdown')# esse parse mode serve para exibir em negrito
    send_menu(message)

@bot.message_handler(commands=['Cardapio_semanal'])
def send_welcome(message):
    string = cardapio.ExibirCardapioSemanal()
    bot.send_message(message.chat.id, string, parse_mode='Markdown')
    send_menu(message)

@bot.message_handler(commands=['Saldo'])
def send_welcome(message):
    bot.reply_to(message, "Informe o seu número de matrícula: ")
    send_menu(message)

@bot.message_handler(commands=['informe'])
def send_welcome(message):
    string = informe.exibir_informe()
    if string:
        bot.reply_to(message, string)
    else:
        bot.reply_to(message, "string vazia")
    send_menu(message)

@bot.message_handler(commands=['Faq'])
def send_welcome(message):
    bot.reply_to(message, "O Restaurante Acadêmico é um projeto de assistência a alunos que é responsável por garantir almoço e lanches a estudantes e servidores do IFCE campus Maracanaú. Deseja ver todas as perguntas ou tem algo específico?")
    send_menu(message)

@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message, message.text)
    send_menu(message)

bot.infinity_polling()