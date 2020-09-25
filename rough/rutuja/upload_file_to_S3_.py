
import boto3
from botocore.exceptions import NoCredentialsError

ACCESS_KEY = 'AKIAQJ7HRZ3USL7TURBO'
SECRET_KEY = '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'

def upload_to_aws(local_file, bucket,bucket_folder ,dest_file_name):
    s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY,
                      aws_secret_access_key=SECRET_KEY)

    try:
        s3.upload_file(local_file, bucket, '%s/%s' % (bucket_folder,dest_file_name))
        print("Upload Successful")
        return True
    except FileNotFoundError:
        print("The file was not found")
        return False
    except NoCredentialsError:
        print("Credentials not available")
        return False


#uploaded = upload_to_aws('C:\\Users\\SAI\\PycharmProjects\\pythonProject\\rutuja.student_record.json', 'bpa-rg-rough', 'devs/rutuja','rutuja_test.py')