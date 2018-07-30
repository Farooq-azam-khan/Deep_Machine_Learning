from neural_network import NeuralNetwork 
import random

def main():
    # XOR problem revisisted
    nn = NeuralNetwork(2, 4, 1)
    input = [1,0]
    output = nn.feed_forward(input)

    # data
    val0 = [0,0]
    val1 = [0,1]
    val2 = [1,0]
    val3 = [1,1]
    inputs = [val0, val1, val2, val3]
    targets = [[0], [1], [1], [0]]

    for _ in range(10000):
        indx = random.randrange(0,4)
        input = inputs[indx]
        target = targets[indx]
        # print(input, target)
        nn.train(input, target)

    print("xor problem")
    for i in range(len(inputs)):
        input = inputs[i]
        prediction = nn.feed_forward(input)
        print("{} | {} -> {:.2f}".format(input[0], input[1], prediction[0]))

    # TODO: save neural network
if __name__ == "__main__":
    main()
