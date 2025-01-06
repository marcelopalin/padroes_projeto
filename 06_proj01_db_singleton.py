import sqlite3
from typing import Optional


class Database:
    """
    Implementação do padrão Singleton diretamente na classe `Database` usando o método especial __new__.

    Atributos:
        connection (Optional[sqlite3.Connection]): Objeto de conexão com o banco de dados.
        cursor (Optional[sqlite3.Cursor]): Cursor associado à conexão com o banco de dados.

    Métodos:
        connect() -> sqlite3.Cursor:
            Cria uma conexão com o banco de dados SQLite se ainda não existir e retorna o cursor.
    """
    _instance = None  # Atributo para armazenar a única instância da classe
    connection: Optional[sqlite3.Connection] = None
    cursor: Optional[sqlite3.Cursor] = None

    def __new__(cls, *args, **kwargs):
        """
        Sobrescreve o método __new__ para garantir que apenas uma instância seja criada.

        Returns:
            Database: A única instância da classe.
        """
        if cls._instance is None:
            print(f"Criando a instância da classe {cls.__name__}")
            cls._instance = super(Database, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def connect(self) -> sqlite3.Cursor:
        """
        Estabelece uma conexão com o banco de dados SQLite, se ainda não estiver conectada.

        Returns:
            sqlite3.Cursor: O cursor associado à conexão com o banco de dados.
        """
        if self.connection is None:
            print('Não temos ainda uma conexão... vamos criá-la...')
            self.connection = sqlite3.connect('db.geek')
            self.cursor = self.connection.cursor()
        return self.cursor


# Testando o padrão Singleton com __new__
db1 = Database().connect()  # Cria a primeira conexão com o banco de dados
db2 = Database().connect()  # Retorna a mesma conexão existente

# Verificando se as conexões são as mesmas
print(f'DB1 Cursor ID: {id(db1)}')
print(f'DB2 Cursor ID: {id(db2)}')

# Resultado esperado:
# Ambos os IDs (db1 e db2) serão iguais, confirmando que a mesma instância foi utilizada.
