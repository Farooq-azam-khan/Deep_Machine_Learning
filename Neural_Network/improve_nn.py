import random 
import math
from matrix import Matrix


class ActivationFunction():
    #            fucntion, derivative of function 
    def __init__(self, func, dfunc):
        self.func = func
        self.dfunc = dfunc

sigmoid = ActivationFunction(lambda x: 1/(1+math.exp(-x)), lambda y: y*(1-y))
tanh = ActivationFunction(lambda x: math.tanh(x), lambda y: 1 - (y*y))

class NNLayer():
    def __init__(self, nodes, layer_type='hidden'):
        self.nodes = nodes 
        self.data = Matrix(self.nodes, 1)
        self.layer_type = layer_type
        
    def __repr__(self):
        return f"(nodes: {self.nodes} layer:{self.layer_type}) \n {self.data}"
    def __str__(self):
        return f"(nodes: {self.nodes} layer:{self.layer_type}) \n {self.data}"

class Weight():
    def __init__(self, row, cols):
        self.row = row
        self.cols = cols 
        self.data = Matrix(row, cols)
        self.data.randomize()
    def __repr__(self):
        return f"(row: {self.row}, col: {self.cols}) \n {self.data}"
    def __str__(self):
        return f"(row: {self.row}, col: {self.cols}) \n {self.data}"
        
class Bias():
    def __init__(self, row):
        self.data = Matrix(row, 1)
        self.data.randomize()
    def __repr__(self):
        return f"{self.data}"
    def __str__(self):
        return f"{self.data}"

class NeuralNetwork():
    def __init__(self, input_nodes, output_nodes):
        self.input_nodes = input_nodes
        self.add_layer_indx = 0
        self.layers = []
        self.output_nodes = output_nodes
        
        # add input and output layer
        self.add_input_layer()
        self.add_layer_indx += 1
        self.add_output_layer()
        
        # set learning rate
        self.set_learning_rate(0.1)
        # set activation function 
        self.set_activation_function()
        # inputs -> (weight 0) hidden layer 0 -> (weight 1) hidden layer 1 -> ... -> (weight output) output
        self.num_weights_bias = len(self.layers) - 1
        self.weights = []
        self.bias = []
        
    def set_weights(self):
        self.weights = []
        for i in range(len(self.layers)-1):
            current_layer = self.layers[i]
            next_layer = self.layers[i+1]
            self.weights.append(Weight(next_layer.nodes, current_layer.nodes))
            
    def set_bias(self, nodes):
        self.bias = []
        for i in range(len(self.layers)):
            current_layer = self.layers[i]
            self.bias.append(Bias(current_layer.nodes))
        
    def set_learning_rate(self, lr):
        self.lr = lr
        
    def set_activation_function(self, func = sigmoid):
        self.activation_function = func
    
    # add hidden layer
    def add_hidden_layer(self, nodes):
        # add a new layer as the second last element 
        self.layers.insert(self.add_layer_indx, NNLayer(nodes))
        self.add_layer_indx += 1
        
        previous_layer = self.layers[self.add_layer_indx - 1]
                
        self.set_bias(nodes)
        self.set_weights()
        
    def add_input_layer(self):
        # insert input layer at the beginning 
        self.layers.insert(0, NNLayer(self.input_nodes, 'input_layer'))
    
    def add_output_layer(self):
        # insert output layer to the end
        self.layers.append(NNLayer(self.output_nodes, 'output_layer'))
        
    def predict(self):
        # TODO: predict algorithm 
        # each iteration activation_function * (weight * layer + bias)
        pass
    def train(self):
        # TODO: trian model 
        pass
        
    def __repr__(self):
        ret = f"input_nodes: {self.input_nodes}, output_nodes: {self.output_nodes}\n"
        ret += f"len(layers): {len(self.layers)}, len(weights): {len(self.weights)}, len(bias): {len(self.bias)}\n"
        ret += f"{self.layers}"
        ret += "weights: \n" 
        ret += f"{self.weights}"
        ret += "bias: \n" 
        ret += f"{self.bias}"
        return ret
        
        