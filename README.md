
# U.S. Public Holidays 2025 – PySpark Data Processing  

## Overview  
This project fetches, processes, and stores public holiday data for the United States in 2025 using **PySpark** and the [Nager.Date API](https://date.nager.at/). The data is transformed for easy analysis and stored as a **Parquet file** in an **Amazon S3 bucket**.  

## Data Workflow  

1️⃣ **Data Extraction**  
- Retrieved public holiday data from `https://date.nager.at/api/v3/PublicHolidays/2025/US` using `requests`.  
- Extracted holiday details including `date`, `localName`, `name`, and `fixed`.  

2️⃣ **Data Processing (PySpark)**  
- Loaded JSON response into a **Spark DataFrame**.  
- Extracted `year` and `month` from `date` for better analysis.  
- Cleaned and validated data to remove inconsistencies.  

3️⃣ **Data Storage**  
- Transformed data is stored as a **Parquet file** in an **S3 bucket**.  


