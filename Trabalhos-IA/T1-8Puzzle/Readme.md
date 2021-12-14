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

# Resultados para entrada '2_3541687'

## DFS
     Total de nós expandidos: 97553
     Tempo decorrido: 1.1085724830627441 segundos
     Custo da solução: 91735

## BFS
     Total de nós expandidos: 110498
     Tempo decorrido: 2.8513777256011963 segundos
     Custo da solução: 23

## A* Hamming
     Total de nós expandidos: 12840
     Tempo decorrido: 0.3401467800140381 segundos
     Custo da solução: 23

## A* Manhattan
     Total de nós expandidos: 1634
     Tempo decorrido: 0.05478644371032715
     Custo da solução: 23


# Fontes externas consultadas

## Dúvida no Stackoverflow - Funcionamento interno da PriorityQueue

Para o A*, utilizamos a classe PriorityQueue do Python para implementar a fronteira. Esbarramos em um possível problema com a forma como ela opera por padrão, em específico no caso de termos dois elementos com prioridade igual: o critério de desempate padrão dela quebrava o código, por não estarmos implementando o método de igualdade entre Nodos. Para entender esse problema e chegar na solução que utilizamos (usar uma condição de desempate extra, sendo ela o id dos objetos), consultamos essa thread no Stackoverlow (a PriorityQueue utiliza heapq internamente para fazer o gerenciamento da fila): https://stackoverflow.com/questions/53554199/heapq-push-typeerror-not-supported-between-instances

Do que está descrito nas respostas ali, utilizamos apenas a ideia de ter o id como critério extra de desempate. No código da função astar (arquivo solucao.py) está indicado com um comentário de várias linhas o ponto em que essa referência foi relevante, inclusive com o mesmo link indicado lá.
