# Controle de treinos da semana

Aplicativo de linha de comando em Python para registrar treinos, consultar os treinos realizados e acompanhar uma meta semanal. A meta inicial é de **5 treinos**.

## Como executar

1. Instale o Python 3, caso ainda não esteja instalado.
2. Coloque este README na mesma pasta do arquivo `treinos(3).py`.
3. Abra o terminal nessa pasta e execute:

   ```bash
   python "treinos(3).py"
   ```

   No Windows, se o comando `python` não funcionar, experimente `py "treinos(3).py"`.

Não é necessário instalar bibliotecas adicionais.

## Opções do menu

| Opção | Funcionalidade |
| --- | --- |
| `1` | Pergunta o nome do treino e o acrescenta à lista. Uma resposta vazia é recusada. |
| `2` | Mostra todos os treinos registrados ou avisa que a lista está vazia. |
| `3` | Mostra quantos treinos foram registrados, a meta e quantos faltam. |
| `0` | Encerra o programa. |

Qualquer outra opção apresenta a mensagem `Opção inválida.` e o menu aparece novamente.

## Exemplo de uso

```text
Escolha uma opção: 1
Qual treino você fez? Peito
Treino registrado: Peito

Escolha uma opção: 1
Qual treino você fez? Tríceps
Treino registrado: Tríceps

Escolha uma opção: 2
- Peito
- Tríceps

Escolha uma opção: 3
Treinos realizados: 2 | Meta: 5
Treinos que faltam: 3
```

## Organização do código

O programa cria `treinos_da_semana = []` antes do menu. A mesma lista é passada às funções de registrar, listar e mostrar progresso. `meta_semanal = 5` define a quantidade de treinos desejada.

| Função | O que faz |
| --- | --- |
| `registrar_treino(treinos)` | Lê o nome digitado e usa `treinos.append(nome)` para acrescentá-lo à lista recebida. |
| `listar_treinos(treinos)` | Usa `len(treinos)` para verificar se há registros. Se houver, o `for` mostra cada item. |
| `calcular_faltantes(meta, realizados)` | Devolve com `return` a diferença entre meta e realizados, ou `0` quando a meta já foi alcançada. |
| `mostrar_progresso(treinos, meta)` | Conta os itens com `len`, chama `calcular_faltantes` e mostra o resultado. |

O `while True` mantém o menu ativo. `if` e `elif` escolhem a função correspondente à opção digitada. A opção `0` usa `break` para terminar o laço. O `else` trata opções inválidas.

### Como a lista chega à função

Ao escolher `1`, o menu executa `registrar_treino(treinos_da_semana)`. Dentro dessa chamada, o parâmetro `treinos` aponta para a lista `treinos_da_semana`. Assim, `treinos.append(nome)` acrescenta o nome digitado à lista que o menu utiliza nas outras opções.

## Armazenamento e contagem dos treinos

A meta configurada é de 5 treinos. Cada nome registrado conta como um treino, inclusive se o mesmo nome for informado mais de uma vez. Os registros ficam na memória durante a execução e a lista começa vazia quando o programa é aberto novamente.
