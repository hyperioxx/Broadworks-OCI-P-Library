from BroadworksOCIP import Client
from BroadworksOCIP.broadworks.schema.request.group import GroupDeviceTypeCustomTagGetListRequest, GroupDeviceTypeCustomTagAddRequest, GroupDeviceTypeCustomTagDeleteListRequest

client = Client(username="username", password="password", address="https://api.broadsoft.com/webservice/services/ProvisioningService")

client.login() 


x1 = GroupDeviceTypeCustomTagGetListRequest("serviceproviderID", "GroupID", "Polycom VVX 600")
response = client.send(x1)
print(response.get_tags())


x2 = GroupDeviceTypeCustomTagAddRequest('serviceproviderID', 'GroupID', "Polycom VVX 600", '%ffdffd%', "TEST")

response = client.send(x2)
print(response)

x4 = GroupDeviceTypeCustomTagGetListRequest("serviceproviderID", "GroupID", "Polycom VVX 600")
response = client.send(x4)

print(response.get_tags())



x3 = GroupDeviceTypeCustomTagDeleteListRequest('serviceproviderID', 'GroupID', "Polycom VVX 600", '%ffdffd%')


response = client.send(x3)
print(response)


