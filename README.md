# Conceitos de Orientação a Objetos


Uma classe é uma estrutura fundamental na programação orientada a objetos que serve como um molde ou modelo para criar objetos, 
definindo o comportamento (métodos) e as características (atributos) que esses objetos terão. 

Um objeto é uma entidade criada a partir 
de uma classe, representando uma instância concreta com dados específicos e funcionalidade própria. 

A instância refere-se ao objeto em si, 
ou seja, a materialização de uma classe na memória, sendo possível criar múltiplas instâncias de uma mesma classe, cada uma com seus 
próprios dados. 

Atributos são as variáveis associadas a uma classe ou objeto, usadas para armazenar informações que caracterizam 
o objeto, como o nome ou idade de uma pessoa em uma classe Pessoa. 

O estado de um objeto é definido pelos valores atuais dos seus 
atributos em um dado momento, representando a condição ou configuração específica do objeto naquele instante. 
Juntos, esses conceitos formam a base para modelar sistemas complexos no paradigma orientado a objetos.


## Padrões de projeto

### Singleton

O padrão Singleton garante que uma classe tenha apenas uma única instância durante 
todo o ciclo de vida da aplicação. Este código utiliza o método especial __new__ 
para verificar se já existe uma instância criada. Caso não exista, cria uma nova 
instância; caso contrário, retorna a instância já criada.

### Singleton Lazy Instance

Lazy Initialization (Inicialização Preguiçosa) é uma técnica que adia a criação 
da instância até que ela seja realmente necessária. Isso pode ser útil para 
economizar recursos em situações onde a instância pode nunca ser usada.

# ### Comparação com o Código Anterior

**Código Anterior**:
- A instância era criada no momento em que a classe era chamada pela primeira vez, utilizando o método especial `__new__`.
- Não havia separação explícita entre o ato de criar a instância e o de acessá-la.

**Código Atual (Lazy Instance)**:
- A instância só é criada quando o método `get_instance` é chamado pela primeira vez.
- Isso permite que o objeto seja carregado na memória apenas se necessário, economizando recursos.


### Monostate

Monostate é uma abordagem onde todas as instâncias da classe compartilham o mesmo estado
(atributos), mas são objetos (instâncias) distintos (com IDs diferentes). Isso é feito utilizando
um dicionário compartilhado para armazenar o estado da classe.


