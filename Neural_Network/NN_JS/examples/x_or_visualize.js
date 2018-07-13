let training_data = [{
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
let nn;
let lr_slider; // learning rate slider

let resolution;
let cols;
let rows;

function setup()
{
  createCanvas(400, 400);
  //         inputs, hidden_nodes, output
  nn = new NeuralNetwork(2, 4, 1);

  lr_slider = createSlider(0.01, 0.5, 0.1, 0.01);

  resolution = 5;
  cols = height / resolution;
  rows = width / resolution;
}

function draw()
{
  background(51);
  for (let i=0; i<1000; i++)
  {
    // get a random element from traning_data
    let data = random(training_data);
    // train with the object's inputs and outputs
    nn.train(data.inputs, data.outputs);
  }

  // set the learning rate
  nn.setLearningRate(lr_slider.value());
  noStroke();
  for(let i=0; i<cols; i++)
  {
    for (let j=0; j<rows; j++)
    {
      let x1 = i / cols; // (0 to 1)
      let x2 = j / rows; // (0 to 1)
      let inputs = [x1, x2];
      let y = nn.feedforward(inputs);
      fill(y * 255);
      rect(i*resolution, j*resolution, resolution, resolution);
    }
  }

}
