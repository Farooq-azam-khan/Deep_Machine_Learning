// let m = new Matrix(3,2);


class Matrix {
  constructor(rows, cols) {
    this.rows = rows;
    this.cols = cols;
    this.data = Array(this.rows).fill().map(() => Array(this.cols).fill(0));
  }

  copy() {
    let m = new Matrix(this.rows, this.cols);
    for (let i = 0; i < this.rows; i++) {
      for (let j = 0; j < this.cols; j++) {
        m.data[i][j] = this.data[i][j];
      }
    }
    return m;
  }

  static fromArray(arr) {
    return new Matrix(arr.length, 1).map((e, i) => arr[i]);
  }

  static subtract(a, b) {
    if (a.rows !== b.rows || a.cols !== b.cols) {
      console.log('Columns and Rows of A must match Columns and Rows of B.');
      return;
    }

    // Return a new Matrix a-b
    return new Matrix(a.rows, a.cols)
      .map((_, i, j) => a.data[i][j] - b.data[i][j]);
  }

  toArray() {
    let arr = [];
    for (let i = 0; i < this.rows; i++) {
      for (let j = 0; j < this.cols; j++) {
        arr.push(this.data[i][j]);
      }
    }
    return arr;
  }

  randomize() {
    return this.map(e => Math.random() * 2 - 1);
  }

  add(n) {
    if (n instanceof Matrix) {
      if (this.rows !== n.rows || this.cols !== n.cols) {
        console.log('Columns and Rows of A must match Columns and Rows of B.');
        return;
      }
      return this.map((e, i, j) => e + n.data[i][j]);
    } else {
      return this.map(e => e + n);
    }
  }

  static transpose(matrix) {
    return new Matrix(matrix.cols, matrix.rows)
      .map((_, i, j) => matrix.data[j][i]);
  }

  static multiply(a, b) {
    // Matrix product
    if (a.cols !== b.rows) {
      console.log('Columns of A must match rows of B.')
      return;
    }

    return new Matrix(a.rows, b.cols)
      .map((e, i, j) => {
        // Dot product of values in col
        let sum = 0;
        for (let k = 0; k < a.cols; k++) {
          sum += a.data[i][k] * b.data[k][j];
        }
        return sum;
      });
  }

  multiply(n) {
    if (n instanceof Matrix) {
      if (this.rows !== n.rows || this.cols !== n.cols) {
        console.log('Columns and Rows of A must match Columns and Rows of B.');
        return;
      }

      // hadamard product
      return this.map((e, i, j) => e * n.data[i][j]);
    } else {
      // Scalar product
      return this.map(e => e * n);
    }
  }

  map(func) {
    // Apply a function to every element of matrix
    for (let i = 0; i < this.rows; i++) {
      for (let j = 0; j < this.cols; j++) {
        let val = this.data[i][j];
        this.data[i][j] = func(val, i, j);
      }
    }
    return this;
  }

  static map(matrix, func) {
    // Apply a function to every element of matrix
    return new Matrix(matrix.rows, matrix.cols)
      .map((e, i, j) => func(matrix.data[i][j], i, j));
  }

  print() {
    console.table(this.data);
    return this;
  }

  serialize() {
    return JSON.stringify(this);
  }

  static deserialize(data) {
    if (typeof data == 'string') {
      data = JSON.parse(data);
    }
    let matrix = new Matrix(data.rows, data.cols);
    matrix.data = data.data;
    return matrix;
  }
}

