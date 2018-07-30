from neural_network import NeuralNetwork 
import random 

def poly_true(x):
    y = x*x
    return y

def get_array(num):
    xs = [random.uniform(-10,10) for i in range(num)]
    ys = [poly_true(x) for x in xs]
    
    return xs, ys
def main():
    poly = NeuralNetwork(1, 10, 1)    
    
    xs, ys = get_array(10)
    
    EPOCHS = 20 
    for epoch in range(1, EPOCHS+1):
        for _ in range(1000):
            rand_indx_num = random.randrange(0, len(xs))
            rand_x, target = xs[rand_indx_num], ys[rand_indx_num]
            input_arr = [rand_x]
            poly.train(input_arr, [target])
        # print(f"EPOCH: {epoch} out of {EPOCHS} accuracy: {accuracy}")    
    print('finished')
    
    print(f'{poly.predict([0])}')
    print(f'{poly.predict([0.5])}')
    print(f'{poly.predict([10])}')
    
if __name__ == '__main__':
    main()