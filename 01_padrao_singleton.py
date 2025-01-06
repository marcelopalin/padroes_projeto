class Singleton(object):
    """
    Implementação do padrão de projeto Singleton em Python.

    O padrão Singleton garante que uma classe tenha apenas uma única instância durante 
    todo o ciclo de vida da aplicação. Este código utiliza o método especial __new__ 
    para verificar se já existe uma instância criada. Caso não exista, cria uma nova 
    instância; caso contrário, retorna a instância já criada.

    Atributos:
        instance (Singleton): A única instância da classe Singleton.

    Métodos:
        __new__(cls): Método especial para criar ou retornar a única instância da classe.
    """

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
            print(f'Criando o objeto {cls.instance}')
        return cls.instance


# Testando o padrão Singleton
s1 = Singleton()
print(f'Instância 1: {id(s1)}')

s2 = Singleton()
print(f'Instância 2: {id(s2)}')

# Resultado:
# Ambas as instâncias (s1 e s2) terão o mesmo ID, provando que são a mesma instância.

#    - A instância era criada no momento em que a classe era chamada pela primeira vez, utilizando o método especial `__new__`.
#    - Não há separação explícita entre o ato de criar a instância e o de acessá-la.

## Em 02_singleton_lazy_instance.py:
# Vamos aprender como implementar o padrão Singleton com Lazy Initialization em Python.

#   - A Lazy Initialization (inicialização preguiçosa) é uma estratégia onde a instância de um objeto só é criada no momento em que ela é realmente necessária. 
#   - Neste caso, a instância única é criada dentro do método `get_instance` e não diretamente no método construtor `__init__`.