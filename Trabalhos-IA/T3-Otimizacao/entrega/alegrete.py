import numpy as np

# Helper functions
def _predict(theta_0, theta_1, x):
    return theta_1 * x + theta_0       # good old line equation from high school when we were all young and happy


def compute_mse(theta_0, theta_1, data):
    """
    Calcula o erro quadratico medio
    :param theta_0: float - intercepto da reta
    :param theta_1: float -inclinacao da reta
    :param data: np.array - matriz com o conjunto de dados, x na coluna 0 e y na coluna 1
    :return: float - o erro quadratico medio
    """
    n = len(data)

    predicted = [_predict(theta_0, theta_1, element[0]) for element in data]
    
    square_error = lambda x, y: (x - y)**2
    squared_errors = [square_error(predicted[i], data[i][1]) for i in range(n)]

    mse = sum(squared_errors) / n

    return mse


def step_gradient(theta_0, theta_1, data, alpha):
    """
    Executa uma atualização por descida do gradiente  e retorna os valores atualizados de theta_0 e theta_1.
    :param theta_0: float - intercepto da reta
    :param theta_1: float -inclinacao da reta
    :param data: np.array - matriz com o conjunto de dados, x na coluna 0 e y na coluna 1
    :param alpha: float - taxa de aprendizado (a.k.a. tamanho do passo)
    :return: float,float - os novos valores de theta_0 e theta_1, respectivamente
    """
    n = len(data)

    predicted = [_predict(theta_0, theta_1, element[0]) for element in data]

    simple_error = lambda x, y: x - y
    errors = [simple_error(predicted[i], data[i][1]) for i in range(n)]

    # Both expressions below can be checked on page 14 of the second set of slides on week 7 ("Otimizacao Continua.pdf")
    df_d0 = (2 * sum(errors)) / n
    df_d1 = (2 * sum([errors[i] * data[i][0] for i in range(n)])) / n

    new_theta_0 = theta_0 - alpha*df_d0
    new_theta_1 = theta_1 - alpha*df_d1

    return (new_theta_0 , new_theta_1)


def fit(data, theta_0, theta_1, alpha, num_iterations):
    """
    Para cada época/iteração, executa uma atualização por descida de
    gradiente e registra os valores atualizados de theta_0 e theta_1.
    Ao final, retorna duas listas, uma com os theta_0 e outra com os theta_1
    obtidos ao longo da execução (o último valor das listas deve
    corresponder à última época/iteração).

    :param data: np.array - matriz com o conjunto de dados, x na coluna 0 e y na coluna 1
    :param theta_0: float - intercepto da reta
    :param theta_1: float -inclinacao da reta
    :param alpha: float - taxa de aprendizado (a.k.a. tamanho do passo)
    :param num_iterations: int - numero de épocas/iterações para executar a descida de gradiente
    :return: list,list - uma lista com os theta_0 e outra com os theta_1 obtidos ao longo da execução
    """
    current_iteration = 1
    all_theta_zeroes = []
    all_theta_ones = []

    while current_iteration <= num_iterations:
        (cur_theta_zero, cur_theta_one) = step_gradient(theta_0, theta_1, data, alpha)

        all_theta_zeroes.append(cur_theta_zero)
        all_theta_ones.append(cur_theta_one)

        theta_0 = cur_theta_zero
        theta_1 = cur_theta_one

        current_iteration += 1
    
    return (all_theta_zeroes, all_theta_ones)
