import xml.etree.cElementTree as ET
from BroadworksOCIP.broadworks.schema.request.base import OCIRequest
from BroadworksOCIP.broadworks.errors import RequiredField

class SystemRoutingGetRequest(OCIRequest):

    def __init__(self):
        self.command_name = "SystemRoutingGetRequest"
        self.node_name = "command"
        self.create_command_root()

    def _export(self):
        return ET.tostring(self.root)


class SystemSoftwareVersionGetRequest(OCIRequest):

    def __init__(self):
        self.command_name = "SystemSoftwareVersionGetRequest"
        self.node_name = "command"
        self.create_command_root()

    def _export(self):
        return ET.tostring(self.root)


class SystemCodecGetListRequest(OCIRequest):

    def __init__(self):
        self.command_name = "SystemCodecGetListRequest"
        self.node_name = "command"
        self.create_command_root()

    def _export(self):
        return ET.tostring(self.root)



class SystemAccessDeviceCustomTagGetListRequest(OCIRequest):

    def __init__(self, device_name):
        self.command_name = "SystemAccessDeviceCustomTagGetListRequest"
        self.node_name = "command"
        self.create_command_root()
        self.device_name = device_name

    def _export(self):
        ET.SubElement(self.root,"deviceName").text = self.device_name
        return ET.tostring(self.root)


class SystemAccessDeviceCustomTagModifyRequest(OCIRequest):

    def __init__(self, device_name, tag_name, tag_value):
        self.command_name = "SystemAccessDeviceCustomTagModifyRequest"
        self.node_name = "command"
        self.create_command_root()
        self.device_name = device_name
        self.tag_name = tag_name
        self.tag_value = tag_value


    def _export(self):
        ET.SubElement(self.root,"deviceName").text = self.device_name
        ET.SubElement(self.root, "tagName").text = self.tag_name
        ET.SubElement(self.root, "tagValue").text = self.tag_value
        return ET.tostring(self.root)




