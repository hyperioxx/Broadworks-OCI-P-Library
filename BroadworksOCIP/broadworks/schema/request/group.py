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



class GroupDnGetListRequest(OCIRequest):

    def __init__(self, serviceproviderid=None, groupid=None):
        self.command_name = "GroupDnGetListRequest"
        self.node_name = "command"
        self.serviceprovider = serviceproviderid
        self.group = groupid
        self.create_command_root()


    def _export(self):
        root = ET.Element(self.node_name)
        root.set("xmlns:xsi", "http://www.w3.org/2001/XMLSchema-instance")
        root.set("xsi:type", self.command_name)
        ET.SubElement(root, "serviceProviderId").text = self.serviceprovider
        ET.SubElement(root, "groupId").text = self.group
        return ET.tostring(root)


class GroupGetRequest14sp7(OCIRequest):

    def __init__(self, serviceproviderid=None, groupid=None):
        self.command_name = "GroupGetRequest14sp7"
        self.node_name = "command"
        self.serviceprovider = serviceproviderid
        self.group = groupid
        self.create_command_root()


    def _export(self):
        root = ET.Element(self.node_name)
        root.set("xmlns:xsi", "http://www.w3.org/2001/XMLSchema-instance")
        root.set("xsi:type", self.command_name)
        ET.SubElement(root, "serviceProviderId").text = self.serviceprovider
        ET.SubElement(root, "groupId").text = self.group
        return ET.tostring(root)


class GroupDomainGetAssignedListRequest(OCIRequest):

    def __init__(self, serviceproviderid=None, groupid=None):
        self.command_name = "GroupDomainGetAssignedListRequest"
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



class GroupAddRequest(OCIRequest):
    #todo: add full options
    def __init__(self, serviceproviderid=None, groupid=None, domain=None, group_name=None,
                 clid=None, email=None, user_limit=None):
        self.command_name = "GroupAddRequest"
        self.node_name = "command"
        self.serviceprovider = serviceproviderid
        self.group = groupid
        self.group_name = group_name
        self.domain = domain
        self.clid = clid
        self.email = email
        self.user_limit = user_limit
        self.create_command_root()


    def _export(self):
        root = ET.Element(self.node_name)
        root.set("xmlns:xsi", "http://www.w3.org/2001/XMLSchema-instance")
        root.set("xsi:type", self.command_name)
        ET.SubElement(root, "serviceProviderId").text = self.serviceprovider
        ET.SubElement(root, "groupId").text = self.group
        ET.SubElement(root, "defaultDomain").text = self.domain
        ET.SubElement(root, "userLimit").text = self.user_limit
        if self.clid:
            ET.SubElement(root, "groupName").text = self.group_name
        if self.clid:
            ET.SubElement(root, "callingLineIdName").text = self.clid

        return ET.tostring(root)

class GroupServiceAssignListRequest(OCIRequest):
    def __init__(self, serviceproviderid=None, groupid=None, service_name=None):
        self.command_name = "GroupServiceAssignListRequest"
        self.node_name = "command"
        self.serviceprovider = serviceproviderid
        self.group = groupid
        self.service_name = service_name
        self.create_command_root()


    def _export(self):
        root = ET.Element(self.node_name)
        root.set("xmlns:xsi", "http://www.w3.org/2001/XMLSchema-instance")
        root.set("xsi:type", self.command_name)
        ET.SubElement(root, "serviceProviderId").text = self.serviceprovider
        ET.SubElement(root, "groupId").text = self.group
        ET.SubElement(root, "serviceName").text = self.service_name
        return ET.tostring(root)

class GroupServiceUnassignListRequest(OCIRequest):
    def __init__(self, serviceproviderid=None, groupid=None, service_name=None):
        self.command_name = "GroupServiceUnassignListRequest"
        self.node_name = "command"
        self.serviceprovider = serviceproviderid
        self.group = groupid
        self.service_name = service_name
        self.create_command_root()


    def _export(self):
        root = ET.Element(self.node_name)
        root.set("xmlns:xsi", "http://www.w3.org/2001/XMLSchema-instance")
        root.set("xsi:type", self.command_name)
        ET.SubElement(root, "serviceProviderId").text = self.serviceprovider
        ET.SubElement(root, "groupId").text = self.group
        ET.SubElement(root, "serviceName").text = self.service_name
        return ET.tostring(root)

