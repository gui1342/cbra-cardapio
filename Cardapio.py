import sqlite3
#import locale
from datetime import datetime, timedelta
import datetime
#import calendar

class Cardapio:
    #locale.setlocale(locale.LC_TIME, 'pt_BR.utf8')
    def __init__(self):
        self.titulo_da_semana = ['Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sábado', 'Domingo']
        self.dias_da_semana = []
        self.cardapio_semana = []

    def consultar_banco(self):
        connect = sqlite3.connect("banco.db")
        cursor = connect.cursor()
        cursor.execute("SELECT data_da_semana  FROM cardapio")
        self.dias_da_semana = [row[0] for row in cursor.fetchall()]
        cursor.execute("SELECT *FROM cardapio")
        self.cardapio_semana = cursor.fetchall()
        connect.close()

    def ExibirCardapioDiario(self, dia_da_semana):
        indice = dia_da_semana.weekday()
        if indice < 5:
            s = "----------------------------------------------------------------\n"
            return "Cardápio de hoje  {}  {}\n{}*Prato principal 1:* {}\n*Prato principal 2:* {}\n*Prato principal 3:* {}\n{}*Acompanhamento 1:* {}\n*Acompanhamento 2:* {}\n*Acompanhamento 3:* {}\n*Acompanhamento 4:* {}\n{}*Doce:* {}\n{}*Bebida 1:* {}\n*Bebida 2:* {}\n*Bebida 3:* {}".format(self.dias_da_semana[indice], self.titulo_da_semana[indice], s, self.cardapio_semana[indice][1], self.cardapio_semana[indice][2], self.cardapio_semana[indice][3], s, self.cardapio_semana[indice][4], self.cardapio_semana[indice][5], self.cardapio_semana[indice][6], self.cardapio_semana[indice][7], s, self.cardapio_semana[indice][8], s, self.cardapio_semana[indice][9], self.cardapio_semana[indice][10], self.cardapio_semana[indice][11])
        else:
            return "O Restaurante Acadêmico não oferece refeições hoje"


    def ExibirCardapioSemanal(self):
        data = datetime.date.today()
        indice = data.weekday()
        cardapio_semanal = ""
        s = "----------------------------------------------------------------\n"
        if 0 <= indice <= 3:
            for i in range(indice, 4):
                indice += 1
                cardapio_semanal += "Cardápio do dia  {}  {}\n\n*Prato principal 1:* {}\n*Prato principal 2:* {}\n*Prato principal 3:* {}\n{}".format(self.dias_da_semana[indice], self.titulo_da_semana[indice], self.cardapio_semana[indice][1], self.cardapio_semana[indice][2], self.cardapio_semana[indice][3], s)
            return cardapio_semanal
        else: return "Desculpe ainda não temos dados para esta semana"
