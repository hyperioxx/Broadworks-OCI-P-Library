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



class GroupDeviceTypeCustomTagGetListRequest(OCIRequest):

    def __init__(self, serviceproviderid, groupid, deviceType):
        self.command_name = "GroupDeviceTypeCustomTagGetListRequest"
        self.node_name = "command"
        self.create_command_root()
        self.serviceproviderid = serviceproviderid
        self.groupid = groupid
        self.deviceType = deviceType

    def _export(self):
        root = ET.Element(self.node_name)
        root.set("xmlns:xsi", "http://www.w3.org/2001/XMLSchema-instance")
        root.set("xsi:type", self.command_name)
        ET.SubElement(self.root, "serviceProviderId").text = self.serviceproviderid
        ET.SubElement(self.root, "groupId").text = self.groupid
        ET.SubElement(self.root,"deviceType").text = self.deviceType
        return ET.tostring(self.root)



class GroupDeviceTypeCustomTagModifyRequest(OCIRequest):

    def __init__(self, serviceproviderid, groupid, deviceType, tagName, tagValue):
        self.command_name = "GroupDeviceTypeCustomTagModifyRequest"
        self.node_name = "command"
        self.create_command_root()
        self.serviceproviderid = serviceproviderid
        self.groupid = groupid
        self.deviceType = deviceType
        self.tagName = tagName
        self.tagValue = tagValue

    def _export(self):
        root = ET.Element(self.node_name)
        root.set("xmlns:xsi", "http://www.w3.org/2001/XMLSchema-instance")
        root.set("xsi:type", self.command_name)
        ET.SubElement(self.root, "serviceProviderId").text = self.serviceproviderid
        ET.SubElement(self.root, "groupId").text = self.groupid
        ET.SubElement(self.root,"deviceType").text = self.deviceType
        ET.SubElement(self.root,"tagName").text = self.tagName
        ET.SubElement(self.root,"tagValue").text = self.tagValue
        return ET.tostring(self.root)



class GroupDeviceTypeCustomTagAddRequest(OCIRequest):

    def __init__(self, serviceproviderid, groupid, deviceType, tagName, tagValue):
        self.command_name = "GroupDeviceTypeCustomTagAddRequest"
        self.node_name = "command"
        self.create_command_root()
        self.serviceproviderid = serviceproviderid
        self.groupid = groupid
        self.deviceType = deviceType
        self.tagName = tagName
        self.tagValue = tagValue

    def _export(self):
        root = ET.Element(self.node_name)
        root.set("xmlns:xsi", "http://www.w3.org/2001/XMLSchema-instance")
        root.set("xsi:type", self.command_name)
        ET.SubElement(self.root, "serviceProviderId").text = self.serviceproviderid
        ET.SubElement(self.root, "groupId").text = self.groupid
        ET.SubElement(self.root,"deviceType").text = self.deviceType
        ET.SubElement(self.root,"tagName").text = self.tagName
        ET.SubElement(self.root,"tagValue").text = self.tagValue
        return ET.tostring(self.root)


class GroupDeviceTypeCustomTagDeleteListRequest(OCIRequest):

    def __init__(self, serviceproviderid, groupid, deviceType, tagName):
        self.command_name = "GroupDeviceTypeCustomTagDeleteListRequest"
        self.node_name = "command"
        self.create_command_root()
        self.serviceproviderid = serviceproviderid
        self.groupid = groupid
        self.deviceType = deviceType
        self.tagName = tagName

    def _export(self):
        root = ET.Element(self.node_name)
        root.set("xmlns:xsi", "http://www.w3.org/2001/XMLSchema-instance")
        root.set("xsi:type", self.command_name)
        ET.SubElement(self.root, "serviceProviderId").text = self.serviceproviderid
        ET.SubElement(self.root, "groupId").text = self.groupid
        ET.SubElement(self.root,"deviceType").text = self.deviceType
        if isinstance(self.tagName, list):
            for tag in self.tagName:
                ET.SubElement(self.root,"tagName").text = tag
        else:
            ET.SubElement(self.root,"tagName").text = self.tagName
        return ET.tostring(self.root)


