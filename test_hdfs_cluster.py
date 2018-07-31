from pyhdfs import *

client = HdfsClient(hosts="47.93.45.238,9000",user_name="hadoop",timeout=5)

response = client.open("/user/hadoop/test.csv")

print response.read()