import xml.etree.cElementTree as ET
from BroadworksOCIP.broadworks.schema.request.base import OCIRequest

class UserGetListInGroupRequest(OCIRequest):

    def __init__(self, serviceproviderid=None, groupid=None):
        self.command_name = "UserGetListInGroupRequest"
        self.node_name = "command"
        self.serviceprovider = serviceproviderid
        self.group = groupid
        self.create_command_root()

    def _export(self):
        root = ET.Element(self.node_name)
        root.set("xmlns:xsi", "http://www.w3.org/2001/XMLSchema-instance")
        root.set("xsi:type", self.command_name)
        ET.SubElement(root, "serviceProviderId").text = self.serviceprovider
        ET.SubElement(root, "GroupId").text = self.group
        return ET.tostring(root)


class Test:
    pass