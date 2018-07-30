from improve_nn import NeuralNetwork 

def main():
    nn = NeuralNetwork(3, 3)
    nn.add_hidden_layer(2)
    nn.add_hidden_layer(2)
    print(nn)

if __name__ == '__main__':
    main()