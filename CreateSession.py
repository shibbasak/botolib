import os
import boto3
from datetime import datetime, timedelta
import json

session = boto3.Session(profile_name='default')
#dev_s3_client = session.client('s3',region_name='us-east-1')
glue_job = session.client('glue',region_name='us-east-1')


response = glue_job.start_job_run(
               JobName = 'xxx',
               Arguments = {
                 '--some_key':   'Some Value'} )

print(json.dumps(response, indent=4, sort_keys=True, default=str))
