import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import style
style.use('ggplot')
import numpy as np
from math import exp

def logistic_probability(b0, b1, b2, x1, x2):
    # b2
    # b1: slope defines steepness
    # b0: shifts curve left and right
    p = 1 / (1+exp(-(b0 + b1*x1 + b2*x2)))
    return p
    
def logistic_model(b0, b1, b2):
    x1s = [x for x in range(100)]
    x2s = [x for x in range(100)]
    ps = [logistic_probability(b0, b1, b2, x1, x2) for x1, x2 in zip(x1s, x2s)]
    
    return np.array(x1s, dtype=np.float64), np.array(x2s, dtype=np.float64), np.array([ps], dtype=np.float64)
    
def main():
    logistic_b0, logistic_b1, logistic_b2 = -5, 1/10, 1/19
    logistic_x1s, logistic_x2s, logistic_ps = logistic_model(logistic_b0, logistic_b1, logistic_b2)
    
    # TODO: fix graph
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(logistic_x1s, logistic_x2s, logistic_ps,  rstride=1, cstride=1, color='b', alpha=0.5)
    ax.set_xlabel('X1s')
    ax.set_ylabel('X2s')
    ax.set_zlabel('ps')
    plt.show()
    
    
    
    
if __name__ == '__main__':
    main()