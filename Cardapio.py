import sqlite3
import locale
import datetime
import calendar

class Cardapio:
    locale.setlocale(locale.LC_TIME, 'pt_BR.utf8')
    def __init__(self):
        self.titulo_da_semana = ['Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sábado', 'Domingo']
        self.dias_da_semana = []
        self.cardapio_semana = []

    def consultar_banco(self):
        connect = sqlite3.connect("banco.db")
        cursor = connect.cursor()
        cursor.execute("SELECT data_da_semana  FROM cardapio")
        self.dias_da_semana = [row[0] for row in cursor.fetchall()]
        #self.dias_da_semana = cursor.fetchall()
        #data_atual = datetime.date.today()
        #self.titulo_da_semana = data_atual.strftime('%A')
        #self.titulo_da_semana = calendar.day_name[0]
        cursor.execute("SELECT *FROM cardapio")
        self.cardapio_semana = cursor.fetchall()
        connect.close()
        for i in range(len(self.dias_da_semana)):
            print(self.dias_da_semana[i])


    def ExibirCardapioDiario(self, dia_da_semana):
        indice = dia_da_semana.weekday()
        #indice = 1
        print(f"indice = {indice}")
        #print("Cardápio de hoje   {}   {}\nPrato principal 1: {}\nPrato principal 2: {}\nPrato principal 3: {}\nAcompanhamento 1: {}\nAcompanhamento 2: {}\nAcompanhamento 3: {}\nAcompanhamento 4: {}\nDoce: {}\nBebida 1: {}\nBebida 2: {}\nBebida 3: {}".format(self.dias_da_semana[indice], self.titulo_da_semana[indice], self.cardapio_semana[indice][1], self.cardapio_semana[indice][2], self.cardapio_semana[indice][3], self.cardapio_semana[indice][4], self.cardapio_semana[indice][5], self.cardapio_semana[indice][6], self.cardapio_semana[indice][7], self.cardapio_semana[indice][8], self.cardapio_semana[indice][9], self.cardapio_semana[indice][10], self.cardapio_semana[indice][11]))
        if indice < 4:
            s = "----------------------------------------------------------------\n"
            return "{} {}\n{}*Prato principal 1:* {}\n*Prato principal 2:* {}\n*Prato principal 3:* {}\n{}*Acompanhamento 1:* {}\n*Acompanhamento 2:* {}\n*Acompanhamento 3:* {}\n*Acompanhamento 4:* {}\n{}*Doce:* {}\n{}*Bebida 1:* {}\n*Bebida 2:* {}\n*Bebida 3:* {}".format(self.dias_da_semana[indice], self.titulo_da_semana[indice], s, self.cardapio_semana[indice][1], self.cardapio_semana[indice][2], self.cardapio_semana[indice][3], s, self.cardapio_semana[indice][4], self.cardapio_semana[indice][5], self.cardapio_semana[indice][6], self.cardapio_semana[indice][7], s, self.cardapio_semana[indice][8], s, self.cardapio_semana[indice][9], self.cardapio_semana[indice][10], self.cardapio_semana[indice][11])
            #return "{} {}\n*Prato principal 1:* {}\nPrato principal 2: {}\nPrato principal 3: {}\nAcompanhamento 1: {}\nAcompanhamento 2: {}\nAcompanhamento 3: {}\nAcompanhamento 4: {}\nDoce: {}\nBebida 1: {}\nBebida 2: {}\nBebida 3: {}".format(self.dias_da_semana[indice], self.titulo_da_semana[indice], self.cardapio_semana[indice][1], self.cardapio_semana[indice][2], self.cardapio_semana[indice][3], self.cardapio_semana[indice][4], self.cardapio_semana[indice][5], self.cardapio_semana[indice][6], self.cardapio_semana[indice][7], self.cardapio_semana[indice][8], self.cardapio_semana[indice][9], self.cardapio_semana[indice][10], self.cardapio_semana[indice][11])