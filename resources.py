from config import S3_BUCKET, S3_KEY, S3_SECRET
import boto3
from flask import session

def aws_bucket_info():
    if S3_KEY and S3_SECRET:
        s3_resource = boto3.resource('s3',aws_access_key_id=S3_KEY,aws_secret_access_key=S3_SECRET)
    else:
        s3_resource = boto3.resource('s3')
    if 'bucket' in session:
        bucket = session['bucket']
    else:
        bucket = S3_BUCKET
    my_bucket = s3_resource.Bucket(bucket)
    return my_bucket

def get_bucket_list():
    client = boto3.client('s3')
    return client.list_buckets().get('Buckets')