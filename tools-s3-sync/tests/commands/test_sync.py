import boto3
from moto 
import mock_s3
from snovak.commands import sync

@mock_s3
def setup_test_bucket():
    mockedS3Resource = boto3.resource("s3", region_name="us-east-1")
    # Add files to the bucket
    file_contents = "This is a test file."
    file_names = ['file1.txt', 'file2.txt', 'file3.txt']
    for file_name in file_names:
        conn.Object(bucket_name, file_name).put(Body=file_contents)

    return mockedS3Resource

@mock_s3
def test_my_model_save():
    mockedS3Resource = setup_test_bucket()
    sync()
