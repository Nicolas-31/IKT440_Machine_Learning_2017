Naive Bayes Assignment

// NEW
    As some of you may be aware, there have been a few errors in the test which should now be fixed. 
    Read below for any new notes or modifications.
    
  	- Some of the files may have specific characters which will result in a "UnicodeDecodeError". In order to bypass this
    	  use the 'codecs' library to open a file. An example can be seen below:
    	
        	with codecs.open(path, "r", encoding="utf-8", errors="ignore") as f:
        		data = f.readlines()
	
	- As the test is time-sensitive it is important to optimize your code as much as possible. Remember that lookups in python
          are much faster using dictionaries/sets than lists (constant lookup vs linear lookup). I recommend you store the stop_words 
          and other similar files in a set. Below is a set-comprehension that can be used as an example:
          
        	with open("stop_words.txt", "r") as f:
        		stop_words = {word.strip() for word in f.readlines()}
            
          Read more: https://wiki.python.org/moin/TimeComplexity
            
        - A fast way to count the number of occurences of a word in a list/set etc is by using the "Counter" collection in python
        
        	from collection import Counter
            
        	# words = ["hello", "world", "some", "other", "random", "words", ..., "hello"] 
        	word_count = Counter(words)
            
          Read more: https://docs.python.org/2/library/collections.html#collections.Counter
            
    
Requirements:

    All of the following points are required to pass the automated test for the Naive Bayes assignment.

    1. The proposed solution must be written in python 3, with the file name 'naivebayes.py'

       Note: It is allowed to have multiple python files, such as a config file or dataloader. However, the required method must
             be available. Furthermore, all files need to be placed in a folder named 'NaiveBayes'

	// MODIFIED. IMPORTANT!
    2. A method named 'classify_documents()', is required. The method has two input arguments, training data folder
       and testing data folder. The method is required to return a dictionary. The key will be the name of the file (name only, not path),
       and the value will be your corresponding prediction for that given file. For instance, 'file_name_1' : 'misc.forsale'.
       You can get the name of all files in a directory by using "os.listdir(path_to_directory)"
       Also, the prediction has to be the exact same as the categories below. Any typos will result in a failure. 

       Note: Both inputs are strings to directories/folders only. Therefore you have to read all files in that folder. The training data
       containins sub-folders which needs to be handled. The name of the folder is the subject that needs to be classified. The testing 
       data does not contain any folders. Each file needs to be classified and a dictionary should be returned. 


    Note: The test is time limited to 5 minutes, exceeding this limit will fail the test. Furthermore, the length of
    list containing the predictions needs to be the same as the number of files in the testing folder (2000 files)


Structure of deliveries:

    |-NaiveBayes
    |--naivebayes.py
        |---> classify_documents(string: training_folder, string: testing_folder) -> dict
    |--*.py
    



Data Information:

    The training data contains file form 20 different subjects (classes). Each of the subject has 900
    different files, with the exception 'soc.religion.christian' which contains only 897.

    The testing data contains 2000 files randomly chosen between the subject, the target is to predict these.

    The categories are as followed (which also are the folder names in the training data):

        1.  alt.atheism
        2.  comp.graphics
        3.  comp.os.ms-windows.misc
        4.  comp.sys.ibm.pc.hardware
        5.  comp.sys.mac.hardware
        6.  comp.windows.x
        7.  misc.forsale
        8.  rec.autos
        9.  rec.motorcycles
        10. rec.sport.baseball
        11. rec.sport.hockey
        12. sci.crypt
        13. sci.electronics
        14. sci.med
        15. sci.space
        16. soc.religion.christian
        17. talk.politics.guns
        18. talk.politics.mideast
        19. talk.politics.misc
        20. talk.religion.misc

    Note: These all the given files (training and testing) contains a header, which should be removed. This
          pre-processing should be handled by the students.
          Furthermore, in addition to the training data, a list of stopwords are available in the download zip, which
          you may use if you want.


NB: DO NOT UPLOAD THE DATA TO YOUR GIT REPOSITORY. THEY WILL BE AVAILBE FOR THE TEST.