class GroupDeleteRequest(OCIRequest):
    def __init__(self, serviceproviderid=None, groupid=None):
        self.command_name = "GroupDeleteRequest"
        self.node_name = "command"
        self.serviceprovider = serviceproviderid
        self.group = groupid
        self.create_command_root()

    def _export(self):
        root = ET.Element(self.node_name)
        root.set("xmlns:xsi", "http://www.w3.org/2001/XMLSchema-instance")
        root.set("xsi:type", self.command_name)
        ET.SubElement(root, "serviceProviderId").text = self.serviceprovider
        ET.SubElement(root, "groupId").text = self.group
        return ET.tostring(root)


class GroupDnAssignListRequest(OCIRequest):
    def __init__(self, serviceproviderid=None, groupid=None, dn=None, dn_range=None):
        self.command_name = "GroupDnAssignListRequest"
        self.node_name = "command"
        self.serviceprovider = serviceproviderid
        self.group = groupid
        self.dn = dn
        self.dn_range = dn_range
        self.create_command_root()

    def _export(self):
        root = ET.Element(self.node_name)
        root.set("xmlns:xsi", "http://www.w3.org/2001/XMLSchema-instance")
        root.set("xsi:type", self.command_name)
        ET.SubElement(root, "serviceProviderId").text = self.serviceprovider
        ET.SubElement(root, "groupId").text = self.group
        if self.dn:
            ET.SubElement(root, "phoneNumber").text = self.group
        if self.dn_range:
            ET.SubElement(root, "groupId").text = self.group
        return ET.tostring(root)


class GroupDnUnassignListRequest(OCIRequest):
    def __init__(self, serviceproviderid=None, groupid=None, dn=None, dn_range=None):
        self.command_name = "GroupDnUnassignListRequest"
        self.node_name = "command"
        self.serviceprovider = serviceproviderid
        self.group = groupid
        self.dn = dn
        self.dn_range = dn_range
        self.create_command_root()

    def _export(self):
        root = ET.Element(self.node_name)
        root.set("xmlns:xsi", "http://www.w3.org/2001/XMLSchema-instance")
        root.set("xsi:type", self.command_name)
        ET.SubElement(root, "serviceProviderId").text = self.serviceprovider
        ET.SubElement(root, "groupId").text = self.group
        if self.dn:
            ET.SubElement(root, "phoneNumber").text = self.group
        if self.dn_range:
            ET.SubElement(root, "groupId").text = self.group
        return ET.tostring(root)


class GroupDnGetAvailableListRequest(OCIRequest):
    def __init__(self, serviceproviderid=None, groupid=None):
        self.command_name = "GroupDnGetAvailableListRequest"
        self.node_name = "command"
        self.serviceprovider = serviceproviderid
        self.group = groupid
        self.create_command_root()

    def _export(self):
        root = ET.Element(self.node_name)
        root.set("xmlns:xsi", "http://www.w3.org/2001/XMLSchema-instance")
        root.set("xsi:type", self.command_name)
        ET.SubElement(root, "serviceProviderId").text = self.serviceprovider
        ET.SubElement(root, "groupId").text = self.group
        return ET.tostring(root)


class GroupVoiceMessagingGroupGetRequest(OCIRequest):
    def __init__(self, serviceproviderid=None, groupid=None):
        self.command_name = "GroupVoiceMessagingGroupGetRequest"
        self.node_name = "command"
        self.serviceprovider = serviceproviderid
        self.group = groupid
        self.create_command_root()

    def _export(self):
        root = ET.Element(self.node_name)
        root.set("xmlns:xsi", "http://www.w3.org/2001/XMLSchema-instance")
        root.set("xsi:type", self.command_name)
        ET.SubElement(root, "serviceProviderId").text = self.serviceprovider
        ET.SubElement(root, "groupId").text = self.group
        return ET.tostring(root)



class Test:
    pass