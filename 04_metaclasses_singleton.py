class MetaSingleton(type):
    """
    Metaclasse que implementa o padrão Singleton.

    Uma metaclasse é uma classe especial que define o comportamento das classes que ela cria.
    Neste caso, a metaclasse `MetaSingleton` redefine o método `__call__` para garantir que
    a classe criada por ela siga o padrão Singleton.

    Métodos:
        __call__(cls, *args, **kwargs): Controla a criação de instâncias, garantindo que apenas
        uma instância seja criada para a classe `Produto`.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Sobrescreve o método __call__ para controlar a criação de instâncias.

        Caso uma instância da classe já exista, ela será retornada. Se ainda não existir,
        uma nova instância será criada e armazenada.

        Args:
            *args: Argumentos posicionais para o construtor da classe.
            **kwargs: Argumentos nomeados para o construtor da classe.

        Returns:
            A única instância da classe `Produto`.
        """
        if cls not in cls._instances:
            print(f'Criando nova instância da classe {cls.__name__} com argumentos: {args}')
            cls._instances[cls] = super().__call__(*args, **kwargs)
        else:
            print(f'Retornando instância existente da classe {cls.__name__}')
        return cls._instances[cls]


class Produto(metaclass=MetaSingleton):
    """
    Classe que utiliza a metaclasse `MetaSingleton` para implementar o padrão Singleton.

    Atributos:
        nome (str): Primeiro valor armazenado no objeto.
        preco (int): Segundo valor armazenado no objeto.
    """

    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


# Testando o padrão Singleton com metaclasses
obj1 = Produto("Camisa", 720)  # Criando a primeira instância
print(f'Objeto 1: {obj1}, ID: {id(obj1)}')

obj2 = Produto("Caneta", 36)  # Tentativa de criar uma nova instância
print(f'Objeto 2: {obj2}, ID: {id(obj2)}')

# Verificando os valores armazenados
print(f'Valores do objeto 1: nome={obj1.nome}, preco={obj1.preco}')
print(f'Valores do objeto 2: nome={obj2.nome}, preco={obj2.preco}')


