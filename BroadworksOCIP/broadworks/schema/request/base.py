import xml.etree.cElementTree as ET

class OCIRequest:

    def __repr__(self):
        return self._export().decode('utf-8')

    def __str__(self):
        return self._export().decode('utf-8')

    def create_command_root(self):
        self.root = ET.Element(self.node_name)
        self.root.set("xmlns:xsi", "http://www.w3.org/2001/XMLSchema-instance")
        self.root.set("xsi:type", self.command_name)

    def _export(self):
        raise NotImplementedError()