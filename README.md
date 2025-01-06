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
todo o ciclo de vida da aplicação. Este código utiliza o método especial **new**
para verificar se já existe uma instância criada. Caso não exista, cria uma nova
instância; caso contrário, retorna a instância já criada.

### Singleton Lazy Instance

Lazy Initialization (Inicialização Preguiçosa) é uma técnica que adia a criação
da instância até que ela seja realmente necessária. Isso pode ser útil para
economizar recursos em situações onde a instância pode nunca ser usada.

### Comparação com o Código Anterior

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

### Metaclasse Singleton

#### **1. Metaclasse `MetaSingleton`**

A metaclasse `MetaSingleton` foi projetada para implementar o padrão **Singleton**. 
Isso significa que, ao utilizar essa metaclasse em uma classe (`Produto` no caso), 
a classe criada terá apenas uma única instância durante o ciclo de vida do programa.

- **Atributos**:

  - **`_instances`**: Um dicionário interno que armazena as instâncias únicas de cada classe que utiliza `MetaSingleton` como metaclasse.

- **Método `__call__`**:
  - Sobrescreve o comportamento padrão do método `__call__` (executado ao instanciar uma classe).
  - **Fluxo de funcionamento**:
    1. Verifica se a classe (`cls`) já possui uma instância armazenada no dicionário `_instances`.
    2. Se não existir, cria uma nova instância da classe utilizando o método padrão da metaclasse (`super().__call__`) e a armazena no dicionário.
    3. Se já existir, retorna a instância armazenada, ignorando quaisquer novos argumentos fornecidos.

---

#### **2. Classe `Produto`**

A classe `Produto` utiliza a metaclasse `MetaSingleton`, o que a torna automaticamente uma 
classe Singleton. Apesar de receber argumentos ao ser instanciada, esses argumentos só têm efeito 
na primeira instância criada, já que as chamadas subsequentes retornam a mesma instância.

- **Atributos**:

  - **`nome`**: Representa o nome do produto.
  - **`preco`**: Representa o preço do produto.

- **Comportamento Singleton**:
  - A primeira vez que a classe é instanciada, cria-se um objeto com os valores fornecidos.
  - Chamadas subsequentes retornam o mesmo objeto, sem criar uma nova instância ou alterar os valores dos atributos.

---

### Fluxo de Execução no Teste

1. **Primeira Instância (`obj1`)**:

   - O código `obj1 = Produto("Camisa", 720)` verifica se já existe uma instância no dicionário `_instances`.
   - Como é a primeira chamada, uma nova instância é criada com os atributos:
     - `nome = "Camisa"`
     - `preco = 720`
   - A instância é armazenada no dicionário `_instances` e utilizada para todas as chamadas subsequentes.

2. **Segunda Instância (`obj2`)**:
   - O código `obj2 = Produto("Caneta", 36)` tenta criar uma nova instância.
   - No entanto, como a instância da classe `Produto` já existe no dicionário `_instances`, a instância anterior é retornada.
   - Os valores de `nome` e `preco` permanecem como `"Camisa"` e `720`, definidos na primeira instância.

---

### Saída do Programa

```plaintext
Criando nova instância da classe Produto com argumentos: ('Camisa', 720)
Objeto 1: <__main__.Produto object at 0x7f8e2c4e4df0>, ID: 140249823050224
Retornando instância existente da classe Produto
Objeto 2: <__main__.Produto object at 0x7f8e2c4e4df0>, ID: 140249823050224
Valores do objeto 1: nome=Camisa, preco=720
Valores do objeto 2: nome=Camisa, preco=720
```

---

### Pontos Importantes

1. **Mesma Instância**:

   - O `id(obj1)` e o `id(obj2)` são iguais, provando que ambos referem-se ao mesmo objeto.

2. **Argumentos Ignorados**:
   - Na segunda chamada, os argumentos `"Caneta", 36` são ignorados, já que a instância já existe e não é recriada.

---

### Diferenças com Singleton Baseado em `__new__`

- **Com Metaclasse**:

  - O controle do Singleton está centralizado na metaclasse, o que permite reaproveitar 
  o comportamento em múltiplas classes apenas utilizando a mesma metaclasse.
  - É ideal para projetos que possuem várias classes Singleton.

- **Com `__new__`**:
  - O padrão Singleton é implementado individualmente em cada classe.
  - É mais simples, mas menos reutilizável.

---

### Cenários de Uso

1. **Gerenciamento de Recursos**:

   - Quando é necessário garantir que apenas uma instância de um recurso seja criada, como conexão com banco de dados ou controle de sessão.

2. **Centralização de Estado**:

   - Útil para classes que precisam compartilhar um único estado em todo o programa.

3. **Configurações Globais**:
   - Permite armazenar configurações de forma centralizada e acessível em diferentes partes do código.

---

### Conclusão

A abordagem Singleton com metaclasses é poderosa, pois centraliza a lógica de criação única, 
tornando-a reutilizável para diversas classes. No caso do exemplo, a classe `Produto` é um Singleton, 
e a lógica do padrão é implementada de forma limpa e escalável, adequada para projetos maiores e mais complexos.
