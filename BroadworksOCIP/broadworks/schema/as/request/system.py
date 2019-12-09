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
