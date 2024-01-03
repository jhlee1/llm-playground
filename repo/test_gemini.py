import asyncio
import logging

import pytest
from google.cloud import aiplatform
from google.oauth2 import service_account
from pyspark.sql import SparkSession
from pyspark.sql import Row

# test_add.py
from .gemini import code_generation

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


@pytest.fixture
def setup_cred():
    credentials = service_account.Credentials.from_service_account_file('joohanlee-playground-d64f38409fea.json')
    aiplatform.init(
        project="joohanlee-playground",
        location="us-central1",
        credentials=credentials,
        service_account="vertex-api-user@joohanlee-playground.iam.gserviceaccount.com",
    )


def test_code_generation(setup_cred):
    result = asyncio.run(code_generation(text="Can you make a code to use oauth in python?"))

def test_code_generation_with_schema(setup_cred):
    # Initialize a SparkSession
    spark = SparkSession.builder \
        .appName("Example") \
        .getOrCreate()

    # Sample data
    data = [Row(name="Alice", age=25), Row(name="Bob", age=30), Row(name="Charlie", age=35)]

    # Create a DataFrame
    df = spark.createDataFrame(data)

    # Show the DataFrame
    schema_json = df.schema.json()
    result = asyncio.run(code_generation(text="Can you use a pyspark dataframe to get the average age based on this schema in json:" + schema_json))
    # result = asyncio.run(code_generation(
    #     text="Can you create a spark SQL to get the average age based on this schema described in json:" + schema_json))
    print(result.text)


