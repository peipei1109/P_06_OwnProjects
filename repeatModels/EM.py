# -*- encoding: utf-8 -*-

__author__ = 'luopei'

import numpy as np
from scipy import stats

# 硬币投掷结果观测序列
observations = np.array([[1, 0, 0, 0, 1, 1, 0, 1, 0, 1],
                         [1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
                         [1, 0, 1, 1, 1, 1, 1, 0, 1, 1],
                         [1, 0, 1, 0, 0, 0, 1, 1, 0, 0],
                         [0, 1, 1, 1, 0, 1, 1, 1, 0, 1]])


#抛硬币是一个二项分布，可以用scipy中的binom来计算。对于第一行数据，正反面各有5次，所以：
coin_A_pmf_observation_1 = stats.binom.pmf(5,10,0.6)


# 类似地，可以计算第一行数据由B生成的概率：
coin_B_pmf_observation_1 = stats.binom.pmf(5,10,0.5)

#输出
print coin_A_pmf_observation_1,coin_B_pmf_observation_1

# 将两个概率正规化，得到数据来自硬币A的概率：
normalized_coin_A_pmf_observation_1 = coin_A_pmf_observation_1/(coin_A_pmf_observation_1+coin_B_pmf_observation_1)
print "%0.2f" %normalized_coin_A_pmf_observation_1   



'''
这个值类似于三硬币模型中的μ，只不过多了一个下标，代表是第几行数据（数据集由5行构成）。同理，可以算出剩下的4行数据的μ。

有了μ，就可以估计数据中AB分别产生正反面的次数了。μ代表数据来自硬币A的概率的估计，将它乘上正面的总数，得到正面来自硬币A的总数，同理有反面，同理有B的正反面。

'''


# 给出EM算法单个迭代的代码：   
def em_single(priors, observations):
    """
    EM算法单次迭代
    Arguments
    ---------
    priors : [theta_A, theta_B]
    observations : [m X n matrix]
 
    Returns
    --------
    new_priors: [new_theta_A, new_theta_B]
    
    :param priors:
    :param observations:
    :return:
    """
    counts = {'A': {'H': 0, 'T': 0}, 'B': {'H': 0, 'T': 0}}
    theta_A = priors[0]
    theta_B = priors[1]
    # E step
    for observation in observations:
        len_observation = len(observation)
        num_heads = observation.sum()
        num_tails = len_observation - num_heads
        contribution_A = stats.binom.pmf(num_heads, len_observation, theta_A)
        contribution_B = stats.binom.pmf(num_heads, len_observation, theta_B)   # 两个二项分布
        weight_A = contribution_A / (contribution_A + contribution_B)
        weight_B = contribution_B / (contribution_A + contribution_B)
        # 更新在当前参数下A、B硬币产生的正反面次数
        counts['A']['H'] += weight_A * num_heads
        counts['A']['T'] += weight_A * num_tails
        counts['B']['H'] += weight_B * num_heads
        counts['B']['T'] += weight_B * num_tails
    # M step
    new_theta_A = counts['A']['H'] / (counts['A']['H'] + counts['A']['T'])
    new_theta_B = counts['B']['H'] / (counts['B']['H'] + counts['B']['T'])
    return [new_theta_A, new_theta_B]

# 给定循环的两个终止条件：模型参数变化小于阈值；循环达到最大次数，就可以写出EM算法的主循环了：

def em(observations, prior, tol=1e-6, iterations=10000):
    """
    EM算法
    :param observations: 观测数据
    :param prior: 模型初值
    :param tol: 迭代结束阈值
    :param iterations: 最大迭代次数
    :return: 局部最优的模型参数
    """
    import math
    iteration = 0
    while iteration < iterations:
        new_prior = em_single(prior, observations)
        delta_change = np.abs(prior[0] - new_prior[0])
        if delta_change < tol:
            break
        else:
            prior = new_prior
            iteration += 1
    return [new_prior, iteration]


#给定数据集和初值，就可以调用EM算法了：
print em(observations, [0.6, 0.5])

# 我们可以改变初值，试验初值对EM算法的影响。
print em(observations, [0.5,0.6])

print em(observations, [0.3,0.3])

print   em(observations, [0.9999,0.00000001])


