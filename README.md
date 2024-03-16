# pyspark_Series
Data Description:
The TLC (Taxi and Limousine Commission) Trip Record Data refers to a dataset that
contains detailed information about taxi trips in New York City. This dataset is made
available by the TLC, which regulates and oversees the taxi and for-hire vehicle industry
in the city.
The TLC Trip Record Data includes various attributes for each taxi trip, such as the
pickup and drop-off locations, trip distance, trip duration, fare amount, payment type,
and additional surcharges. It also provides information about the taxi's unique identifier,
driver details, and other relevant trip-related information.
Analyzing the TLC Trip Record Data typically involves processing and cleaning the
dataset, performing exploratory data analysis, and applying various statistical and
machine learning techniques to derive meaningful insights. The large volume and
complexity of the dataset often require tools and frameworks like PySpark or Apache
Spark for efficient data processing and analysis.

## Running the Code on Interactive Shell

1. Once the lab is spun up, open a terminal window.

2. To execute the code on an interactive pyspark shell, we need to login to Spark docker container. Execute following command on terminal to do the same.

 ```docker exec -i -t hdp_spark-master bash```

3. Once we are inside the Spark container, execute following command to launch a pyspark shell.

 ```./spark/bin/pyspark```

4. Once the shell is launced, navigate into Project folder on Desktop, for getting the commands to run in the interactive shell.

## Running the Code on JupyterLab 
1. Once the lab is spun up, open a terminal window.

2. To run the code in jupyterlab we need to copy the data and code files to the jupyterlab's docker container. Execute following command on the terminal to do the same.

```docker cp /home/user/Project/pyspark_basics  hdp_jupyterlab:/opt/workspace/```

3. Open Chrome browser to launch an instance of jupyterlab. Type following in the address bar and press enter.
```localhost:4888/```

5. Click on the Data folder on the left panel, and navigate to the folder where all the data and code files are present.

6. Execute the code as instructed in the project videos.
