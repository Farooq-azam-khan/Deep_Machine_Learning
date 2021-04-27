import numpy as np
from math import sqrt
import matplotlib.pyplot as plt
from matplotlib import style
from collections import Counter
style.use("fivethirtyeight")

# key are the colors which we will classify to on graph
dataset = {'k':[[1,2], [2,3], [3,1]], 'r':[[6,5], [7,7], [8,6]]}
# our predcition feature
new_features = [5,7]

# KNN algorithm
def k_nearest_neighbors(data, predict, k=3):
    if len(data)>=k:
        warnings.warn("K is set to value less than total voting groups")

    distances = []
    for group in data: # getting the color
        for features in data[group]: # getting the 2d-list
            # Eucildean distance (higher dimensions and faster)
            euclidean_distance = np.linalg.norm(np.array(features)-np.array(predict))
            distances.append([euclidean_distance, group])
            
    votes = [i[1] for i in sorted(distances)[:k]]
    vote_result = Counter(votes).most_common(1)[0][0]
    
    return vote_result

def main():
    result = k_nearest_neighbors(dataset, new_features)

    '''
    for i in dataset:
        for ii in dataset[i]:
            plt.scatter(ii[0],ii[1], s=100, color=i)
    '''
    [ [ plt.scatter(ii[0],ii[1], s=100, color=i) for ii in dataset[i]] for i in dataset]
    plt.scatter(new_features[0], new_features[1], color=result)
    plt.show()

    # TODO: Euclidean distance, manhattan distance, minkowski distance, hamming distance


if __name__ == '__main__':
    main()