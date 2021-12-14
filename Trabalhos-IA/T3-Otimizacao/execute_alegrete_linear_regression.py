import alegrete
import numpy as np

def execute_linear_regression():
    data = np.genfromtxt('alegrete.csv', delimiter=',')
    # (all_theta_zeroes, all_theta_ones) = alegrete.fit(data, 1, 1, 0.0005, 1)
    # print(len(all_theta_zeroes), len(all_theta_ones))
    # print(f'Mean squared error: {alegrete.compute_mse(all_theta_zeroes[0], all_theta_ones[0], data)}')

    # (all_theta_zeroes, all_theta_ones) = alegrete.fit(data, 1, 1, 0.0005, 2)
    # print(len(all_theta_zeroes), len(all_theta_ones))
    # print(f'Mean squared error: {alegrete.compute_mse(all_theta_zeroes[1], all_theta_ones[1], data)}')

    # (all_theta_zeroes, all_theta_ones) = alegrete.fit(data, 1, 1, 0.0005, 3)
    # print(len(all_theta_zeroes), len(all_theta_ones))
    # print(f'Mean squared error: {alegrete.compute_mse(all_theta_zeroes[2], all_theta_ones[2], data)}')

    # (all_theta_zeroes, all_theta_ones) = alegrete.fit(data, 1, 1, 0.0005, 4)
    # print(len(all_theta_zeroes), len(all_theta_ones))
    # print(f'Mean squared error: {alegrete.compute_mse(all_theta_zeroes[3], all_theta_ones[3], data)}')

    print(f'Starting Mean squared error: {alegrete.compute_mse(1, 1, data)}')
    # for i in range(1,551):
    #     (all_theta_zeroes, all_theta_ones) = alegrete.fit(data, 0, 0, 0.01, i)
    #     print(len(all_theta_zeroes), len(all_theta_ones))
    #     print(f'Mean squared error: {alegrete.compute_mse(all_theta_zeroes[i-1], all_theta_ones[i-1], data)}')

    (all_theta_zeroes, all_theta_ones) = alegrete.fit(data, 0, 0, 0.0117, 15500)
    print(len(all_theta_zeroes), len(all_theta_ones))
    print(f'Mean squared error: {alegrete.compute_mse(all_theta_zeroes[15499], all_theta_ones[15499], data)}')


# Por algum motivo, '0.01' para alpha parece ser um ponto de virada no algoritmo (pelo menos na minha implementacao):
#   qualquer valor de 0.01 para baixo vai reduzindo o erro medio a cada epoca/iteracao (quanto menor, mais devagar a melhora).
#   jah qualquer valor acima de 0.01 faz com que o erro medio aumente de forma consistente.
# O numero de iteracoes parece soh ajudar, mas para valores muito acima de 1500 parece ter pouquissimo ganho.
# Por conta disso, vou fixar alpha no melhor valor aparente (0.01) e numero de iteracoes em 15500 (arbitrariamente).
# Os thetas iniciais talvez ainda possam ser fine-tuned, o ganho nao deve ser muuuuito grande, 
#   mas, para os valores fixados de alpha e numero de iteracoes, parece ainda dar para ter alguma melhora visivel
execute_linear_regression()
