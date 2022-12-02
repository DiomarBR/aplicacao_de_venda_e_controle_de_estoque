from PyQt5 import uic,QtWidgets
import sqlite3

def FecharEstoque():
    estoque.close()
    inicial.show()

def FecharVendas():
    vendas.close()
    inicial.show()
    
def ChamarVendas():
    vendas.show()
    estoque.close()
    inicial.close()
    
    
def ChamarEstoque():
    estoque.show()
    vendas.close()
    inicial.close()
    
def connect():
    global conn
    conn=sqlite3.connect(r"DataBase\produtos.db")
    
    global cursor 
    cursor = conn.cursor()
    
    
app=QtWidgets.QApplication([])
inicial=uic.loadUi(r"View\Ui\maingui.ui")
vendas=uic.loadUi(r"View\Ui\vendas.ui")
estoque=uic.loadUi(r"View\Ui\produtos.ui")
inicial.button_estoque.clicked.connect(ChamarEstoque)
inicial.button_vendas.clicked.connect(ChamarVendas)
vendas.butto_inicio.clicked.connect(FecharVendas)
vendas.button_estoque.clicked.connect(ChamarEstoque)
estoque.inicio.clicked.connect(FecharEstoque)
estoque.button_vendas.clicked.connect(ChamarVendas)

inicial.show()
app.exec()


def SalvarDados():
    codigo1 = estoque.codigo01.text()
    codigo2 = estoque.codigo02.text()
    nome = estoque.nome.text()
    valor = estoque.valor.text()
    quantidade = estoque.quantidade.text()
    

    cursor.execute(f"INSERT INTO estoque VALUES({codigo1}, {codigo2}, '{nome}', {valor}, {quantidade})")
    banco.commit()

connect()

estoque.enviar_buton.clicked.connect(SalvarDados)


# con = sqlite3.connect("aplicacao_de_venda_e_controle_de_estoque\DataBase\produtos.db")
# codigo = int(input("Digite o codigo de barras: "))
# codig2 = int(input("Digite o codigo de barras 2 se nao tem e 0: "))
# nome = input('Digite o nome do produto: ')
# valor = float(input('Digite o valor do produto: '))
# quantidade = int(input('Digite a quantidade de produto: '))
# cursor = con.cursor()
# cursor.execute(f"INSERT INTO estoque VALUES({codigo}, {codig2}, '{nome}', {valor}, {quantidade})")
# con.commit()

# x = cursor.execute("SELECT * FROM estoque")

# for i in x:
#     print(i)

