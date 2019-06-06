import xml.etree.ElementTree as ET
from BroadworksOCIP.broadworks.schema.response.base import Contact, StreetAddress

class ServiceProviderGetListResponse:
    def __init__(self, oci_response):
        self.xml = oci_response
        tree = ET.fromstring(oci_response)
        self.sp_array = []
        try:
            for serviceprovider in tree.find("command").find("serviceProviderTable").findall("row"):
                sp_info = serviceprovider.findall("col")
                self.sp_array.append(ServiceProviderResult(sp_id=sp_info[0].text, sp_name=sp_info[1].text,is_ent=sp_info[2].text))
        except AttributeError:
            print("asdasd")

    def get_search_result(self):
        return self.sp_array



class ServiceProviderGetResponse17sp1:

    def __init__(self, oci_response):
        self.xml = oci_response
        tree = ET.fromstring(oci_response)
        self.is_ent = None
        self.custom_route = None
        self.default_domain = None
        self.serviceprovider_name = None
        self.support_email = None
        self.contact = None
        self.address = None
        try:
            self.is_ent = tree.find("command").find("isEnterprise").text
        except AttributeError:
            pass
        try:
            self.custom_route = tree.find("command").find("useCustomRoutingProfile").text
        except AttributeError:
            pass
        try:
            self.default_domain = tree.find("command").find("defaultDomain").text
        except AttributeError:
            pass
        try:
            self.serviceprovider_name = tree.find("command").find("serviceProviderName").text
        except AttributeError:
            pass
        try:
            self.support_email = tree.find("command").find("supportEmail").text
        except AttributeError:
            pass
        try:
            self.contact = Contact(tree.find("command").find("contact").tostring())
        except AttributeError:
            pass
        try:
            self.address = StreetAddress(tree.find("command").find("address").tostring())
        except AttributeError as err:
            print(err)


    def get_is_ent(self):
        return self.is_ent

    def get_custom_route(self):
        return self.custom_route

    def get_default_domain(self):
        return self.default_domain

    def serviceprovider_name(self):
        return self.serviceprovider_name

    def get_support_email(self):
        return self.support_email

    def get_contact(self):
        return self.contact

    def get_address(self):
        return self.address








class ServiceProviderResult:

    def __init__(self, sp_id, sp_name, is_ent):
        self.sp_id = sp_id
        self.sp_name = sp_name
        self.is_ent = is_ent

    def get_serviceprovider_id(self):
        return self.sp_id

    def get_serviceprovider_name(self):
        return self.sp_name

    def get_is_ent(self):
        return self.is_ent