from PyQt5.QtSql import QSqlQuery
from DataBase.conexaoSQL import ConexaoSQL

class ProdutosDAO:
    def CadastrarProduto(Produtos):
        conn = ConexaoSQL
        db = conn.getConexao()
        db.open()

        query = QSqlQuery()
        query.prepare("INSERT INTO produtos(Codigo1, Codigo2, Nome, Valor, Quanridade) "
                      "VALUES (?, ?, ?, ?, ?)")
        query.addBindValue(Produtos.Codigo1)
        query.addBindValue(Produtos.Codigo2)
        query.addBindValue(Produtos.Nome)
        query.addBindValue(Produtos.Valor)
        query.addBindValue(Produtos.Quantidade)
        query.exec_()
        db.commit()

    # def AtualizarCliente(codigoCli, cliente):
    #     conn = ConexaoSQL
    #     db = conn.getConexao()
    #     db.open()
    #
    #     query = QSqlQuery()
    #     query.prepare("UPDATE Cliente SET Nome = '"+cliente.Nome+"', CPF = '"+cliente.CPF
    #                   +"', Endereco = '"+cliente.Endereco+"', Email = '"+cliente.Email
    #                   +"', Telefone = '"+cliente.Telefone
    #                   +"' WHERE CodigoCli = "+codigoCli)
    #     query.exec_()
    #     db.commit()

    # def ExcluirCliente(codigoCli):
    #     conn = ConexaoSQL
    #     db = conn.getConexao()
    #     db.open()
    #
    #     query = QSqlQuery()
    #     query.prepare("DELETE FROM Cliente WHERE CodigoCli=:codigoCli")
    #     query.bindValue(":codigoCli", codigoCli)
    #     query.exec_()
    #     db.commit()

    # def PesquisarTodosClientes():
    #     conn = ConexaoSQL
    #     db = conn.getConexao()
    #     db.open()
    #
    #     sql = "SELECT * FROM Cliente"
    #     query = QSqlQuery(sql)
    #
    #     return query

    # def PesquisarCliente(valor, tipo):
    #     conn = ConexaoSQL
    #     db = conn.getConexao()
    #     db.open()
    #
    #     if tipo=='Código':
    #         sql = "SELECT * FROM Cliente where CodigoCli = " + valor
    #         query = QSqlQuery(sql)
    #     elif tipo=='Nome':
    #         sql = "SELECT * FROM Cliente where Nome = '"+valor+"'"
    #         query = QSqlQuery(sql)
    #     elif tipo=='CPF':
    #         sql = "SELECT * FROM Cliente where CPF = '" + valor+"'"
    #         query = QSqlQuery(sql)
    #
    #     return query