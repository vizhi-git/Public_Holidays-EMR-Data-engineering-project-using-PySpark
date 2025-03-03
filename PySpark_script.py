import requests
import json
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, year, month, when

# Initialize Spark Session
spark = SparkSession.builder.appName("PublicHolidaysAnalysis").getOrCreate()

# Fetch Data from API
url = "https://date.nager.at/api/v3/PublicHolidays/2025/US"
response = requests.get(url)

if response.status_code == 200:
    holidays_data = response.json()
else:
    print(f"Failed to retrieve data: {response.status_code}")
    holidays_data = []

# Convert JSON to PySpark DataFrame
holidays_df = spark.createDataFrame(holidays_data)

# Select Relevant Columns
df_holidays = holidays_df.select(["date", "localName", "name", "countryCode", "fixed", "global", "counties", "launchYear"])

# Extract Year and Month from Date
df_holidays = df_holidays.withColumn("year", year(col("date")))
df_holidays = df_holidays.withColumn("month_num", month(col("date")))

# Map Month Number to Month Name
df_holidays = df_holidays.withColumn(
    "month",
    when(col("month_num") == 1, "January")
    .when(col("month_num") == 2, "February")
    .when(col("month_num") == 3, "March")
    .when(col("month_num") == 4, "April")
    .when(col("month_num") == 5, "May")
    .when(col("month_num") == 6, "June")
    .when(col("month_num") == 7, "July")
    .when(col("month_num") == 8, "August")
    .when(col("month_num") == 9, "September")
    .when(col("month_num") == 10, "October")
    .when(col("month_num") == 11, "November")
    .when(col("month_num") == 12, "December")
)

# Drop Unnecessary Columns
df_holidays = df_holidays.drop("month_num")

# Handle Null Values
df_holidays = df_holidays.na.fill({"counties": "N/A", "launchYear": 0})

# Show Sample Data
df_holidays.show(5)

# Save to S3
s3_path = "s3://public-holidays-data-us-2025/holidays.parquet"
df_holidays.write.mode("overwrite").parquet(s3_path)

