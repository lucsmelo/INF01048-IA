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

Não é necessário a instalação de bibliotecas extras. 

Foram utilizadas apenas bibliotecas presentes na distribuição padrão do Python 3.

# Eplicações e descrições

## Função de avaliação

No jogo de Othello, embora o objetivo seja terminar o jogo com mais peças do que o oponente, um número grande de peças pode ser convertido em questão de uma jogada, o que torna o número de jogadas possíveis a maior prioridade no inicio do jogo. O tabuleiro também possui casas de extrema importância, que são as casas do canto, já que uma vez conquistadas, as peças ali não podem ser convertidas pelo oponente. Nossa função de avaliação prioriza a conquista dos cantos do tabuleiro e o número de jogadas, até que todos os cantos estejam conquistados. Desse ponto em diante, passa a buscar o maior número de peças.

## Critério de Parada

Nosso agente vê jogadas com profundidade máxima 7, portanto, esse é o critério de parada.

# Fontes externas consultadas

## Seção "Basic Othello Strategy" do Site "https://www.eothello.com/"

Corners and stable discs:
According to the rules of Othello, once a disc is placed in a corner, that disc can never be flipped back (it is "stable"). Because of that, corners are the most valuable squares on the board. Once you have a corner, you can often build more adjacent stable discs around it. In the example below, Black has the corner at h8, and stable discs next to it.

Danger squares:
Within the Othello board there are squares that are safer than others. When starting a game, it is recommended to play within the 4x4 central area (marked by white translucent discs in the diagram below) when possible. It is often not recommended to move on the squares next to corners (marked by black translucent discs). Moving in these squares could give the opponent access to the adjacent corner.

Mobility:
A common beginner mistake is to try to get as many discs as possible from the beginning. This is not a good strategy in Othello. A better strategy is to focus on limiting your opponent's options, while having many possible moves yourself. This is usually easier to achieve by having fewer discs. In the example below, White, with only one disc, can easily win the game in four moves.

