import xml.etree.cElementTree as ET
from BroadworksOCIP.broadworks.schema.request.base import OCIRequest
from BroadworksOCIP.broadworks.errors import RequiredField

class AuthenticationRequest(OCIRequest):

    def __init__(self, userId=None):
        self.command_name = "AuthenticationRequest"
        self.node_name = "command"
        self.userId = userId
        self.create_command_root()

    def _export(self):
        if self.userId:
            ET.SubElement(self.root,"userId").text = self.userId
        return ET.tostring(self.root)



class LoginRequest14sp4(OCIRequest):

    def __init__(self, userId=None, signedpassword=None, plaintextpassword=None):
        self.command_name = "LoginRequest14sp4"
        self.node_name = "command"
        self.userId = userId
        self.signedpassword = signedpassword
        self.plaintextpassword = plaintextpassword
        self.create_command_root()

    def _export(self):
        if not self.userId:
            raise RequiredField("missing required field: username")
        if self.userId:
            ET.SubElement(self.root,"userId").text = self.userId
        if self.signedpassword:
            ET.SubElement(self.root, "signedPassword").text = self.signedpassword
        if self.plaintextpassword:
            ET.SubElement(self.root, "plainTextPassword").text = self.plaintextpassword

        return ET.tostring(self.root)


