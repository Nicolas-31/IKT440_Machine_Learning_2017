import network
import pgm_trainingdata_loader as nnloader
import pickle
import numpy as np


def sigmoid(z):
    np.seterr(all='ignore')
    return 1.0/(1.0+np.exp(-z))


def feedforward(a, we, bi):
    for b, w in zip(bi, we):
        a = sigmoid(np.dot(w, a)+b)
    return a

def dir_result(result):
    if result == 0:
        return 'left'
    if result == 1:
        return 'right'
    if result == 2:
        return 'up'
    if result == 3:
        return 'straight'

#
#
# Example output: {'name_of_file_1' : 'up', 'name_of_file_2' : 'left', etc}
def predict(testfilepath):

    verification_data = nnloader.load_verification_bamboo(testfilepath)
    with open('weights_biases.pickle', 'rb') as p:
        (w, b) = pickle.load(p)

    prediction_dict = {}
    for (data, filename) in verification_data:
        elements = feedforward(data, w, b)
        resultIndex = np.argmax(elements)
        prediction_dict[filename] = dir_result(resultIndex)
    return prediction_dict


#res = predict("../../data/nntraining_data/")
#print(res)