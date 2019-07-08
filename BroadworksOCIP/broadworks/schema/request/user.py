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
            ET.SubElement(root, "usePersonalizedName").text = self.usepersonalizedname
        if self.auto_login:
            ET.SubElement(root,"voicePortalAutoLogin").text = "true"
        if self.personalizednameaudiofile:
            ET.SubElement(root, "personalizedNameAudioFile").text = self.personalizednameaudiofile
        return ET.tostring(root)


class UserModifyRequest17sp4(OCIRequest):

    def __init__(self):
        pass



class Test:
    pass