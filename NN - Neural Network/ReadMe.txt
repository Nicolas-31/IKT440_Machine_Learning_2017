Neural Network Assignment

Task:

  Configure a neural network to recognize face directions (left, right, straight, up) as described in the lecture slides. 
  The dataset can be found in 'training_data.zip'.


Resources:

    Recommended: 
    Read chapter one of Neural Networks and Deep Learning and extract the python code for back-propogation neural network. 
    Link: http://neuralnetworksanddeeplearning.com/chap1.html

    Optional: 
    Use Tensorflow (CPU) for building/training your model. We recommend the above method 
    as it gives you a better and deeper understanding of how neural networks work.


Requirements:

    All of the following points are required to pass the automated test for the Learning Automata assignment.

    1. The proposed solution for the assignment must be written in python, with the file name 'neuralnetworks.py'

        * Note: You can use multiple python files (i.e "model.py") if needed, however the required method (see below)
                must be in the required file ('neuralnetworks.py').
                Furthermore, all files need to be placed in a folder named 'NeuralNetworks'

    2. A method named 'predict()', is required. The method must take in one argument which will be a folder where the test files are located.
    Furthermore, the method is required to return a dictionary where the key is the name of the file, and the value your prediction.
 
    Example output:
       
          {'name_of_file_1' : 'up', 'name_of_file_2' : 'left', etc}
       
    * NOTE The test will NOT train your model, as it is too intensive and takes a long time. Therefore, you should upload already trained weights and biases to update your model. 
    That is, train at home, save the weights and biases (to a file) when you are satisfied and upload them with the model. Use these weights and biases when predicting.



