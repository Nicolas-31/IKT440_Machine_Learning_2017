import network
import pgm_trainingdata_loader as nnloader
import pickle


net = network.Network([960, 400, 200, 60, 4])
(training_data, validation_data, verification_data) = nnloader.load_data()

net.SGD(training_data, 60, 10, 0.1, test_data=validation_data)


print("dont run")
with open('weights_biases.pickle', 'wb') as p:
    pickle.dump([net.weights, net.biases], p, protocol=pickle.HIGHEST_PROTOCOL)


'''
with open('weights_biases.pickle', 'rb') as p:
    (w, b) = pickle.load(p)
net.loadInitData(w, b)
test_results = net.evaluate(validation_data)
print(test_results)
for data in verification_data:
    result = net.feedforward(data)
    print(result)
'''