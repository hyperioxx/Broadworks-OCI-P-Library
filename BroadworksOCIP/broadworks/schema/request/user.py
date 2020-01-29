import xml.etree.cElementTree as ET
from BroadworksOCIP.broadworks.errors import RequiredField
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


class UserGetRequest22V5(OCIRequest):
    """ Request to get the user information.
        The response is either UserGetResponse22V5
        or ErrorResponse. """

    def __init__(self, userId=None):
        self.command_name = "UserGetRequest22V5"
        self.node_name = "command"
        self.userId = userId
        self.create_command_root()

    def _export(self):
        root = ET.Element(self.node_name)
        root.set("xmlns:xsi", "http://www.w3.org/2001/XMLSchema-instance")
        root.set("xsi:type", self.command_name)
        ET.SubElement(root, "userId").text = self.userId
        return ET.tostring(root)


class UserVoiceMessagingUserModifyVoicePortalRequest20(OCIRequest):

    def __init__(self, userid=None, usepersonalizedname=None,
                 auto_login=None, personalizednameaudiofile=None):
        self.command_name = "UserVoiceMessagingUserModifyVoicePortalRequest20"
        self.node_name = "command"
        self.userid = userid
        self.usepersonalizedname = usepersonalizedname
        self.auto_login = auto_login
        self.personalizednameaudiofile = personalizednameaudiofile
        self.create_command_root()

    def _export(self):
        root = ET.Element(self.node_name)
        root.set("xmlns:xsi", "http://www.w3.org/2001/XMLSchema-instance")
        root.set("xsi:type", self.command_name)
        if not self.userid:
            raise RequiredField("userId is a required field")
        ET.SubElement(root, "userId").text = self.userid
        if self.usepersonalizedname:
            ET.SubElement(
                root, "usePersonalizedName").text = self.usepersonalizedname
        if self.auto_login == False:
            ET.SubElement(root, "voicePortalAutoLogin").text = "false"
        else:
            ET.SubElement(root, "voicePortalAutoLogin").text = "true"
        if self.personalizednameaudiofile:
            ET.SubElement(
                root, "personalizedNameAudioFile").text = self.personalizednameaudiofile
        return ET.tostring(root)


class UserAddRequest22(OCIRequest):
    """ Request to add a user.
        The domain is required in the userId.
        The password is not required if external authentication is enabled.

        Mandatory Parameters:

        serviceProviderId
        groupId
        userId
        lastName
        firstName
        callingLineIdLastName
        callingLineIdFirstName

        properties: Optional parameters may be provided in form of a dictionary.

        The response is either SuccessResponse or ErrorResponse.
    """

    def __init__(self, serviceProviderId=None, groupId=None, userId=None, lastName=None, firstName=None, callingLineIdLastName=None, callingLineIdFirstName=None, properties=None):
        self.command_name = "UserAddRequest22"
        self.node_name = "command"
        self.serviceProviderId = serviceProviderId
        self.groupId = groupId
        self.userId = userId
        self.lastName = lastName
        self.firstName = firstName
        self.callingLineIdLastName = callingLineIdLastName
        self.callingLineIdFirstName = callingLineIdFirstName
        self.properties = properties

    def _export(self):
        root = ET.Element(self.node_name)
        root.set("xmlns:xsi", "http://www.w3.org/2001/XMLSchema-instance")
        root.set("xsi:type", self.command_name)
        if not self.serviceProviderId:
            raise RequiredField("ServiceProviderID is a required field")
        ET.SubElement(root, "serviceProviderId").text = self.serviceProviderId
        if not self.groupId:
            raise RequiredField("GroupID is a required field")
        ET.SubElement(root, "groupId").text = self.groupId
        if not self.userId:
            raise RequiredField("userId is a required field")
        ET.SubElement(root, "userId").text = self.userId
        if not self.lastName:
            raise RequiredField("lastName is a required field")
        ET.SubElement(root, "lastName").text = self.lastName
        if not self.firstName:
            raise RequiredField("firstName is a required field")
        ET.SubElement(root, "firstName").text = self.firstName
        if not self.callingLineIdLastName:
            raise RequiredField("callingLineIdLastName is a required field")
        ET.SubElement(
            root, "callingLineIdLastName").text = self.callingLineIdLastName
        if not self.callingLineIdFirstName:
            raise RequiredField("callingLineIdFirstName is a required field")
        ET.SubElement(
            root, "callingLineIdFirstName").text = self.callingLineIdFirstName
        if self.properties:
            for props, values in self.properties.items():
                ET.SubElement(root, props).text = values
        return ET.tostring(root)


# New Request function for Release 22:
class UserModifyRequest22(OCIRequest):

    """ Modify User profile parameters fuction for Release 22. 

    Parameters:

    userId = BW user id
    properties = Dictionary with properties and values.
    Ex: properties = {'lastName': 'BR', 'firstName': 'Mandrick'}

    The dictionary must respect the sequence specified on the XSD schema.

    Returns either a success message or an error message.

    """

    def __init__(self, userId, properties=None):
        self.command_name = "UserModifyRequest22"
        self.node_name = "command"
        self.userId = userId
        self.properties = properties
        self.create_command_root()

    def _export(self):
        root = ET.Element(self.node_name)
        root.set("xmlns:xsi", "http://www.w3.org/2001/XMLSchema-instance")
        root.set("xsi:type", self.command_name)
        if not self.userId:
            raise RequiredField("userId is a required field")
        ET.SubElement(root, "userId").text = self.userId
        if not self.properties:
            raise RequiredField(
                "Please provide the propeties and values you want to change")
        else:
            for props, values in self.properties.items():
                ET.SubElement(root, props).text = values
            return ET.tostring(root)


class UserDeleteRequest(OCIRequest):
    """ Request to delete a user.  The response is either SuccessResponse or ErrorResponse."""

    def __init__(self, userId):
        self.command_name = "UserDeleteRequest"
        self.node_name = "command"
        self.userId = userId
        self.create_command_root()

    def _export(self):
        root = ET.Element(self.node_name)
        root.set("xmlns:xsi", "http://www.w3.org/2001/XMLSchema-instance")
        root.set("xsi:type", self.command_name)
        if not self.userId:
            raise RequiredField("userId is a required field")
        ET.SubElement(root, "userId").text = self.userId
        return ET.tostring(root)
