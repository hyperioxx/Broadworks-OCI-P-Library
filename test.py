from zeep import Client
from BroadworksOCIP.broadworks.schema.base import BroadsoftDocument
from BroadworksOCIP.broadworks.schema.login import AuthenticationRequest

x = BroadsoftDocument(protocol="OCI", sessionId="123154323456543")
y = AuthenticationRequest(userId="aaron.parfitt@thevoicefactory.co.uk")

x.add_command(y)
print(x)

client = Client("http://api.thevoicefactory.co.uk/webservice/services/ProvisioningService?wsdl")

client.service.processOCIMessage(x)


