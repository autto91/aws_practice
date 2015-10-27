#!/usr/bin/python
import boto.ec2
from keyfile import *

conn = boto.ec2.connect_to_region('us-west-2',
    aws_access_key_id = key_id,
    aws_secret_access_key = secret_key)


web = conn.create_security_group('websrv', 'webserver group')
web.authorize('tcp', 80, 80, '0.0.0.0/0')
web.authorize(ip_protocol = 'tcp', from_port = 22, to_port = 22, cidr_ip = '0.0.0.0/16')

app = conn.create_security_group('appserver', 'application servers')
app.authorize(src_group=web)
