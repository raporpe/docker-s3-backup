from distutils.command.upload import upload
import shutil
import time
import boto3
import os


print("Starting backup")
# Create a zip of the backup directory
file_name = "backup-" + time.strftime("%Y-%m-%d-%H-%M-%S")
file_name_full = file_name + ".zip"
shutil.make_archive(file_name, 'zip', "/backup")

# If the access key and secret key env variables are not set, then exit
if os.environ.get('ACCESS_KEY_ID') is None \
    or os.environ.get('SECRET_ACCESS_KEY') is None \
    or os.environ.get('BUCKET') is None:
    print("You must set ACCESS_KEY_ID, SECRET_ACCESS_KEY and BUCKET environment variables")
    exit(1)

access_key_id = os.environ['ACCESS_KEY_ID']
secret_access_key = os.environ['SECRET_ACCESS_KEY']
bucket = os.environ['BUCKET']

# If the endpoint is not set, set default aws s3 endpoint
if not os.environ.get('ENDPOINT_URL'):
    os.environ['ENDPOINT_URL'] = 'https://s3.amazonaws.com'
    
endpoint_url = os.environ['ENDPOINT_URL']

print("Uploading to S3")
s3 = boto3.resource('s3',
    endpoint_url=endpoint_url, 
    aws_access_key_id=access_key_id, 
    aws_secret_access_key=secret_access_key
)

# Set the bucket
b = s3.Bucket(bucket)
# Upload the file
b.upload_file(file_name_full, file_name_full)
        
print("Upload Successful")

print("Deleting local backup")

# Delete the zip file
os.remove(file_name_full)

print("All done!")
