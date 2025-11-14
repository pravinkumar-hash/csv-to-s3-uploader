import boto3
from botocore.exceptions import NoCredentialsError

BUCKET_NAME = "pravin-csv-upload-project"   
FILE_PATH = "sample.csv"                    
S3_FILE_NAME = "uploaded-sample.csv"        

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
