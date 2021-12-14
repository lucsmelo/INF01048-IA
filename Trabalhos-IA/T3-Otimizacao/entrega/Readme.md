# Integrantes

## Lucas Lima de Melo

Cartao: 00315747

Turma: A

## Pedro Fronchetti Costa da Silva

Cartao: 00313878

Turma: A

## Tiago Silveira Ceccon

Cartao: 00278142

Turma: B

# Bibliotecas

Foram usadas as bibliotecas:

-Matplotlib.pyplot

-Random

# Eplicações e descrições

## 8 Queens

### Valores

Uma das possíveis combinações de valores que resultam na minimização de conflitos é (g, n, k, m, e) = (35, 32, 17, 0.81, False).

### Comentarios

Como o programa é não determinístico, achar uma solução que consistemente zere o número de conflitos é complicado, então decidimos utilizar uma que consistemente minimize entre
os valores 0 e 1 no número de conflitos.

Nosso algoritmo para o `evaluate` assume que a entrada é uma configuração válida do problema. Utilizar configurações inválidas, como por exemplo uma columa com rainha colocada na "linha" -3 ou 15, pode gerar um comportamento estranho no resultado da função, com a estranheza sendo aproximadamente proporcional ao nível de estranheza da configuração inválida. Em especial, notar que percorremos as colunas da esquerda para a direita procurando por conflitos, e o único critério de parada é a coluna mais à direita - as diagonais (que são verificadas dentro do mesmo loop), portanto, podem fazer comparações com valores de linha fora do tabuleiro, o que não altera em nada o resultado para entradas válidas, já que nenhuma rainha vai estar lá nesses casos. Aqui adotamos o bom e velho ideal de Garbage In, Garbage Out.

O código para geração do gráfico encontra-se no próprio arquivo `eight_queens.py` . Utilizamos uma variável global e condicionais para que ele por padrão não seja gerado quando o script é importado/usado como módulo, mas seja gerado quando o usuário executa esse script diretamente (por exemplo, com o comando `python eight_queens.py` no diretório que contém o arquivo).

## Alegrete

### Valores

Para uma boa execução, usar valores iniciais: `theta_0 = 0`, `theta_1 = 0`, `alpha = 0.01` e `num_iterations = 15500`. O erro quadrático médio obtido deve resultar em torno de `8.953942751950361`.

Obs.: Para o trecho do notebook `alegrete.ipynb` em que é gerada a animação, esses valores resultam em uma animação com tamanho grande demais (suficiente para o ambiente reclamar e não prosseguir) e uma demora gigantesca. Os demais trechos, que apenas executam a regressão mas não geram a animação, funcionam tranquilamente. Caso se deseje rodar o trecho da animação, utilizar como número de iterações algo em torno de `num_iterations = 1500` (os demais valores podem continuar iguais), que resulta em um EQM em torno de 8.953999429824432 .

### Comentarios

Para a nossa implementação, observamos que as redondezas do valor `0.01` para alpha se comportou como um ponto de mudança drástica no comportamento do algoritmo. Qualquer valor abaixo disso resulta em uma melhora contínua através de cada iteração conforme o esperado, com valores mais baixos resultando em uma melhoria mais lenta, porém de `0.02` para cima, começamos a encontrar overshooting, com o erro quadrático médio aumentando em cada iteração, fazendo com que as execuções divergissem de forma espetacular. Pequenos acréscimos no valor sugerido, como os do intervalo `0.011` a `0.012` acabaram entrando em um terreno nebuloso composto por ganhos marginais demais para serem justificáveis e comportamentos erráticos como overshooting e warnings de overflow, portanto optamos pelo valor `0.01` como a alternativa boa e segura.

# Fontes externas consultadas

Para esse trabalho, foram consultados apenas os materiais utilizados na disciplina: slides, vídeos e anotações.
