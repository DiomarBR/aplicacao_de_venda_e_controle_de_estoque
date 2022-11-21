from PyQt5 import QtCore, QtGui, QtWidgets

from View.produtos import Ui_MainWindow
# from View.FrmAluguel import Ui_FrmAluguel
# from View.FrmPesqAluguel import Ui_FrmPesqAluguel



class Ui_FrmPrincipal(object):

    def setupUi(self, Mercearia_do_Ziron):
        Mercearia_do_Ziron.setObjectName("Mercearia_do_Ziron")
        Mercearia_do_Ziron.resize(350, 550)
        Mercearia_do_Ziron.setMinimumSize(QtCore.QSize(350, 550))
        Mercearia_do_Ziron.setMaximumSize(QtCore.QSize(350, 550))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("venv/favicon_io/favicon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Mercearia_do_Ziron.setWindowIcon(icon)
        self.menu_principal = QtWidgets.QWidget(Mercearia_do_Ziron)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        self.menu_principal.setFont(font)
        self.menu_principal.setObjectName("menu_principal")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.menu_principal)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.main = QtWidgets.QFrame(self.menu_principal)
        self.main.setStyleSheet("background-color: rgb(42, 156, 255);")
        self.main.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.main.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main.setLineWidth(0)
        self.main.setObjectName("main")


        self.button_vendas = QtWidgets.QPushButton(self.main)
        self.button_vendas.setGeometry(QtCore.QRect(100, 190, 161, 51))
        self.button_vendas.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.button_vendas.setStyleSheet("background-color: rgb(41, 99, 161);")
        self.button_vendas.setObjectName("button_vendas")



        self.button_estoque = QtWidgets.QPushButton(self.main)
        self.button_estoque.setGeometry(QtCore.QRect(100, 280, 161, 51))
        self.button_estoque.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.button_estoque.setStyleSheet("background-color: rgb(41, 99, 161);")
        self.button_estoque.setObjectName("button_estoque")
        self.button_estoque.clicked.connect(self.estoque)

        self.button_exportar = QtWidgets.QPushButton(self.main)
        self.button_exportar.setGeometry(QtCore.QRect(100, 390, 161, 51))
        self.button_exportar.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.button_exportar.setStyleSheet("background-color: rgb(41, 99, 161);")
        self.button_exportar.setObjectName("button_exportar")




        self.label = QtWidgets.QLabel(self.main)
        self.label.setGeometry(QtCore.QRect(60, 50, 221, 81))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.main)
        Mercearia_do_Ziron.setCentralWidget(self.menu_principal)

        self.retranslateUi(Mercearia_do_Ziron)
        QtCore.QMetaObject.connectSlotsByName(Mercearia_do_Ziron)

    def retranslateUi(self, Mercearia_do_Ziron):
        _translate = QtCore.QCoreApplication.translate
        Mercearia_do_Ziron.setWindowTitle(_translate("Mercearia_do_Ziron", "Mercearia do Ziron"))
        self.button_vendas.setText(_translate("Mercearia_do_Ziron", "VENDAS"))
        self.button_estoque.setText(_translate("Mercearia_do_Ziron", "ESTOQUE"))
        self.button_exportar.setText(_translate("Mercearia_do_Ziron", "Exportar para excel"))
        self.label.setText(_translate("Mercearia_do_Ziron", "Mercearia Do Ziron"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Mercearia_do_Ziron = QtWidgets.QMainWindow()
    ui = Ui_FrmPrincipal()
    ui.setupUi(Mercearia_do_Ziron)
    Mercearia_do_Ziron.show()
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