class GroupDeviceTypeFileGetListRequest14sp8(OCIRequest):

    def __init__(self, serviceproviderid, groupid, deviceType):
        self.command_name = "GroupDeviceTypeFileGetListRequest14sp8"
        self.node_name = "command"
        self.create_command_root()
        self.serviceproviderid = serviceproviderid
        self.groupid = groupid
        self.deviceType = deviceType


    def _export(self):
        root = ET.Element(self.node_name)
        root.set("xmlns:xsi", "http://www.w3.org/2001/XMLSchema-instance")
        root.set("xsi:type", self.command_name)
        ET.SubElement(self.root, "serviceProviderId").text = self.serviceproviderid
        ET.SubElement(self.root, "groupId").text = self.groupid
        ET.SubElement(self.root,"deviceType").text = self.deviceType
        return ET.tostring(self.root)


class GroupDeviceTypeFileGetRequest16sp1(OCIRequest):

    def __init__(self, serviceproviderid, groupid, deviceType, fileFormat):
        self.command_name = "GroupDeviceTypeFileGetRequest16sp1"
        self.node_name = "command"
        self.create_command_root()
        self.serviceproviderid = serviceproviderid
        self.groupid = groupid
        self.deviceType = deviceType
        self.file_format = fileFormat

    def _export(self):
        root = ET.Element(self.node_name)
        root.set("xmlns:xsi", "http://www.w3.org/2001/XMLSchema-instance")
        root.set("xsi:type", self.command_name)
        ET.SubElement(self.root, "serviceProviderId").text = self.serviceproviderid
        ET.SubElement(self.root, "groupId").text = self.groupid
        ET.SubElement(self.root,"deviceType").text = self.deviceType
        ET.SubElement(self.root,"fileFormat").text = self.file_format
        return ET.tostring(self.root)


class GroupDeviceTypeFileModifyRequest14sp8(OCIRequest):

    def __init__(self, serviceproviderid, groupid, deviceType, fileFormat, enconf='Default'):
        #todo: file upload feature
        self.command_name = "GroupDeviceTypeFileModifyRequest14sp8"
        self.node_name = "command"
        self.create_command_root()
        self.serviceproviderid = serviceproviderid
        self.groupid = groupid
        self.deviceType = deviceType
        self.file_format = fileFormat
        self.enconf = enconf


    def _export(self):
        root = ET.Element(self.node_name)
        root.set("xmlns:xsi", "http://www.w3.org/2001/XMLSchema-instance")
        root.set("xsi:type", self.command_name)
        ET.SubElement(self.root, "serviceProviderId").text = self.serviceproviderid
        ET.SubElement(self.root, "groupId").text = self.groupid
        ET.SubElement(self.root,"deviceType").text = self.deviceType
        ET.SubElement(self.root,"fileFormat").text = self.file_format
        ET.SubElement(self.root,"fileSource").text = self.enconf
        return ET.tostring(self.root)



        
class GroupCPEConfigRebuildConfigFileRequest(OCIRequest):

    def __init__(self,serviceproviderid, groupid, deviceType, force=False):
        self.command_name = "GroupCPEConfigRebuildConfigFileRequest"
        self.node_name = "command"
        self.create_command_root()
        self.serviceproviderid = serviceproviderid
        self.groupid = groupid
        self.deviceType = deviceType
        if force:
            self.force = 'true'
        else:
            self.force = 'false'

    def _export(self):
        root = ET.Element(self.node_name)
        root.set("xmlns:xsi", "http://www.w3.org/2001/XMLSchema-instance")
        root.set("xsi:type", self.command_name)
        ET.SubElement(self.root, "serviceProviderId").text = self.serviceproviderid
        ET.SubElement(self.root, "groupId").text = self.groupid
        ET.SubElement(self.root,"deviceType").text = self.deviceType
        ET.SubElement(self.root,"fileFormat").text = self.file_format
        ET.SubElement(self.root,"force").text = self.force
        return ET.tostring(self.root)





class Test:
    pass