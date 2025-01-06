
### Código Singleton Monostate

class Monostate:
    """
    Implementação do padrão Singleton na variação Monostate.

    Monostate é uma abordagem onde todas as instâncias da classe compartilham o mesmo estado
    (atributos), mas são objetos (instâncias) distintos (com IDs diferentes). Isso é feito utilizando
    um dicionário compartilhado para armazenar o estado da classe.

    Atributos:
        __estado (dict): Dicionário compartilhado que contém os atributos de todas as instâncias.

    Métodos:
        __new__(cls, *args, **kwargs): Define que todas as instâncias compartilham o mesmo estado.
    """

    __estado = {}  # Dicionário compartilhado entre todas as instâncias

    def __new__(cls, *args, **kwargs):
        """
        Método especial que configura o estado compartilhado entre as instâncias.
        """
        obj = super(Monostate, cls).__new__(cls, *args, **kwargs)
        obj.__dict__ = cls.__estado  # Aponta o __dict__ da instância para o estado compartilhado
        return obj


# Testando o Monostate
m1 = Monostate()
print(f'M1 ID: {id(m1)}')
print(m1.__dict__)  # Exibe o estado de m1

m2 = Monostate()
print(f'M2 ID: {id(m2)}')
print(m2.__dict__)  # Exibe o estado de m2

# Alterando um atributo na instância m1
m1.nome = 'Felicity'
m1.idade = 32

# Observando o estado compartilhado
print(f'M1: {m1.__dict__}')
print(f'M2: {m2.__dict__}')  # O atributo 'nome' também aparece em m2


# ### Explicação do Monostate

# - **Monostate**:
#   - No padrão **Monostate**, todas as instâncias compartilham o mesmo estado, mas continuam sendo objetos diferentes.
#   - Isso é feito através do atributo especial `__dict__`, que normalmente é um dicionário único para cada instância. 
# No Monostate, todas as instâncias apontam para o mesmo dicionário de estado.

# - **`__dict__`**:
#   - É um dicionário interno que armazena os atributos e seus valores para cada instância de uma classe.
#   - No Monostate, `__dict__` de todas as instâncias é configurado para apontar para o mesmo dicionário compartilhado (`__estado`), 
# garantindo que o estado seja único para todas as instâncias, enquanto os objetos permanecem diferentes.

# ---

# ### Diferenças entre Singleton e Monostate

# 1. **Singleton**:
#    - Há apenas uma única instância da classe em todo o programa.
#    - Compartilha tanto o estado quanto o objeto (o ID da instância é sempre o mesmo).

# 2. **Monostate**:
#    - Há várias instâncias da classe (com IDs diferentes), mas todas compartilham o mesmo estado.
#    - É mais flexível que Singleton, já que permite criar objetos distintos com o mesmo comportamento.

# ---

# ### Quando Utilizar o Monostate

# O Monostate é útil quando:

# 1. **Compartilhamento de Estado**:
#    - Há a necessidade de garantir que várias instâncias compartilhem o mesmo estado, mas sem forçar uma única instância.

# 2. **Configurações Globais**:
#    - Útil para armazenar configurações de um sistema (como opções de log ou cache) acessíveis a partir de múltiplas instâncias.

# 3. **Objetos de Coordenação**:
#    - Quando diferentes instâncias de um objeto precisam trabalhar de forma sincronizada 
# (por exemplo, controladores de sessões ou estados de máquinas de estado).

# ---

# ### Exemplos na Vida Real

# 1. **Gerenciamento de Configurações**:
#    - Imagine uma aplicação onde várias partes precisam acessar e modificar as mesmas configurações 
# globais, como a URL da API, mas cada módulo pode criar sua própria instância.

# 2. **Cache Compartilhado**:
#    - Em sistemas que utilizam caching, você pode criar várias instâncias de um cache compartilhado com acesso ao mesmo estado subjacente.

# 3. **Componentes de UI**:
#    - Quando widgets ou componentes de UI precisam refletir o mesmo estado centralizado, mas ainda precisam 
#     ser tratados como instâncias independentes para eventos.

# ---

# ### Conclusão

# O padrão **Monostate** é uma variação interessante do Singleton, oferecendo flexibilidade 
# ao permitir múltiplas instâncias enquanto compartilha o mesmo estado. 
# Ele é especialmente útil em cenários que exigem sincronização de estado 
# sem restringir a criação de múltiplos objetos.