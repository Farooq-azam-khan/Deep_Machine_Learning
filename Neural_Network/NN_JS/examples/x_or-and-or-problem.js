let xor_training_data = [{
    inputs: [0, 0],
    outputs: [0]
  },
  {
    inputs: [0, 1],
    outputs: [1]
  },
  {
    inputs: [1, 0],
    outputs: [1]
  },
  {
    inputs: [1, 1],
    outputs: [0]
  }
];
let and_training_data = [{
    inputs: [0, 0],
    outputs: [0]
  },
  {
    inputs: [0, 1],
    outputs: [0]
  },
  {
    inputs: [1, 0],
    outputs: [0]
  },
  {
    inputs: [1, 1],
    outputs: [1]
  }
];
let or_training_data = [{
    inputs: [0, 0],
    outputs: [0]
  },
  {
    inputs: [0, 1],
    outputs: [1]
  },
  {
    inputs: [1, 0],
    outputs: [1]
  },
  {
    inputs: [1, 1],
    outputs: [1]
  }
];
let nn;
function setup()
{
  //         inputs, hidden_nodes, output
  nn_xor = new NeuralNetwork(2, 4, 1);
  nn_and = new NeuralNetwork(2, 4, 1);
  nn_or = new NeuralNetwork(2, 4, 1);
  // console.log(training_data[0].inputs, training_data[0].targets);
  // train the data (100 times)
  for (let i=0; i<100000; i++)
  {
    let xor_data = random(xor_training_data);
    let and_data = random(and_training_data);
    let or_data = random(or_training_data);
    nn_xor.train(xor_data.inputs, xor_data.outputs);
    nn_and.train(and_data.inputs, and_data.outputs);
    nn_or.train(or_data.inputs, or_data.outputs);
  }

  // test the data
  console.log("exclusive or");
  console.log("0 xor 0: " + nn_xor.feedforward([0,0]));
  console.log("0 xor 1: " + nn_xor.feedforward([0,1]));
  console.log("1 xor 0: " + nn_xor.feedforward([1,0]));
  console.log("1 xor 1: " + nn_xor.feedforward([1,1]));
  console.log("logical and");
  console.log("0 and 0: " + nn_and.feedforward([0,0]));
  console.log("0 and 1: " + nn_and.feedforward([0,1]));
  console.log("1 and 0: " + nn_and.feedforward([1,0]));
  console.log("1 and 1: " + nn_and.feedforward([1,1]));
  console.log("logical or"); 
  console.log("0 or 0: " + nn_or.feedforward([0,0]));
  console.log("0 or 1: " + nn_or.feedforward([0,1]));
  console.log("1 or 0: " + nn_or.feedforward([1,0]));
  console.log("1 or 1: " + nn_or.feedforward([1,1]));
}

function draw()
{

}
