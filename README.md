
# U.S. Public Holidays 2025 – PySpark Data Processing  

## Overview  
This project retrieves, processes, and stores the public holiday data for the United States in 2025. The data is fetched from the Nager.Date API and is processed using PySpark. After transforming the data into a structured format for easy analysis, it is stored as a Parquet file in an Amazon S3 bucket for efficient access and future processing. 

## Data Workflow
### 1.Data Extraction
API Source: The data is fetched from the Nager.Date API via the endpoint:
https://date.nager.at/api/v3/PublicHolidays/2025/US using the requests Python library.

Extracted Data: The API provides the following details for each public holiday:

date: The actual date of the holiday (e.g., "2025-01-01")
localName: The local name of the holiday in the respective language.
name: The official name of the holiday (e.g., "New Year's Day").
fixed: A boolean indicating whether the holiday occurs on a fixed date every year.
###2. Data Processing (PySpark)
Loading Data into Spark: The JSON data received from the API is loaded into a PySpark DataFrame. This allows for distributed data processing and transformation, making the analysis scalable.

### Data Transformation:

Date Parsing: The date field is parsed to extract the year and month to support better time-based analysis and filtering.
Data Cleaning: Any missing or inconsistent data (e.g., missing holiday names or invalid date formats) is handled to ensure the dataset is complete and accurate.
Data Structuring: The data is transformed into a clean, structured format that is easier to query and analyze later. This includes renaming columns and handling any special cases for holidays that may require custom processing.
### 3.Data Storage
Output Format: The final dataset, after processing, is stored in the Parquet format, which is highly optimized for big data processing.

Storage in S3: The Parquet file is uploaded to an Amazon S3 bucket, where it can be accessed by other applications or analyzed further using tools like AWS Athena or PySpark.

## Technologies Used

PySpark: Distributed computing framework for processing large datasets efficiently.

Amazon S3: Cloud storage service used to store the processed data in Parquet format.

Nager.Date API: Provides public holiday data for various countries, including the United States in 2025.

Requests: Python library used to make HTTP requests to the Nager.Date API.

Parquet: A columnar storage file format optimized for big data processing.  

## Prerequisites

Python 3.x installed on your machine.

PySpark and other required libraries.

Access to an Amazon S3 bucket for storing the output data.



