import boto3

s3 = boto3.client('s3')

buckets = s3.list_buckets()
print("Buckets:")
for bucket in buckets['Buckets']:
    print(f"- {bucket['Name']}")

bucket_name = 'natwestassignment'
s3_resource = boto3.resource('s3')
bucket = s3_resource.Bucket(bucket_name)
object_count = sum(1 for _ in bucket.objects.all())
print(f"Total objects in {bucket_name}: {object_count}")
