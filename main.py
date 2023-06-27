import boto3, os
# Access the AWS access keys from environment variables
aws_access_key_id = os.environ.get('AKIA5CDXV56QWROL5CNJ')
aws_secret_access_key = os.environ.get('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')
aws_region = os.environ.get('us-west-2')
session = boto3.Session(
aws_access_key_id=aws_access_key_id,
aws_secret_access_key=aws_secret_access_key,
region_name=aws_region # Replace with your desired AWS region
)
#adding this for testing purpose


def list_s3_buckets():
    s3_client = session.client('s3')
    response = s3_client.list_buckets()
    buckets = [bucket['Name'] for bucket in response['Buckets']]
    print(f"S3 Buckets: {buckets}")
if __name__ == '__main__':
    list_s3_buckets()