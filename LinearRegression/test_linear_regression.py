import matplotlib.pyplot as plt
from matplotlib import style
import random
style.use('fivethirtyeight')

from linear_regression import LinearRegression

def create_dataset(how_many, variance, step=2, correlation=False):
    val = 1
    ys = []
    for i in range(how_many):
        y = val + random.randrange(-variance, variance)
        ys.append(y)
        if correlation and correlation == 'pos':
            val += step
        elif correlation and correlation == 'neg':
            val -= step
    xs = [i for i in range(len(ys))]
    return xs, ys #np.array(xs, dtype=np.float64), np.array(ys, dtype=np.float64)

def main():
    xs, ys = create_dataset(50, 10, 2, correlation='neg')
    trian_xs, train_ys  = xs[:25], ys[:25]
    test_xs, test_ys    = xs[25:], ys[25:]
    
    # ml model 
    model = LinearRegression()
    model.fit(trian_xs, train_ys)
    preds = model.predictions(xs)
    print("{:1.2f}".format(model.score(ys, preds)))
    
    # plot the dataset
    plt.scatter(trian_xs, train_ys)
    plt.scatter(test_xs, test_ys)
    plt.plot(xs, preds)
    plt.show()
    
if __name__ == '__main__':
    main()