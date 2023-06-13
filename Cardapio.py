import sqlite3
from datetime import datetime
import datetime

class Cardapio:
    def __init__(self):
        self.titulo_da_semana = ['Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sábado', 'Domingo']
        self.dias_da_semana = [] #alimetado com o banco de dados todas as datas da semana
        self.cardapio_semana = [] #todo o cardapio será armazenado aqui, cada dia representa um indice

#A função consultar banco fará a consulta de todos os dados necessarios e armazenará em listas
    def consultar_banco(self):
        connect = sqlite3.connect("banco.db")#abre uma conexão com o banco, entre parenteses o nome do arquivo
        cursor = connect.cursor()#o cursor vai permitir fazer ações com essa conexão
        cursor.execute("SELECT data_da_semana  FROM cardapio")#seleciona a coluna data da semana da tabela cardapio
        self.dias_da_semana = [row[0] for row in cursor.fetchall()]#armazena as datas na lista
        cursor.execute("SELECT *FROM cardapio")#seleciona todos os dados da tabela cardapio
        self.cardapio_semana = cursor.fetchall()#armazena na lista cardapio da semana
        connect.close()#encerra a conexão com o banco

    def ExibirCardapioDiario(self, dia_da_semana):#recebe uma data
        indice = dia_da_semana.weekday()#cada dia esta representado com um indice, começando com 0 e segunda feira
        if indice < 5:#se o dia for segunda a sexta ele exibe o cardapio
            s = "----------------------------------------------------------------\n"
            return "Cardápio de hoje  {}  {}\n{}*Prato principal 1:* {}\n*Prato principal 2:* {}\n*Prato principal 3:* {}\n{}*Acompanhamento 1:* {}\n*Acompanhamento 2:* {}\n*Acompanhamento 3:* {}\n*Acompanhamento 4:* {}\n{}*Doce:* {}\n{}*Bebida 1:* {}\n*Bebida 2:* {}\n*Bebida 3:* {}".format(self.dias_da_semana[indice], self.titulo_da_semana[indice], s, self.cardapio_semana[indice][1], self.cardapio_semana[indice][2], self.cardapio_semana[indice][3], s, self.cardapio_semana[indice][4], self.cardapio_semana[indice][5], self.cardapio_semana[indice][6], self.cardapio_semana[indice][7], s, self.cardapio_semana[indice][8], s, self.cardapio_semana[indice][9], self.cardapio_semana[indice][10], self.cardapio_semana[indice][11])
        else:#finais de semana ou qualquer outra condição
            return "O Restaurante Acadêmico não oferece refeições hoje"


    def ExibirCardapioSemanal(self):
        data = datetime.date.today()#recebe a data atual
        indice = data.weekday()#atribui o indice correspondente a data no dia da semana (0-6)
        cardapio_semanal = ""#cria a variavel como string
        s = "----------------------------------------------------------------\n"#separador de campos na exibição
        if 0 <= indice <= 3:#se o dia atual for segunda a quinta
            for i in range(indice, 4):#do indice ate sexta feira
                indice += 1#acrescenta um dia para exibir apenas os dias posteriores
                cardapio_semanal += "Cardápio do dia  {}  {}\n\n*Prato principal 1:* {}\n*Prato principal 2:* {}\n*Prato principal 3:* {}\n{}".format(self.dias_da_semana[indice], self.titulo_da_semana[indice], self.cardapio_semana[indice][1], self.cardapio_semana[indice][2], self.cardapio_semana[indice][3], s)
            return cardapio_semanal
        else: return "Desculpe ainda não temos dados para esta semana"#se for sexta feira exibe esta mensagem
