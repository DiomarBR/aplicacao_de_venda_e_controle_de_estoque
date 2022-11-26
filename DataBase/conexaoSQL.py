from PyQt5.QtSql import QSqlDatabase

class ConexaoSQL:
    def getConexao():
        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName("produtos.db")

        return db