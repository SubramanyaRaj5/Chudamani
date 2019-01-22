import boto3

ec2=boto3.resource('ec2')

instance_id='i-0837712bae72e34db'
instance=ec2.Instance(instance_id)
response=instance.terminate()
print(response)
