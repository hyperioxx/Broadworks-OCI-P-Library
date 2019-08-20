import xml.etree.cElementTree as ET
from BroadworksOCIP.broadworks.schema.request.base import OCIRequest
from BroadworksOCIP.broadworks.errors import RequiredField

class ServiceProviderGetListRequest(OCIRequest):

    def __init__(self, is_enterprise=False, serviceprovider=None):
        self.command_name = "ServiceProviderGetListRequest"
        self.node_name = "command"
        if is_enterprise == False:
            self.isenterprise = "false"
        else:
            self.isenterprise = "true"
        self.response_size = 100
        self.search = SearchCriteriaServiceProviderId(value=serviceprovider)
        self.serviceprovider = serviceprovider
        self.create_command_root()

        #todo: add ability to modify SearchCriteriaServiceProviderId

    def _export(self):
        root = ET.Element(self.node_name)
        root.set("xmlns:xsi","http://www.w3.org/2001/XMLSchema-instance")
        root.set("xsi:type", self.command_name)
        ET.SubElement(root,"isEnterprise").text = self.isenterprise
        ET.SubElement(root, "responseSizeLimit").text = str(self.response_size)
        root.append(ET.fromstring(str(self.search)))
        return ET.tostring(root)



class ServiceProviderGetRequest17sp1(OCIRequest):
    """
    Get the profile for a service provider or enterprise. The response is either a ServiceProviderGetResponse17sp1 or an ErrorResponse.
    """

    def __init__(self, serviceproviderid=None):
        if not serviceproviderid:
            raise RequiredField("missing required field: serviceproviderid")
        self.command_name = "ServiceProviderGetRequest17sp1"
        self.node_name = "command"
        self.serviceprovider = serviceproviderid
        self.create_command_root()



    def _export(self):
        root = ET.Element(self.node_name)
        root.set("xmlns:xsi","http://www.w3.org/2001/XMLSchema-instance")
        root.set("xsi:type", self.command_name)
        ET.SubElement(root,"serviceProviderId").text = self.serviceprovider
        return ET.tostring(root)





class ServiceProviderAddRequest13mp2(OCIRequest):

    def __init__(self, is_ent=False, serviceproviderid=None, routing_profile=False, default_domain=None, serviceprovider_name=None, support_email=None):
        if not serviceproviderid:
            raise RequiredField("missing required field: serviceproviderid")
        self.command_name = "ServiceProviderGetRequest17sp1"
        self.node_name = "command"
        self.is_ent = is_ent
        self.routing_profile = routing_profile
        self.serviceprovider = serviceproviderid
        self.default_domain = default_domain
        self.serviceprovider_name = serviceprovider_name
        self.support_email = support_email
        self.contact = None
        self.address = None
        self.create_command_root()



    def _export(self):
        root = ET.Element(self.node_name)
        root.set("xmlns:xsi","http://www.w3.org/2001/XMLSchema-instance")
        root.set("xsi:type", self.command_name)
        ET.SubElement(root,"serviceProviderId").text = self.serviceprovider
        return ET.tostring(root)



class ServiceProviderDomainGetAssignedListRequest(OCIRequest):
    def __init__(self, serviceproviderid=None):
        if not serviceproviderid:
            raise RequiredField("missing required field: serviceproviderid")
        self.command_name = "ServiceProviderDomainGetAssignedListRequest"
        self.node_name = "command"
        self.serviceprovider = serviceproviderid
        self.create_command_root()



    def _export(self):
        root = ET.Element(self.node_name)
        root.set("xmlns:xsi","http://www.w3.org/2001/XMLSchema-instance")
        root.set("xsi:type", self.command_name)
        ET.SubElement(root,"serviceProviderId").text = self.serviceprovider
        return ET.tostring(root)








class SearchCriteriaServiceProviderId(OCIRequest):

    def __init__(self, mode="Starts With", value=None, case_insensitive=True):
        self.node_name = "searchCriteriaServiceProviderId"
        self.mode = mode
        self.value = value
        if case_insensitive:
            self.case_insensitive = "true"
        else:
            self.case_insensitive = "false"

    def _export(self):
        root = ET.Element(self.node_name)
        #root.set("xmlns:xsi","http://www.w3.org/2001/XMLSchema-instance")
        ET.SubElement(root,"mode").text = self.mode
        ET.SubElement(root, "value").text = self.value
        ET.SubElement(root,"isCaseInsensitive").text = self.case_insensitive
        return ET.tostring(root)


class SearchCriteriaServiceProviderName:
    pass



