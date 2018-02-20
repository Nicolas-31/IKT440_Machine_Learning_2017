Learning Automata Assignment

Requirements:

    All of the following points are required to pass the automated test for the Learning Automata assignment.

    1. The proposed solution for the assignment must be written in python, with the file name 'learningautomata.py'

       * Note: You can use multiple python files (i.e "Environment.py") if needed, however the required method (see below)
               must be in the required file ('learningautomata.py').
               Furthermore, all files need to be placed in a folder named 'LearningAutomata'

    2. A method named 'run_simulation()', is required. 
       The method must take three values as arguments. The first will be the number of states your simulation shall use
       for the Environment. The second argument will be the target number of sensors that should be active. The last 
       argument will be the total number of sensors that should be created.
       
       Example test:
       'run_simulation(states=5, target=7, total=10)'
       
       Furthermore, the method is required to return a list, containing the number of nodes that are 'active' for each iteration.
       
    * Note: The test is time limited, if this limit is exceeded the the accuracy of the given 
            run will be set to 0%. We recommend that the simulation should run no more than 10 000 iterations. 1000 should be more than enough.

            There is a pass percentage for the bamboo test. Failing to achieve an higher persentage does not necessarily 
            mean that the assingment is not passed, it is just an 'expected' limit to achieve.

Structure of the expected deliveries:

    |-LearningAutomata
    |--learningautomata.py
        |---> run_simulation(integer: number_of_states, target_sensors, total_sensors) -> list
        |---> etc
    |-- *.py
