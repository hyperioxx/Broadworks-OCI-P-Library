from BroadworksOCIP.broadworks.schema.request.base import OCIRequest

class ServiceProviderGetListRequest(OCIRequest):

    def __init__(self, is_enterprise=False, serviceprovider=None):
        self.command_name = "ServiceProviderGetListRequest"
        self.node_name = "command"
        self.isenterprise = isEnterprise
        self.response_size = 100
        self.search = None
        self.serviceprovider = serviceprovider
        self.create_command_root()

    def _export(self):
        root = ET.Element(self.node_name)
        root.set("xmlns:xsi","http://www.w3.org/2001/XMLSchema-instance")
        root.set("xsi:type", self.command_name)
        if self.userId:
            ET.SubElement(root,"userId").text = self.userId
        return ET.tostring(root)




class SearchCriteriaServiceProviderId(OCIRequest):

    def __init__(self, is_enterprise=False, serviceprovider=None):
        self.command_name = "AuthenticationRequest"
        self.node_name = "command"

    def _export(self):
        root = ET.Element(self.node_name)
        root.set("xmlns:xsi","http://www.w3.org/2001/XMLSchema-instance")
        root.set("xsi:type", self.command_name)
        if not self.userId:
            ET.SubElement(root,"userId").text = self.userId
        return ET.tostring(root)


class SearchCriteriaServiceProviderName:
    pass
