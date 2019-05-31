import io
from BroadworksOCIP.broadworks.schema import \
    UserGetListInSystemRequest as UserSys

from BroadworksOCIP.broadworks.schema import \
    BroadsoftDocument


class UserGetListInSystemRequest:

    def __init__(self):
        self.broadsoft_doc = BroadsoftDocument()
        self.command = UserSys()
        self.broadsoft_doc.protocol = "OCI"
        self.command
        self.broadsoft_doc.add_command(self.command)
        self.inmemfile = io.StringIO()

    def get_raw_xml(self):
        self.broadsoft_doc.export(self.inmemfile,0)
        print(self.inmemfile.getvalue())



    def get_bw_session(self):
        pass

    def searchcriteria(self, searchtype=None):
        pass
