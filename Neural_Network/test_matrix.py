import unittest

from matrix import Matrix
class TestMatrixClass(unittest.TestCase):
    
    def test_rows(self):
        mat = Matrix(2, 2)
        self.assertEqual(mat.rows, 2)
        
    def test_cols(self):
        mat = Matrix(2,2)
        self.assertEqual(mat.cols, 2)
    
    def test_data(self):
        mat = Matrix(2,2)
        self.assertEqual(mat.data, [[0, 0], [0,0]])
        
    def test_fromArray(self):
        mat = Matrix.fromArray([0, 0, 0])
        self.assertEqual(mat.rows, 3)
        self.assertEqual(mat.cols, 1)
        self.assertEqual(mat.data, [[0], [0], [0]])
        
    def test_subtract0(self):
        mat_a = Matrix(2,2)
        mat_a.map(lambda x: x+1)
        mat_b = Matrix(2,2)
        mat_b.map(lambda x: x+1)
        result = Matrix.subtract(mat_a, mat_b)
        self.assertEqual(result.data, [[0, 0], [0, 0]])
        
    def test_subtract1(self):
        mat_a = Matrix(2,2)
        mat_a.map(lambda x: x+1)
        mat_b = Matrix(3,2)
        mat_b.map(lambda x: x+1)
        result = Matrix.subtract(mat_a, mat_b)
        self.assertNotIsInstance(type(result), Matrix)
        
    def test_toArray(self):
        mat = Matrix(2,2)
        mat.map(lambda x: x+1)
        arr = mat.toArray()
        self.assertEqual(arr, [1, 1, 1, 1])
        
    def test_add_elementwise(self):
        mat_a = Matrix(2,2)
        mat_b = Matrix(2,2)
        mat_a.map(lambda x: x+1)
        mat_b.map(lambda x: x+2)
        
        mat_ret = mat_a.add(mat_b)
        self.assertEqual(mat_ret.rows, 2)
        self.assertEqual(mat_ret.cols, 2)
        self.assertEqual(mat_ret.data, [[3,3], [3,3]])
    
    def test_add_None(self):
        mat_a = Matrix(2,2)
        mat_b = Matrix(3,2)
        mat_a.map(lambda x: x+1)
        mat_b.map(lambda x: x+2)
        mat_ret_none = mat_a.add(mat_b)
                
        self.assertNotIsInstance(type(mat_ret_none), Matrix)
    
    def test_add_scalar(self):
        mat = Matrix(2,2)
        mat.map(lambda x: x+1)
        mat_ret = mat.add(2)
        
        self.assertEqual(mat_ret.rows, 2)
        self.assertEqual(mat_ret.cols, 2)
        self.assertEqual(mat_ret.data, [[3,3], [3,3]])
        
    def test_transpose(self):
        mat = Matrix(3,2)
        mat_tranposed = Matrix.transpose(mat)
        self.assertEqual(mat_tranposed.rows, 2)
        self.assertEqual(mat_tranposed.cols, 3)
    
    def test_softmax(self):
        mat = Matrix(3, 1).randomize()
        softmax_mat = Matrix.softmax(mat)
        arr = softmax_mat.toArray()
        self.assertEqual(sum(arr), 1.0)
        
        

if __name__ == '__main__':
    unittest.main()