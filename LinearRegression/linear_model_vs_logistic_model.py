import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')

from math import exp

def linear_model(b0, b1):
    # y = b0 + b1 * x
    xs = [x for x in range(100)]
    ys = [(x * b1 + b0) for x in xs]
    return xs, ys

def logistic_probability(b0, b1, x):
    # b1: slope defines steepness
    # b0: shifts curve left and right
    # TODO: draw a 3d graph of this curve
    p = 1 / (1+exp(-(b0+b1*x)))
    return p
    
def logistic_model(b0, b1):
    xs = [x for x in range(100)]
    ys = [logistic_probability(b0, b1, x) for x in xs]
    
    return xs, ys
    
def main():
    linear_b0, linear_b1 = 0, 1/100
    logistic_b0, logistic_b1 = -5, 1/10
    linear_xs, linear_ys = linear_model(linear_b0, linear_b1)
    logistic_xs, logistic_ys = logistic_model(logistic_b0, logistic_b1)
    
    plt.plot(linear_xs, linear_ys)
    plt.plot(logistic_xs, logistic_ys)
    plt.plot(logistic_xs, [1 for x in logistic_xs])
    plt.show()
    
    
    
if __name__ == '__main__':
    main()