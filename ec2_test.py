#!/usr/bin/python
import boto.ec2
import sys
from keyfile import key_id, secret_key

conn = boto.ec2.connect_to_region('us-west-2',
    aws_access_key_id = key_id,
    aws_secret_access_key = secret_key)

rs = conn.get_all_security_groups()

print rs
