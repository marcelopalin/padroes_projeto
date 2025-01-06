class Singleton:
    """
    Implementação do padrão Singleton com Lazy Initialization.

    Lazy Initialization (Inicialização Preguiçosa) é uma técnica que adia a criação 
    da instância até que ela seja realmente necessária. Isso pode ser útil para 
    economizar recursos em situações onde a instância pode nunca ser usada.

    Atributos:
        __instance (Singleton): Armazena a instância única da classe.
    """

    __instance = None

    def __init__(self):
        """
        Método construtor que verifica se a instância já foi criada.
        """
        if not Singleton.__instance:
            print('O método __init__ foi chamado...')
        else:
            print(f'A instância já foi criada: {self.get_instance()}')

    @classmethod
    def get_instance(cls):
        """
        Retorna a instância única da classe. Cria a instância caso ainda não exista.

        Returns:
            Singleton: A única instância da classe Singleton.
        """
        if not cls.__instance:
            cls.__instance = Singleton()
        return cls.__instance


# Testando o padrão Singleton com Lazy Initialization
s1 = Singleton()  # O método __init__ é chamado, mas a instância ainda não foi criada.
print(f'Objeto criado agora: {Singleton.get_instance()}')

s2 = Singleton()  # A instância já foi criada.

# ### Explicação da Lazy Initialization

# - **Definição**: 
#   - A Lazy Initialization (inicialização preguiçosa) é uma estratégia onde a instância de um objeto só é criada no momento em que ela é realmente necessária. 
#   - Neste caso, a instância única é criada dentro do método `get_instance` e não diretamente no método construtor `__init__`.

# ---

# ### Comparação com o Código Anterior

# 1. **Código Anterior**:
#    - A instância era criada no momento em que a classe era chamada pela primeira vez, utilizando o método especial `__new__`.
#    - Não havia separação explícita entre o ato de criar a instância e o de acessá-la.

# 2. **Código Atual (Lazy Instance)**:
#    - A instância só é criada quando o método `get_instance` é chamado pela primeira vez.
#    - Isso permite que o objeto seja carregado na memória apenas se necessário, economizando recursos.

# ---

# ### Comparação com Generators

# - **Semelhanças**:
#   - Ambos postergam a criação de recursos.
#   - Um generator cria itens sob demanda, enquanto o Singleton com lazy initialization cria a instância sob demanda.

# - **Diferenças**:
#   - O Singleton garante que sempre exista apenas uma instância única e compartilhada.
#   - Generators, por outro lado, geram novos valores continuamente (dentro de seu contexto de execução) e podem criar múltiplos iteradores.

# ---

# ### Vantagens do Lazy Instance

# 1. **Eficiência de Recursos**:
#    - A instância só ocupa memória e processamento quando realmente necessária.
#    - Ideal para casos onde a instância pode nunca ser usada durante a execução.

# 2. **Melhor Controle**:
#    - A lógica de criação da instância fica isolada no método `get_instance`, facilitando a manutenção e a legibilidade.

# 3. **Flexibilidade**:
#    - É mais fácil modificar a lógica de criação, se necessário, sem impactar o construtor.

# ---

# ### Conclusão

# - **Lazy Initialization** é uma abordagem mais eficiente e controlada em cenários onde o consumo de recursos é uma preocupação ou a criação da instância pode ser evitada. 
# - Comparado ao código anterior, o código com lazy instance é mais alinhado com boas práticas de economia de recursos e flexibilidade arquitetural.