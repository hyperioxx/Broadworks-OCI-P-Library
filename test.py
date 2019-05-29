from zeep import Client
from BroadworksOCIP.login import AuthenticationRequest

client = Client('http://bw.com/webservice/services'
                '/ProvisioningService?wsdl')
x = AuthenticationRequest(userId="blah@test.com")
#print("".join(str(x).split("\n")))

client.settings(extra_http_headers= {"JSESSION"})
print(client.service.processOCIMessage("".join(str(x).split("\n"))))
#print(client.service.processOCIMessage(y))
