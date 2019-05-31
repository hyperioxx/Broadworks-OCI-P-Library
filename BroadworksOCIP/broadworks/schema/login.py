import xml.etree.cElementTree as ET

class AuthenticationRequest:

    def __init__(self, userId=None):
        self.command_name = "AuthenticationRequest"
        self.node_name = "command"
        self.userId = userId

    def __repr__(self):
        return self._export().decode('utf-8')

    def __str__(self):
        return self._export().decode('utf-8')

    def _export(self):
        root = ET.Element(self.node_name, xmlns="")
        root.set("xmlns:xsi","http://www.w3.org/2001/XMLSchema-instance")
        root.set("xsi:type", self.command_name)
        root.set("xmlns", "")
        if self.userId:
            userId = ET.SubElement(root,"userId").text = self.userId
        return ET.tostring(root)


