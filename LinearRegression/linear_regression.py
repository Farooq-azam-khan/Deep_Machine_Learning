def mean(arr):
    sum = 0
    for val in arr:
        sum+=val
    return sum / len(arr)

def multiply_list(list1, list2):
    if len(list1) == len(list2):
        mul_list = []
        for l1, l2 in zip(list1, list2):
            mul_list.append(l1*l2)
        return mul_list
    else:
        print("length of list does not match")
        return [0]
        
def squared_error(prediction_ys, original_ys):
    if len(prediction_ys) == len(original_ys):
        diff_squared = []
        for prediction_y, origin_y in zip(prediction_ys, original_ys):
            diff_squared.append((prediction_y-origin_y)**2)
        return sum(diff_squared)
    else:
        print("lengths of arrays for prediction and actual values did not match.")
    
class LinearRegression():
    def __init__(self):
        self.m = 0
        self.b = 0    
    
    def get_best_fit(self, xs, ys):
        numerator   = mean(xs) * mean(ys) - mean( multiply_list(xs,ys) )
        denominator = mean(xs) * mean(xs) - mean( multiply_list(xs,xs) )
        self.m =  numerator / denominator
        self.b = mean(ys) - self.m * mean(xs)
        
    def fit(self, xs, ys):
        self.get_best_fit(xs, ys)
        return self.m, self.b
        
    def predict(self, x):
        return self.m * x + self.b
        
    def predictions(self, xs):
        preds = []
        for x in xs:
            preds.append(self.predict(x))
        return preds
        
    # coeeficient of determination
    def score(self, ys_orig, ys_line):
        print("Coefficinet of Determination")
        y_mean_line = [mean(ys_orig) for y in ys_orig]
        
        # get the error for the actual line
        squared_error_regression    = squared_error(ys_orig, ys_line)
        # get the error for the predicted line
        squared_error_mean          = squared_error(ys_orig, y_mean_line)
        
        return 1 - (squared_error_regression / squared_error_mean)
        
        
        