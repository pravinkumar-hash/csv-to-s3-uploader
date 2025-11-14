import boto3
from botocore.exceptions import NoCredentialsError

# AWS credentials → DO NOT TYPE DIRECTLY INSIDE CODE
# Configure them using AWS CLI or environment variables

BUCKET_NAME = "pravin-csv-upload-project"   # Your bucket name
FILE_PATH = "sample.csv"                    # Local file
S3_FILE_NAME = "uploaded-sample.csv"        # File name in S3

def upload_to_aws(local_file, bucket, s3_file):
    s3 = boto3.client('s3')

    try:
        s3.upload_file(local_file, bucket, s3_file)
        print("Upload Successful! ✔")
        return True
    except FileNotFoundError:
        print("The file was not found ")
        return False
    except NoCredentialsError:
        print("Credentials not available ")
        return False

uploaded = upload_to_aws(FILE_PATH, BUCKET_NAME, S3_FILE_NAME)

if uploaded:
    print("Your CSV file is now in S3!")
