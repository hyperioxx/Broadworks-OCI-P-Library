import xml.etree.cElementTree as ET
from BroadworksOCIP.broadworks.schema.request.base import OCIRequest



class GroupGetListInServiceProviderRequest(OCIRequest):

    def __init__(self, serviceproviderid=None):
        self.command_name = "GroupGetListInServiceProviderRequest"
        self.node_name = "command"
        self.response_size = 100
        self.serviceprovider = serviceproviderid
        self.create_command_root()


    def _export(self):
        root = ET.Element(self.node_name)
        root.set("xmlns:xsi", "http://www.w3.org/2001/XMLSchema-instance")
        root.set("xsi:type", self.command_name)
        ET.SubElement(root, "serviceProviderId").text = self.serviceprovider
        ET.SubElement(root, "responseSizeLimit").text = str(self.response_size)
        return ET.tostring(root)



class Test:
    pass