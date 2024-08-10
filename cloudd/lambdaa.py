import boto3
import botocore

import random

def random_drink():
    drink= ['coddee', 'tea', 'colddrink']
    return random.choice(drink)

print(random_drink())

def lambda_handler(event, context):
   print(f'boto3 version: {boto3.__version__}')
   print(f'botocore version: {botocore.__version__}')

if __name__=='__main__':
    lambda_handler('fd', 'test')