# -*- encoding: utf-8 -*-

__author__ = 'luopei'

# MCMC模拟Beta分布

import random
import numpy as np
import matplotlib.pyplot as plt
import scipy.special as ss
# 真实Beta分布概率密度函数
def beta(x, a, b):
    return (1.0 / ss.beta(a,b)) * x**(a-1) * (1-x)**(b-1)
# Beta分布概率密度函数(忽略了Beta函数)
def beta_fpdf(x,a,b):
    return x**(a-1) * (1-x)**(b-1)
# 根据接受概率决定是否转移
def transform(ap):
    stone = random.uniform(0,1)
    if stone>=ap:
        return False
    else:
        return True
def beta_mcmc(N_hops,a,b):
    states = []
    cur = random.uniform(0,1)
    for i in range(0,N_hops):
        states.append(cur)
        next = random.uniform(0,1)
        ap = min(beta_fpdf(next,a,b)/beta_fpdf(cur,a,b),1) # 计算接受概率
        if transform(ap):
            cur = next
    return states[-1000:] # 返回进入平稳分布后的1000个状态
# 绘制通过MCMC方法抽样的Beta分布
def plot_beta(a, b):
    Ly = []
    Lx = []
    i_list = np.mgrid[0:1:100j]
    for i in i_list:
        Lx.append(i)
        Ly.append(beta(i, a, b))
    # 绘制真实的Beta分布进行对照
    plt.plot(Lx, Ly, label="Real Distribution: a="+str(a)+", b="+str(b))
    plt.hist(beta_mcmc(100000,a,b),normed=True,bins=25, histtype='step',label="Simulated_MCMC: a="+str(a)+", b="+str(b))
    plt.legend()
    plt.show()
plot_beta(0.5, 0.6)