import sqlite3
import locale
import datetime
import calendar

class Cardapio:
    locale.setlocale(locale.LC_TIME, 'pt_BR.utf8')
    def __init__(self):
        self.titulo_da_semana = ""
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
        self.titulo_da_semana = calendar.day_name[0]
        cursor.execute("SELECT *FROM cardapio")
        self.cardapio_semana = cursor.fetchall()
        connect.close()
        for i in range(len(self.dias_da_semana)):
            print(self.dias_da_semana[i])


    def ExibirCardapioDiario(self, dia_da_semana):
        #indice = dia_da_semana.weekday()
        indice = 1
        print(f"indice = {indice}")
        if indice < 50:
            return "Cardápio de hoje {} {}\nPrato principal 1: {}\nPrato principal 2:{}".format(self.dias_da_semana[indice], calendar.day_name[indice], self.cardapio_semana[indice][1], self.cardapio_semana[indice][2])