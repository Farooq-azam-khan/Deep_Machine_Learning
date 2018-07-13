function sigmoid(x)
{
  return 1/(1+Math.exp(-x));
}

function dsigmoid(y)
{
  // return sigmoid(x)*(1-sigmoid(x));
  // y has been sigmoided
  return y * (1-y);
}
class NeuralNetwork
{
  constructor(input_nodes, hidden_nodes, output_nodes)
  {
    this.input_nodes = input_nodes;
    this.hidden_nodes = hidden_nodes;
    this.output_nodes = output_nodes;

    // hint: look from right to left(colums are the left nodes and rows are the right nodes in any matrix)
    //rows are based on number hidden layers and  columns are based on input
    this.weights_input_hidden = new Matrix(this.hidden_nodes, this.input_nodes);
    // rows are based on number of output nodes and columns are based on number of hidden nodes
    this.weights_hidden_output = new Matrix(this.output_nodes, this.hidden_nodes);

    // give random weights at start
    this.weights_input_hidden.randomize();
    this.weights_hidden_output.randomize();

    // bias
    this.bias_hidden = new Matrix(this.hidden_nodes, 1);
    this.bias_output = new Matrix(this.output_nodes, 1);
    // randomize bias
    this.bias_hidden.randomize();
    this.bias_output.randomize();
    // learning rate
    this.learning_rate = 0.1;
  }

  setLearningRate(lr)
  {
    this.learning_rate = lr;
  }

  feedforward(input_array)
  {
    // ----------- Generating the hidden output -----------
    // make the input an instanceof Matrix (because Matrix library expects matrix for multiplication)
    let inputs = Matrix.fromArray(input_array);
    // get the values of the hidden nodes (order matters)
    let hidden = Matrix.multiply(this.weights_input_hidden, inputs);
    hidden.add(this.bias_hidden);
    // activation function
    hidden.map(sigmoid);

    // ----------- Generating the output -----------
    let output = Matrix.multiply(this.weights_hidden_output, hidden);
    output.add(this.bias_output);
    output.map(sigmoid);

    // return array of outputs
    return output.toArray();
  }

  train(inputs_array, target_array)
  {

    // ----------- Feed Forward
    // make the input an instanceof Matrix (because Matrix library expects matrix for multiplication)
    // console.log(inputs_array);
    let inputs = Matrix.fromArray(inputs_array);
    // get the values of the hidden nodes (order matters)
    let hidden = Matrix.multiply(this.weights_input_hidden, inputs);
    hidden.add(this.bias_hidden);
    // activation function
    hidden.map(sigmoid);

    // ----------- Generating the output -----------
    let outputs = Matrix.multiply(this.weights_hidden_output, hidden);
    outputs.add(this.bias_output);
    outputs.map(sigmoid);

    // convert targets to Martix object
    let targets = Matrix.fromArray(target_array);

    // calculate the error
    // ERROR = TARGETS - OUTPUTS
    let output_errors = Matrix.subtract(targets, outputs);

    // --------------------- GRADIENT DESCENT ---------------------
    // gradien = learning_rate*output_erros*outputs * (1 - outputs)*hidden_layer_tranpose;
    // calculate the derivative of activation function
    let gradients = Matrix.map(outputs, dsigmoid);
    // myltiply the output_error with the derivative of the outputs
    gradients.multiply(output_errors);
    // multiply with the lr
    gradients.multiply(this.learning_rate);

    // get the tranpose of the hidden layer
    let hidden_Transpose = Matrix.transpose(hidden);
    // get the change in weights (order matter)
    let weights_hidden_output_deltas = Matrix.multiply(gradients, hidden_Transpose);

    // adjust the weights by the change of the weighted deltas
    this.weights_hidden_output.add(weights_hidden_output_deltas);
    // add the small change in bias
    this.bias_output.add(gradients);

    // calculate the hidden layer errors
    let weights_ho_tranposed = Matrix.transpose(this.weights_hidden_output);
    let hidden_errors = Matrix.multiply(weights_ho_tranposed, output_errors);

    // Calculate the Hidden gradient
    let hidden_gradient = Matrix.map(hidden, dsigmoid);
    hidden_gradient.multiply(hidden_errors);
    hidden_gradient.multiply(this.learning_rate);

    // calculate input to (->) hidden delta
    let inputs_T = Matrix.transpose(inputs);
    let weights_input_hidden_deltas = Matrix.multiply(hidden_gradient, inputs_T);

    this.weights_input_hidden.add(weights_input_hidden_deltas);
    // add the bias
    this.bias_hidden.add(hidden_gradient);
  }
}
