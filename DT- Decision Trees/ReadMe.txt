Decision Tree / Random Forests Assignment

Requirements:

    All of the following points are required to pass the automated test for the Decision Tree assignment.

    1. The proposed solution for the assignment must be written in python 3, with the file name being 'decisiontrees.py'. 

       * Note: You can use multiple python files (i.e 'config.py') if needed, but the required methods (mentioned below) must be
         in the required file 'decisiontrees.py'. Furthermore, all files need to be in a folder named 'DecisionTrees'

    2. A build forest method, named 'build_forest()', is required. It must take a list as input, the list contains all
       rows from the training data set. It should return a single integer, which is the number
       of trees that were created in the forest.

       * Note: The test is time limited, if the limit is exceeded the test will fail.

    3. A method named predict() is required. This method must take a list as input, the list contains data from a hidden dataset,
       but the true labels are replaced with "-1". The method is required to return
       a list containing the predicted true labels (i.e I, M, F, M, M, F, ...), the predicted labels should contain
       the same amount of elements as the input list.

    * Note: The two tests will be run independantly, and all data will be lost between the tests. In order to pass, the classifier(s)
      need to be saved. For instance, build_forest() saves its classifier using pickle. predict() will then read this classifier.
    
      There is also a pass percentage of an accuracy above 33% for the bamboo test. Failing to achieve an higher
      persentage does not necessarily mean that the assingment is not passed, it is just an 'expected' 
      limit to achieve.
      
      |-DecisionTrees
      |--decisiontrees.py
          |---> build_forest(list) -> int : number_of_trees
          |---> predict(list) -> list : predictions
          |---> etc
      |-- *.py

Abalone data set:

    The training part of the data set is available for download (downloads/training_data.zip). Note that the data is a CSV file.
    
    * Note: Do not upload the data set to bamboo, only upload the python files. 

    Attribute information:

       The Sex of Abalone the  is the value to predict

        Name		Data Type	Meas.	Description
	----		---------	-----	-----------
	Sex		nominal			M, F, and I (infant)
	Length		continuous	mm	Longest shell measurement
	Diameter	continuous	mm	perpendicular to length
	Height		continuous	mm	with meat in shell
	Whole weight	continuous	grams	whole abalone
	Shucked weight	continuous	grams	weight of meat
	Viscera weight	continuous	grams	gut weight (after bleeding)
	Shell weight	continuous	grams	after being dried
	Rings		integer			+1.5 gives the age in years

   	Statistics for numeric domains:

		Length	Diam	Height	Whole	Shucked	Viscera	Shell	Rings
	Min	0.075	0.055	0.000	0.002	0.001	0.001	0.002	    1
	Max	0.815	0.650	1.130	2.826	1.488	0.760	1.005	   29
	Mean	0.524	0.408	0.140	0.829	0.359	0.181	0.239	9.934
	SD	0.120	0.099	0.042	0.490	0.222	0.110	0.139	3.224

    The Class distribution can be found below. Note that is represents the total number of males, females, and infants. 
    That is, there are 1528 Males in the entire dataset, however, only 80% of the dataset is given for training. 
    The remaining 20% is hidden and will be used for the tests. The datasets were shuffled, before splitting. 
    
        Class   Samples (training data / test data)
        -----   -------
        M       1528 (1208 / 320)
        F       1307 (1077 / 230)
        I       1342 (1056 / 286)
        
        

HINT:
    
    * You may choose to either use a single tree for classification, or build a random forest. 
    	* A random forest consists of many decision trees. For more information watch this video: https://www.youtube.com/watch?v=loNcrMjYh64
    
    * You do not need to use all of the features when building your tree. For instance, using 3 features may give a better result than if you
      were to use all features. How many and which features that are "best" is up to you to decide
      
    * Grouping the data may help :)

        
NB: VERY IMPORTANT!
  If you want to use 'exec(classifier)' inside the 'predict()' function, you need to 
  add the 'globals()' dictionary as a parameter to 'exec()', i.e 'exec(classifier, globals())'
  

