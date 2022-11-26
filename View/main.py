from PyQt5 import QtCore, QtGui, QtQuickWidgets

from view.produtos import Ui_MainWindow

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


# import sqlite3
# con = sqlite3.connect("aplicacao_de_venda_e_controle_de_estoque\DataBase\produtos.db")
# codigo = int(input("Digite o codigo de barras: "))
# codig2 = int(input("Digite o codigo de barras 2 se nao tem e 0: "))
# nome = input('Digite o nome do produto: ')
# valor = float(input('Digite o valor do produto: '))
# quantidade = int(input('Digite a quantidade de produto: '))
# cursor = con.cursor()
# cursor.execute(f"INSERT INTO estoque VALUES({codigo}, {codig2}, '{nome}', {valor}, {quantidade})")
# con.commit()
#
# x = cursor.execute("SELECT * FROM estoque")
#
# for i in x:
#     print(i)