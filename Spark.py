
# setup arguments
# Use this command for excution 'spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.10:2.3.0'
# Don't change anything in the above command because i get my result by this same command after a long struggle
#spark_version = '3.2.1'

# import Libraries
from pyspark.sql import SparkSession
from pyspark.sql.functions import *

if __name__ == '__main__':
	
	# building spark session
    spark = SparkSession.builder.master("local[*]").appName("myApp").getOrCreate()
    df = spark.readStream.format("kafka").option("kafka.bootstrap.servers", "127.0.0.1:9092").option("subscribe","test").option("startingOffsets","earlist").load()

    personStringDF = df.selectExpr("CAST(value AS STRING)")

    PersonDf= personStringDF.select(split(col("value"), ","). getItem(0).alias("ID"))
    # Define your own schema according to your csv file(As below in example). In my case, i have only two columns in my test csv.

    # schema = new StructType()
      .add("id",IntegerType)
      .add("firstname",StringType)
      .add("middlename",StringType)
      .add("lastname",StringType)
      .add("dob_year",IntegerType)
      .add("dob_month",IntegerType)
      .add("gender",StringType)
      .add("salary",IntegerType)

    
    PersonDf.writeStream.format("console").outputMode("append").start().awaitTermination()
