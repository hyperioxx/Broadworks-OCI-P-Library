import xml.etree.cElementTree as ET

class BroadsoftDocument:
    """
    Every Message starts with a BroadsoftDocument tag.
    """

    def __init__(self, protocol=None, sessionId=None, userId=None, phoneNumber=None):
        self.node_name = "BroadsoftDocument"
        self.protocol = protocol
        self.sessionId = sessionId
        self.userId = userId
        self.phoneNumber = phoneNumber
        self.commands = []

    def __repr__(self):
        return self._export().decode('utf-8')


    def __str__(self):
        return self._export().decode('utf-8')


    def add_command(self, command):
        self.commands.append(command)

    def _export(self):
        root = ET.Element(self.node_name, xmlns="C")
        root.set("xmlns:xsi","http://www.w3.org/2001/XMLSchema-instance")
        if self.sessionId:
            sessionId = ET.SubElement(root, 'sessionId', xmlns="").text = str(self.sessionId)
        if self.userId:
            userId = ET.SubElement(root, 'userId', xmlns="").text = self.userId
        if self.phoneNumber:
            phoneNumber = ET.SubElement(root, 'phoneNumber', xmlns="").text = self.phoneNumber
        for command in self.commands:
            command = root.append(ET.fromstring(str(command)))

        return ET.tostring(root)





class ErrorResponse:
    pass
