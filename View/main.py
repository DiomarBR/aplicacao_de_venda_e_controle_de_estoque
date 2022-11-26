from PyQt5 import uic,QtWidgets

def VoltarInicio():
    estoque.close()
    inicial.show()
    
def ChamarEstoque():
    estoque.show()
    inicial.close()
    

    
    
app=QtWidgets.QApplication([])
inicial=uic.loadUi(r"View\Ui\maingui.ui")
estoque=uic.loadUi(r"View\Ui\produtos.ui")
inicial.button_estoque.clicked.connect(ChamarEstoque)
estoque.inicio.clicked.connect(VoltarInicio)

inicial.show()
app.exec()
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