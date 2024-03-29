# %% [markdown]
# ## Data discovery: Load and query Yellow Taxi data
# > Download the dataset from [the official TLC Trip Record Data website](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page)
from pyspark.sql import SparkSession

# %%
# Create SparkSession
spark = SparkSession.builder\
             .master("local[1]")\
             .appName("spark-app-version-x")\
             .getOrCreate()

# %%
# Read taxi data. These can be input parameters, using python arguments.
input_path = '/home/sasa/Downloads/Code/spark_jobs/production_data/yellow_taxis'
output_path = '/home/sasa/Downloads/Code/spark_jobs/reporting/etl_job_taxis_multi_passanger_trips/'


# %%
# Load data into Spark dataframe
df = spark.read.parquet(input_path)

# %%
# Query sample, using Spark SQL
df.createOrReplaceTempView('tbl_raw_yellow_taxis')

# %%
# SQL Statement
df_output = spark.sql('''
                        SELECT *
                        FROM tbl_raw_yellow_taxis 
                        ''')

# %%
# Write data to output
df_output.write.mode('overwrite').parquet(output_path)

# %%
# Stop the session
spark.stop()
#Two output files are generated one is _SUCCESS and "part-00000-3866e57f-4764-4e1c-9905-1f039eb9577c-c000.snappy.parquet"


