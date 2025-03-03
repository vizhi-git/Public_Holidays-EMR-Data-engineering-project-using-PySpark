
# U.S. Public Holidays 2025 – PySpark Data Processing  

## Overview  
This project retrieves, processes, and stores the public holiday data for the United States in 2025. The data is fetched from the Nager.Date API and is processed using PySpark. After transforming the data into a structured format for easy analysis, it is stored as a Parquet file in an Amazon S3 bucket for efficient access and future processing.This project demonstrates how to use Amazon EMR (Elastic MapReduce) to process big data using PySpark. The project walks through the process of setting up Amazon EMR clusters, creating a VPC (Virtual Private Cloud), using Amazon EMR Studio and JupyterLab, and writing PySpark code in Jupyter notebooks to extract, process, and load data into an S3 bucket.


### In this project, we will:

- Create a VPC (Virtual Private Cloud) to isolate and secure resources.
  
- Provision an EMR cluster within the VPC.
  
- Set up Amazon EMR Studio with JupyterLab for interactive development and execution of PySpark code.
  
- Attach Jupyter notebooks to the provisioned EMR cluster.
  
- Write PySpark code to extract data from a data source, process it, and transform it into a Parquet file.
  
- Load the processed data into an S3 bucket for further analysis or storage.
  
## Key Concepts and Technologies Used

Amazon EMR (Elastic MapReduce): A cloud-native big data platform that simplifies running big data frameworks like Apache Spark and Hadoop.

Apache Spark: A powerful, fast, and general-purpose distributed computing system that is highly suitable for data processing and analytics.

Amazon VPC: A Virtual Private Cloud that provides an isolated network for your AWS resources.

Amazon S3: A scalable object storage service to store data files.

PySpark: Python API for Apache Spark that allows us to write Spark applications in Python.

JupyterLab: An interactive web-based notebook that allows us to write and execute Python code interactively.

### Prerequisites

- An AWS account with the necessary permissions to create resources like EMR clusters, VPCs, and S3 buckets.
  
- Basic understanding of Apache Spark and PySpark for big data processing.
  
- Amazon S3 bucket to store processed data.
  
- JupyterLab environment in Amazon EMR Studio.
  
### Setup Instructions
1. Set up a VPC
Start by creating a VPC (Virtual Private Cloud) to isolate the resources we will provision for EMR. This can be done through the AWS Console or using CloudFormation templates.

2. Create an Amazon EMR Cluster
-Open the Amazon EMR Console and select "Create Cluster."
-Choose Apache Spark as the framework for processing your data.
-Configure the EMR cluster with the necessary instance types, instance count, and configure networking to use the previously created VPC.
-Provision the cluster and wait for it to initialize.

3. Set up Amazon EMR Studio and JupyterLab
-Create Amazon EMR Studio using the AWS console.
-Set up JupyterLab within EMR Studio. This environment will allow us to write PySpark code interactively.
-Attach our Jupyter notebook to the EMR cluster we just created.

4. Write PySpark Code in JupyterLab

- Extract Data: Write PySpark code to connect to data source (whether it is a database or file) and extract the necessary data.

- Process the Data: Use PySpark transformations to clean, filter, or aggregate the data as needed.

- Save Data to S3: Once the data is processed, save the transformed data as a Parquet file and load it into your Amazon S3 bucket.