if (typeof module !== 'undefined') {
  module.exports = Matrix;
}
// TODO: fix matrix class
// // eg. let matrix = new Matrix(3, 2); (construct a 3 by 2 matrix)
// class Matrix
// {
//   constructor(rows, columns)
//   {
//     this.rows = rows;
//     this.columns = columns;
//     this.data = []; // data stored in matrix
//
//     // initalize the matrix
//     for(let i=0; i<this.rows; i++)
//     {
//       // every row is an array
//       this.data[i] = [];
//       for(let j=0; j<this.columns; j++)
//       {
//         // every row, col is zero
//         this.data[i][j] = 0;
//       }
//     }
//   }
//
//   copy()
//   {
//     let m = new Matrix(this.rows, this.cols);
//     for(let i=0; i<this.rows; i++)
//     {
//       for(let j=0; j<this.columns; j++)
//       {
//         m.data[i][j] = this.data[i][j];
//       }
//     }
//
//     return m;
//   }
//   // give the matirx random values
//   randomize()
//   {
//     for(let i=0; i<this.rows; i++)
//     {
//       for(let j=0; j<this.columns; j++)
//       {
//         // Math.floor(Math.random()*10);
//         this.data[i][j] = Math.random()*2 - 1; // random num btn (-1,1)
//       }
//     }
//   }
//
//   // make the rows into columns and the rows into columns
//   static transpose(matrix)
//   {
//     let result = new Matrix(matrix.columns, matrix.rows);
//     for (let i=0; i<matrix.rows; i++)
//     {
//       for(let j=0; j<matrix.columns; j++)
//       {
//         //                    has to be [i][j]
//         //because iteration is through this.rows, and this.columns
//         result.data[j][i] = this.data[i][j];
//       }
//     }
//     return result;
//   }
//
//
//   // multiply: multiply a number, n, by the matrix
//   multiply(n)
//   {
//     if (n instanceof Matrix)
//     {
//       if (this.rows !== n.rows || this.columns !== n.columns)
//       {
//         console.log("columns of a must match colums of b and same for rows when using hadamard product");
//         return ;
//       }
//       // Hadamard product: element wise multiplication
//       // https://en.wikipedia.org/wiki/Hadamard_product_(matrices)
//       for(let i=0; i< this.row; i++)
//       {
//         for(let j=0; j<this.columns; j++)
//         {
//           this.data[i][j] *= n.data[i][j];
//         }
//       }
//     }
//     else
//     {
//       for(let i=0; i<this.rows; i++)
//       {
//         for(let j=0; j<this.columns; j++)
//         {
//           this.data[i][j] *= n;
//         }
//       }
//     }
//   }
//
//   // add: adds a number n to each value in matrix
//   add(n)
//   {
//     // if the n coming in is part of matrix class;
//     if (n instanceof Matrix)
//     {
//       if (n.rows !== this.rows || n.columns !== this.columns)
//       {
//         console.log("colums and rows must match when adding");
//         return ;
//       }
//       // add the (i,j) values
//       for(let i=0; i<this.rows; i++)
//       {
//         for(let j=0; j<this.columns; j++)
//         {
//           this.data[i][j] += n.data[i][j];
//         }
//       }
//     }
//     else
//     {
//       for(let i=0; i<this.rows; i++)
//       {
//         for(let j=0; j<this.columns; j++)
//         {
//           this.data[i][j] += n;
//         }
//       }
//     }
//   }
//
//   // generic function that takes in a function as argument
//   map(func)
//   {
//     for(let i=0; i<this.rows; i++)
//     {
//       for(let j=0; j<this.columns; j++)
//       {
//         let val = this.data[i][j];
//         // val is manipulated and then reassigned to i,j position
//         this.data[i][j] = func(val);
//       }
//     }
//     return this;
//   }
//
//   static map(matrix, func)
//   {
//     let result = new Matrix(matrix.rows, matrix.columns);
//     for(let i=0; i<matrix.rows; i++)
//     {
//       for(let j=0; j<matrix.columns; j++)
//       {
//         let val = matrix.data[i][j];
//         result.data[i][j] = func(val);
//       }
//     }
//     return result;
//   }
//   // prints the data in this class
//   print()
//   {
//     console.table(this.data);
//     return this;
//   }
//
//   // static method
//   // matrix * matrix = https://en.wikipedia.org/wiki/Matrix_multiplication
//   static multiply(a, b)
//   {
//     if(a instanceof Matrix && b instanceof Matrix)
//     {
//       // matrix product
//       if (a.columns !== b.rows)
//       {
//         console.log("columns of a must match rows of b");
//         return undefined;
//       }
//       let result = new Matrix(a.rows, b.columns);
//       for (let i=0; i<result.rows; i++)
//       {
//         for(let j=0; j<result.columns; j++)
//         {
//           let sum = 0;
//           // dot product of this.row and n.columns
//           // a[i][j] * b[i][j] +
//           // a[i][j+k] * b[i][j+1] +
//           // a[i][j+k] * b[i][j+2]
//           for (let k=0; k<a.columns; k++)
//           {
//             sum += a.data[i][k] * b.data[k][j];
//           }
//           result.data[i][j] = sum;
//         }
//       }
//       return result;
//     }
//   }
//
//   static transpose(m)
//   {
//     let result = new Matrix(m.columns, m.rows);
//     for (let i=0; i<m.rows; i++)
//     {
//       for(let j=0; j<m.columns; j++)
//       {
//         //                    has to be [i][j]
//         //because iteration is through this.rows, and this.columns
//         result.data[j][i] = m.data[i][j];
//       }
//     }
//     return result;
//   }
//
//   // converts an input array into a Matrix object
//   static fromArray(array)
//   {
//     // row: num elements in array, col: 1
//     let m = new Matrix(array.length, 1);
//     for(let i=0; i<array.length; i++)
//     {
//       m.data[i][0] = array[i];
//     }
//     return m;
//   }
//
//   // converts n,1 matrix to array
//   toArray()
//   {
//     let arr = [];
//     for (let i=0; i<this.rows; i++)
//     {
//       for(let j=0; j<this.columns; j++)
//       {
//         arr.push(this.data[i][j]);
//       }
//     }
//     return arr;
//   }
//
//   // return new matrix a - b
//   static subtract(a, b)
//   {
//     if(a.rows !== b.rows || a.columns !== b.columns)
//     {
//       console.log("columns and rows of a must match columns and rows of b")
//       return;
//     }
//     let result = new Matrix(a.rows, a.columns);
//     for(let i=0; i<result.rows; i++)
//     {
//       for (let j=0; j<result.columns; j++)
//       {
//         result.data[i][j] = a.data[i][j] - b.data[i][j];
//       }
//     }
//     return result;
//   }
// }
