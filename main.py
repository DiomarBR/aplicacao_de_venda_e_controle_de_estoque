from file import Ui_Mercearia_do_Ziron
from produtos import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets

import sys

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Mercearia_do_Ziron = QtWidgets.QMainWindow()
    ui = Ui_Mercearia_do_Ziron()
    ui.setupUi(Mercearia_do_Ziron)
    Mercearia_do_Ziron.show()
    sys.exit(app.exec_())

    def chekFields(self):
       # vendas =
        estoque = 0
        if not self.button_estoque.clicked():
            estoque = 0
        else:
            estoque = 1

    if produtos == 1:
        if __name__ == "__main__":
            import sys

            app = QtWidgets.QApplication(sys.argv)
            MainWindow = QtWidgets.QMainWindow()
            ui = Ui_MainWindow()
            ui.setupUi(MainWindow)
            MainWindow.show()
            sys.exit(app.exec_())
    else:
        produtos = 0

import sqlite3
con = sqlite3.connect("produtos.db")
codigo = int(input("Digite o codigo de barras: "))
codig2 = int(input("Digite o codigo de barras 2 se nao tem e 0: "))
nome = input('Digite o nome do produto: ')
valor = float(input('Digite o valor do produto: '))
quantidade = int(input('Digite a quantidade de produto: '))
cursor = con.cursor()
cursor.execute(f"INSERT INTO estoque VALUES({codigo}, {codig2}, '{nome}', {valor}, {quantidade})")
con.commit()

x = cursor.execute("SELECT * FROM estoque")

for i in x:
    print(i)