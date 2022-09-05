# Spark Streaming with Kafka in-python
We'll create a simple application in Java using Spark which will integrate with the Kafka topic we created earlier. The application will read the messages as posted and count the frequency of words in every message

# Code Explanition
Before Going to Spark streaming, You will need to make sure your kafka Producer is running. If you dont know about kafka consumer and producer check my profile i listed it in a separate repository " https://github.com/majid0110/Kafka-Producer-and-consumers-using-python "

Now you will Need to add defendecies Listed as below :
 Use this command : spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.11:2.3.0 (Your_code_with_location like C:\Users\soft_\Desktop\Spark.py)    
     <groupId>org.apache.spark</groupId>
     <artifactId>spark-sql-kafka-0-10_2.10</artifactI
     <version>2.3.0</version>
 
 # Spark Session
 Spark Streaming uses readStream() on SparkSession to load a streaming Dataset from Kafka.
 ![image](https://user-images.githubusercontent.com/81530072/188498685-5cd1a76d-c5fe-4629-beda-48fa4f7da848.png)

Since the value is in binary, first we need to convert the binary value to String using selectExpr()
![image](https://user-images.githubusercontent.com/81530072/188498803-e5214b6f-b5e3-4847-8619-0ec0f5331eb8.png)

# Defining Schema
Now, extract the value which is in JSON String to DataFrame and convert to DataFrame columns using custom schema.
![image](https://user-images.githubusercontent.com/81530072/188499270-dcdc3997-7752-4de2-aa2b-9979daa7a728.png)

These are the basics of spark streaming with kafka, Now look at the out below:
# Output
![image](https://user-images.githubusercontent.com/81530072/188499385-6292f87e-028f-4483-98da-5fdacc87e4db.png)

The output will be based on your CSV, In my case I have only two columns in my CSV file.

After this you will need to store data in hiveDB for performing SQL Querries.

# Note:
you can run this code on cross environments like on local Machine and Sandbox-HDP.hortonworks but you will need to change your ip and host according to your platform.

if you have any qurried regarding this code, feel free to contact me at ' majidse0110@gmail.com '

