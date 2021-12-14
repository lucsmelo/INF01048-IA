import unittest
import solucao as solucao


class TestaSolucao(unittest.TestCase):
    def test_sucessor(self):
        """
        Testa a funcao sucessor para o estado "2_3541687"
        :return:

        """
        # a lista de sucessores esperados é igual ao conjunto abaixo (ordem nao importa)
        succ_esperados = {("abaixo", "2435_1687"), ("esquerda", "_23541687"), ("direita", "23_541687")}

        sucessores = solucao.sucessor("2_3541687")  # obtem os sucessores chamando a funcao implementada
        self.assertEqual(3, len(sucessores))     # verifica se foram retornados 3 sucessores
        for s in sucessores:                     # verifica se os sucessores retornados estao entre os esperados
            self.assertIn(s, succ_esperados)

    def test_expande(self):
        """
        Testa a função expande para um Node com estado "185432_67" e custo 2
        :return:
        """
        pai = solucao.Nodo("185432_67", None, "abaixo", 2)  # o pai do pai esta incorreto, mas nao interfere no teste
        # a resposta esperada deve conter nodos com os seguintes atributos (ordem dos nodos nao importa)
        resposta_esperada = {
            ("185_32467", pai, "acima", 3),
            ("1854326_7", pai, "direita", 3),
        }

        resposta = solucao.expande(pai)  # obtem a resposta chamando a funcao implementada
        self.assertEqual(2, len(resposta))  # verifica se foram retornados 2 nodos
        for nodo in resposta:
            # verifica se a tupla com os atributos do nodo esta' presente no conjunto com os nodos esperados
            self.assertIn((nodo.estado, nodo.pai, nodo.acao, nodo.custo), resposta_esperada)

    def test_bfs(self):
        """
        Testa o BFS em um estado com solução e outro sem solução
        :return:
        """
        # no estado 2_3541687, a solucao otima tem 23 movimentos.
        self.assertEqual(23, len(solucao.bfs("2_3541687")))
        print("Atencao! O BFS passar nesse teste apenas significa que a lista retornada tem o "
              "numero correto de elementos. Nao verificamos se as acoes levam para a solucao!")

        # nao ha solucao a partir do estado 185423_67
        self.assertIsNone(solucao.bfs("185423_67"))

    def test_astar_hamming(self):
        """
        Testa o A* com dist. Hamming em um estado com solução e outro sem solução
        :return:
        """
        # no estado 2_3541687, a solucao otima tem 23 movimentos.
        self.assertEqual(23, len(solucao.astar_hamming("2_3541687")))
        print("Atencao! O A* Hamming passar nesse teste apenas significa que a lista retornada tem o "
              "numero correto de elementos. Nao verificamos se as acoes levam para a solucao!")

        # nao ha solucao a partir do estado 185423_67
        self.assertIsNone(solucao.astar_hamming("185423_67"))

    def test_astar_manhattan(self):
        """
        Testa o A* com dist. Manhattan em um estado com solução e outro sem solução
        :return:
        """
        # no estado 2_3541687, a solucao otima tem 23 movimentos.
        self.assertEqual(23, len(solucao.astar_manhattan("2_3541687")))
        print("Atencao! O A* Manhattan passar nesse teste apenas significa que a lista retornada tem o "
              "numero correto de elementos. Nao verificamos se as acoes levam para a solucao!")

        # nao ha solucao a partir do estado 185423_67
        self.assertIsNone(solucao.astar_manhattan("185423_67"))

    def test_dfs(self):
        """
        Testa o DFS apenas em um estado sem solucao pq ele nao e' obrigado
        a retornar o caminho minimo
        :param estado: str
        :return:
        """
        # nao ha solucao a partir do estado 185423_67
        self.assertEqual(None, solucao.dfs("185423_67"))


if __name__ == '__main__':
    unittest.main()
