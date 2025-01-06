import sqlite3
from typing import Optional

class Singleton(type):
    """
    Metaclasse que implementa o padrão Singleton.

    A metaclasse `Singleton` é usada para garantir que apenas uma instância de qualquer
    classe que a utilize seja criada durante o ciclo de vida da aplicação. A lógica do Singleton
    é implementada no método especial `__call__`.

    Atributos:
        __instances (dict): Um dicionário para armazenar as instâncias únicas das classes.

    Métodos:
        __call__(cls, *args, **kwargs): Sobrescreve o método de criação de instâncias, garantindo
        que apenas uma instância seja criada por classe.
    """
    __instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Controla a criação de instâncias, assegurando que apenas uma instância seja criada.

        Args:
            *args: Argumentos posicionais passados para o construtor da classe.
            **kwargs: Argumentos nomeados passados para o construtor da classe.

        Returns:
            A instância única da classe.
        """
        if cls not in cls.__instances:
            cls.__instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
            print(f'Criando nova instância da classe {cls.__name__} com argumentos: {args}')
        return cls.__instances[cls]


class Database(metaclass=Singleton):
    """
    Classe que utiliza a metaclasse `Singleton` para garantir que apenas uma conexão com
    o banco de dados SQLite seja criada durante a execução.

    Atributos:
        connection (Optional[sqlite3.Connection]): Objeto de conexão com o banco de dados.
        cursor (Optional[sqlite3.Cursor]): Cursor associado à conexão com o banco de dados.

    Métodos:
        connect() -> sqlite3.Cursor:
            Cria uma conexão com o banco de dados SQLite se ainda não existir e retorna o cursor.
    """
    connection: Optional[sqlite3.Connection] = None
    cursor: Optional[sqlite3.Cursor] = None

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


# Testando o padrão Singleton com a classe Database
db1 = Database().connect()  # Cria a primeira conexão com o banco de dados
db2 = Database().connect()  # Retorna a mesma conexão existente

# Verificando se as conexões são as mesmas
print(f'DB1 Cursor ID: {id(db1)}')
print(f'DB2 Cursor ID: {id(db2)}')

# Resultado esperado:
# Ambos os IDs (db1 e db2) serão iguais, confirmando que a mesma instância foi utilizada.
